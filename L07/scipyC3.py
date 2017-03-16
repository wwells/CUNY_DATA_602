import numpy as np 
from scipy.optimize import curve_fit

## 3.1.1 data model and fitting
# Creating a function to model and create data
def linfunc(x, a, b):
	return a * x + b

def gaussfunc(x, a, b, c):
	return a*np.exp(-(x-b)**2/(2*c**2))

def twogaussfunc(x, a0, b0, c0, a1, b1,c1):
	return a0*np.exp(-(x - b0) ** 2/(2 * c0 ** 2))\
		+ a1 * np.exp(-(x - b1) ** 2/(2 * c1 ** 2))

x = np.linspace(0, 10, 100)
yl = linfunc(x, 1, 2)
yln = yl + 0.9 * np.random.normal(size=len(x))
yg = gaussfunc(x, 1, 5, 2)
ygn = yg + 0.2 * np.random.normal(size=len(x))
y2g = twogaussfunc(x, 1, 3, 1, -2, 15, 0.5)
y2n = y2g + 0.2 * np.random.normal(size=len(x))
guesses = [1, 3, 1, 1, 15, 1]

#Executing curve_fit on noisy data
lpopt, lpcov = curve_fit(linfunc, x, yln)
gpopt, gpcov = curve_fit(gaussfunc, x, ygn)
twogpopt, twogpcov = curve_fit(twogaussfunc, x, y2n, p0=guesses)

# 3.1.2 solutions to functions
from scipy.optimize import fsolve

line = lambda x: x + 3

solution = fsolve(line, -2)
print solution

# Defining function to simplify intersection solution
def findIntersection(func1, func2, x0):
	return fsolve(lambda x : func1(x) - func2(x), x0)

funky = lambda x : np.cos(x / 5) * np.sin(x / 2)
line = lambda x : 0.01 * x - 0.5

x = np.linspace(0,45,10000)
result = findIntersection(funky, line, [15, 20, 30, 35, 40, 45])

print(result, line(result))

# 3.2 interpolation
from scipy.interpolate import interp1d
x = np.linspace(0, 10 * np.pi, 20)
y = np.cos(x)

fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')
xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
yintq = fq(xint)

import matplotlib.pyplot as mpl
from scipy.interpolate import UnivariateSpline

sample = 30
x = np.linspace(1, 10 * np.pi, sample)
y = np.cos(x) + np.log10(x) + np.random.randn(sample) / 10

f = UnivariateSpline(x, y, s=1)
xint = np.linspace(x.min(), x.max(), 1000)
yint = f(xint)

## interpolate image using griddata

from scipy.interpolate import griddata
# Defining a function
ripple = lambda x, y: np.sqrt(x**2 + y**2)+np.sin(x**2 + y**2)
# Generating gridded data. The complex number defines
# how many steps the grid data should have. Without the
# complex number mgrid would only create a grid data structure
# with 5 steps.
grid_x, grid_y = np.mgrid[0:5:1000j, 0:5:1000j]
# Generating sample that interpolation function will see
xy = np.random.rand(1000, 2)
sample = ripple(xy[:,0] * 5 , xy[:,1] * 5)
# Interpolating data with a cubic
grid_z0 = griddata(xy * 5, sample, (grid_x, grid_y), method='cubic')


## 3.3 Integration
from scipy.integrate import quad
# Defining function to integrate
func = lambda x: np.cos(np.exp(x)) ** 2
# Integrating function with upper and lower
# limits of 0 and 3, respectively
solution = quad(func, 0, 3)
print solution
# The first element is the desired value
# and the second is the error.


from scipy.integrate import quad, trapz

x = np.sort(np.random.randn(150) * 4 + 4).clip(0,5)
func = lambda x: np.sin(x) * np.cos(x ** 2) + 1
y = func(x)
# Integrating function with upper and lower
# limits of 0 and 5, respectively
fsolution = quad(func, 0, 5)
dsolution = trapz(y, x=x)
print('fsolution = ' + str(fsolution[0]))
print('dsolution = ' + str(dsolution))
print('The difference is ' + str(np.abs(fsolution[0] - dsolution)))

## 3.4 Stats
# Constructing a random array with 1000 elements
x = np.random.randn(1000)
# Calculating several of the built-in methods
# that numpy.array has
mean = x.mean()
std = x.std()
var = x.var()

from scipy.stats import norm
# Set up the sample range
x = np.linspace(-5,5,1000)
# Here set up the parameters for the normal distribution,
# where loc is the mean and scale is the standard deviation.
dist = norm(loc=0, scale=1)
# Retrieving norm's PDF and CDF
pdf = dist.pdf(x)
cdf = dist.cdf(x)
# Here we draw out 500 random values from the norm.
sample = dist.rvs(500)

from scipy.stats import geom
# Here set up the parameters for the geometric distribution.
p = 0.5
dist = geom(p)
# Set up the sample range.
x = np.linspace(0, 5, 1000)
# Retrieving geom's PMF and CDF
pmf = dist.pmf(x)
cdf = dist.cdf(x)
# Here we draw out 500 random values.
sample = dist.rvs(500)

from scipy import stats
# Generating a normal distribution sample
# with 100 elements
sample = np.random.randn(100)
# normaltest tests the null hypothesis.
out = stats.normaltest(sample)
print ''
print('normaltest output')
print('Z-score = ' + str(out[0]))
print('P-value = ' + str(out[1]))
# kstest is the Kolmogorov-Smirnov test for goodness of fit.
# Here its sample is being tested against the normal distribution.
# D is the KS statistic and the closer it is to 0 the better.
out = stats.kstest(sample, 'norm')
print('\nkstest output for the Normal distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))
# Similarly, this can be easily tested against other distributions,
# like the Wald distribution.
out = stats.kstest(sample, 'wald')
print('\nkstest output for the Wald distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))
print ''

# The harmonic mean: Sample values have to
# be greater than 0.
out = stats.hmean(sample[sample > 0])
print('Harmonic mean = ' + str(out))
# The mean, where values below -1 and above 1 are
# removed for the mean calculation
out = stats.tmean(sample, limits=(-1, 1))
print('\nTrimmed mean = ' + str(out))
# Calculating the skewness of the sample
out = stats.skew(sample)
print('\nSkewness = ' + str(out))
# Additionally, there is a handy summary function called
# describe, which gives a quick look at the data.
out = stats.describe(sample)
print('\nSize = ' + str(out[0]))
print('Min = ' + str(out[1][0]))
print('Max = ' + str(out[1][1]))
print('Mean = ' + str(out[2]))
print('Variance = ' + str(out[3]))
print('Skewness = ' + str(out[4]))
print('Kurtosis = ' + str(out[5]))

## 3.5 Clustering
from scipy.cluster import vq
# Creating data
c1 = np.random.randn(100, 2) + 5
c2 = np.random.randn(30, 2) - 5
c3 = np.random.randn(50, 2)
# Pooling all the data into one 180 x 2 array
data = np.vstack([c1, c2, c3])
# Calculating the cluster centroids and variance
# from kmeans
centroids, variance = vq.kmeans(data, 3)
# The identified variable contains the information
# we need to separate the points in clusters
# based on the vq function.
identified, distance = vq.vq(data, centroids)
# Retrieving coordinates for points in each vq
# identified core
vqc1 = data[identified == 0]
vqc2 = data[identified == 1]
vqc3 = data[identified == 2]

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import pdist, squareform
import scipy.cluster.hierarchy as hy

# Creating a cluster of clusters function
def clusters(number = 20, cnumber = 5, csize = 10):
	# Note that the way the clusters are positioned is Gaussian randomness.
	rnum = np.random.rand(cnumber, 2)
	rn = rnum[:,0] * number
	rn = rn.astype(int)
	rn[np.where(rn < 5 )] = 5
	rn[np.where(rn > number/2. )] = round(number / 2., 0)
	ra = rnum[:,1] * 2.9
	ra[np.where(ra < 1.5)] = 1.5
	cls = np.random.randn(number, 3) * csize
	# Random multipliers for central point of cluster
	rxyz = np.random.randn(cnumber-1, 3)
	for i in xrange(cnumber-1):
		tmp = np.random.randn(rn[i+1], 3)
		x = tmp[:,0] + ( rxyz[i,0] * csize )
		y = tmp[:,1] + ( rxyz[i,1] * csize )
		z = tmp[:,2] + ( rxyz[i,2] * csize )
		tmp = np.column_stack([x,y,z])
		cls = np.vstack([cls,tmp])
	return cls

# Generate a cluster of clusters and distance matrix.
cls = clusters()
D = pdist(cls[:,0:2])
D = squareform(D)
# Compute and plot first dendrogram.
fig = mpl.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
Y1 = hy.linkage(D, method='complete')
cutoff = 0.3 * np.max(Y1[:, 2])
Z1 = hy.dendrogram(Y1, orientation='right', color_threshold=cutoff)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
Y2 = hy.linkage(D, method='average')
cutoff = 0.3 * np.max(Y2[:, 2])
Z2 = hy.dendrogram(Y2, color_threshold=cutoff)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
# Plot distance matrix.
ax3 = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
D = D[idx1,:]
D = D[:,idx2]
ax3.matshow(D, aspect='auto', origin='lower', cmap=mpl.cm.YlGnBu)
ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)
# Plot colorbar.
fig.savefig('cluster_hy_f01.pdf', bbox = 'tight')

# Same imports and cluster function from the previous example
# follow through here.
# Here we define a function to collect the coordinates of
# each point of the different clusters.
def group(data, index):
	number = np.unique(index)
	groups = []
	for i in number:
		groups.append(data[index == i])
	return groups

# Creating a cluster of clusters
cls = clusters()
# Calculating the linkage matrix
Y = hy.linkage(cls[:,0:2], method='complete')
# Here we use the fcluster function to pull out a
# collection of flat clusters from the hierarchical
# data structure. Note that we are using the same
# cutoff value as in the previous example for the dendrogram
# using the 'complete' method.
cutoff = 0.3 * np.max(Y[:, 2])
index = hy.fcluster(Y, cutoff, 'distance')
# Using the group function, we group points into their
# respective clusters.
groups = group(cls, index)
# Plotting clusters
fig = mpl.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
colors = ['r', 'c', 'b', 'g', 'orange', 'k', 'y', 'gray']
for i, g in enumerate(groups):
	i = np.mod(i, len(colors))
	ax.scatter(g[:,0], g[:,1], c=colors[i], edgecolor='none', s=50)
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)

fig.savefig('cluster_hy_f02.pdf', bbox = 'tight')

## 3.6 Signal and Image processing

## 3.7 Sparse Matrices

from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh
import scipy.sparse
import time

N = 3000
# Creating a random sparse matrix
m = scipy.sparse.rand(N, N)
# Creating an array clone of it
a = m.toarray()
print('The numpy array data size: ' + str(a.nbytes) + ' bytes')
print('The sparse matrix data size: ' + str(m.data.nbytes) + ' bytes')
# Non-sparse
t0 = time.time()
res1 = eigh(a)
dt = str(np.round(time.time() - t0, 3)) + ' seconds'
print('Non-sparse operation takes ' + dt)
# Sparse
t0 = time.time()
res2 = eigsh(m)
dt = str(np.round(time.time() - t0, 3)) + ' seconds'
print('Sparse operation takes ' + dt)

