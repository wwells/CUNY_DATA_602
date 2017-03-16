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