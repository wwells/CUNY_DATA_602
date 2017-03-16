"""HW7 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'


Take what you did on homework 5 as a starting point (using any of the provided datasets).  
Replace the regression calculation using least squares with a curve fitting approach 
(examples in the reading).  To start, just fit a linear equation.  Output the equation to the 
console.  You don't need to graph anything (we'll look at that in a couple more weeks).

Again, using timeit, compare the performance of your solution in homework 5 to the scipy 
function.  Output the results to the console.

(Optional)  There are other models that can be fitted to the data we have.  Try to fit other 
equations, like Gaussian, to the data.  Output the equation to the console.

"""
import timeit
import urllib2
import csv
import copy
import numpy as np 
from scipy.optimize import curve_fit

class getfile:
	'a class for loading and cleaning brainandbody.csv'

	def __init__(self, url):
		self.url = url 
		self.filename = urllib2.urlopen(self.url)
		self.f = list(csv.reader(self.filename))

		del self.f[0] #remove headers
		self.f = [c[:1] + map(float, c[1:]) for c in self.f] # convert col2 + 3 to float

### hw5 solution
def mean_calc(data, col):
	"""get mean of a column"""
	m = sum([row[col] for row in data]) / len(data)
	return m

def var_calc(data, col, mean):
	"""get variance of a column"""
	v = sum([(mean - row[col])**2 for row in data])
	return v

def cov_calc(data, xcol, xmean, ycol, ymean): 
	"""get covariance"""
	covariance = sum([(row[xcol]-xmean) * (row[ycol]-ymean) for row in data])
	return covariance

def get_regression(data):
	"""use helper functions to calculate linear regression line"""
	xmean = mean_calc(data, 1)
	xvariance = var_calc(data, 1, xmean)
	ymean = mean_calc(data, 2)
	yvariance = var_calc(data, 2, ymean)
	covariance = cov_calc(data, 1, xmean, 2, ymean)
	B1 = round(covariance / xvariance, 4)
	B0 = round(ymean - B1 * xmean, 4)

## scipy curve_fit helpers and fit function to time
def lin_func(x, a, b):
	return a * x + b

def gauss_func(x, a, b, c):
	return a*np.exp(-(x-b)**2/(2*c**2))

def scipy_curve_fit(func):
	popt, pcov = curve_fit(func, x, y)


if __name__ == '__main__':
	url = 'https://raw.githubusercontent.com/wwells/CUNY_DATA_602/master/L05/brainandbody.csv'
	R = getfile(url)
	d = R.f
	x = [row[1] for row in d]
	y = [row[2] for row in d]
	n = 10000

	t = timeit.Timer(lambda: get_regression(d))
	print 'Built in Method: %s: %s loops = %s seconds' % ('get_regression', n, t.timeit(n))
	t = timeit.Timer(lambda: scipy_curve_fit(lin_func))
	print 'Scipy Linear Fit: %s: %s loops = %s seconds' % ('scipy_curve_fit(lin_func)', n, t.timeit(n))
	t = timeit.Timer(lambda: scipy_curve_fit(gauss_func))
	print 'Scipy Gauss Fit: %s: %s loops = %s seconds' % ('scipy_curve_fit(gauss_func)', n, t.timeit(n))	
	


