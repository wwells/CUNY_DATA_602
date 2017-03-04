"""HW5 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'

Download the new data set on the Lesson 5 page called brainandbody.csv.  
This file is a small set of average brain weights and average body weights for a number of animals.  
We want to see if a relationship exists between the two. (This data set acquired above).

Perform a linear regression using the least squares method on the relationship of 
brain weight [br] to body weight [bo].  Do this using just the built in Python functions 
(this is really easy using scipy, but we're not there yet).  We are looking for a model 
in the form bo = X * br + Y.  Find values for X and Y and print out the entire model to 
the console.
"""

from Tkinter import Tk
from tkFileDialog import askopenfilename
import csv

class Regression:
	'a class for performing least squares method of linear regression'

	def __init__(self):
		"""initialize class by picking a file using tkinter gui"""
		self.GUI = Tk()
		self.GUI.withdraw()
		self.GUI.update()
		self.filename = askopenfilename()

		print '\nLoading %s...' % self.filename
		self.f = list(csv.reader(open(self.filename, 'r')))

		del self.f[0] #remove headers
		self.f = [c[:1] + map(float, c[1:]) for c in self.f] # convert col2 + 3 to float


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

	print 'X:  mean = %s, variance = %s' % (xmean, xvariance)
	print 'Y:  mean = %s, variance = %s' % (ymean, yvariance)

	covariance = cov_calc(data, 1, xmean, 2, ymean)
	print 'Covariance x,y = %s' % covariance

	B1 = round(covariance / xvariance, 4)
	B0 = round(ymean - B1 * xmean, 4)
	print ''
	print 'Linear Regression Equation:'
	print 'Body Weight = %s * Brain Weight + %s' % (B1, B0)
	print ''


if __name__ == '__main__':
	
	R = Regression()
	d = R.f
	print ''
	get_regression(d)
	print '------------------------------------------------'
	print 'Analysis:'
	print 'Body Weight outliers like the two elephants make the Y intercept'
	print '	larger than the expected body weight of 51 of the 62 animals'
	print 'What happens when we remove the two elephant outliers?'
	print '------------------------------------------------'
	print ''

	adj = d[:-2]
	get_regression(adj)

# reference:
# http://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/
