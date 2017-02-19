#!/usr/bin/env python

"""HW3 for CUNY 602:  Advanced Programming Techniques, Spring 2017"""

__author__= "Walt Wells"

# to validate: http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.names


from Tkinter import Tk
from tkFileDialog import askopenfilename
import csv
import re
#from operator import getitem
#from operator import itemgetter

"""create global dictionary with ordinal rankings to validate and sort against"""
buyingDict = dict([('vhigh', 4), ('high', 3), ('med', 2), ('low', 1)])
maintDict = dict([('vhigh', 4), ('high', 3), ('med', 2), ('low', 1)])
doorsDict = dict([('2', 2), ('3', 3), ('4', 4), ('5more', 5)])
personsDict = dict([('2', 2), ('4', 4), ('more', 6)])
lug_bootDict = dict([('small', 1), ('med', 2), ('big', 3)])
safetyDict = dict([('low', 1), ('med', 2), ('high', 3)])
classDict = dict([('unacc', 1), ('acc', 2), ('good', 3), ('vgood', 4)])

globalDict = {'buying': buyingDict, 'maint': maintDict, 'doors': doorsDict, 
	'persons': personsDict, 'lug_boot': lug_bootDict, 'safety': safetyDict, 'class': classDict}


class Cars:
	'a class for importing and organizing and validating car data'

	def __init__(self):
		"""initialize class by picking a file using tkinter gui"""
		self.GUI = Tk()
		self.GUI.withdraw()
		self.GUI.update()
		self.filename = askopenfilename()

		print '\nLoading %s...' % self.filename
		self.f = csv.reader(open(self.filename, 'r'))

	def format(self):
		"""pulls picked file into an initial dictionary"""
		self.cars = []
		for row in self.f:
			self.cars.append({'buying': row[0], 
				'maint': row[1], 
				'doors': row[2],
				'persons': row[3],
				'lug_boot': row[4],
				'safety': row[5],
				'class': row[6]})

	def validate(self):
		"""confirm all file values are the expected ones, else IO Error"""
		try:
			print 'Validating data values...'
			self.n = 0
			for i in self.cars:
				self.n += 1
				for k in i.keys():
					if globalDict[k].has_key(i[k]):
						pass
					else:
						print 'Key: ["%s"] has bad value: %s \n Line[%s]: %s' % (k, i[k], self.n, i)
			print '------------------------------'
		except IOError:
			print 'Cannot validate file'

	def addvalue(self):
		"""add second value to key list in dictionary indicating ordinal variable values

		NOTE:   this is not called in the final program, but successfully appended global dictionary 
		values to the main dataset, creating a list of dictionaries with k: dictionary."""
		try: 
			print 'Adding ordinal values to dataset...'
			for row in self.cars:
				for (k, v) in row.items():
					row[k] = {v : globalDict[k][v]}
		except IOError:
			print 'test error'


# Helper Functions

def sortby(data, key, ascending=True):
	"""sort by key value

	NOTE:   I had a bear of a time trying to sort by ordinal categorical variables.  
	The attempted method was to try and sort against a value dictionary, but I couldn't pull it off. 
	The function below sorts by string value, not ordinal value :( 
	
	A good exercise to try this, but I look forward to using python libraries for managing dataframes moving forward.  
	"""

	if ascending: 
		a = 'ascending'; r = False
	else: 
		a = 'descending'; r = True
	sub = sorted(data, key=lambda x: x[key], reverse=r)
	#sub = sorted(data, key = lambda k:  k[key]==globalDict[key].__getitem__, reverse = r)
	#sub = sorted(data, key=lambda x: itemgetter('persons')==globalDict['persons'].__getitem__, reverse=r)
	print 'Sorting by %s in %s order...' % (key, a)
	return sub

def printnrow(data, n, top=True):
	"""print nrows from top or bottom"""
	if top:  t = 'top'
	else:  t = 'bottom'
	print 'Printing the %s %s rows...' % (t, n)
	if top:
		for i in range(n):
			print data[i]
	else:
		for i in range(n):
			print data[-n]
	print '------------------------------'


def subset(data, key, values):
	"""subset given data based on inputs using re.startswith"""
	result = []
	for row in data: 		
		for k, v in row.iteritems():
			if k.startswith(key) and (v.startswith(values[0]) or v.startswith(values[1])):
				result.append(row)
	return result

def savefile(file):
		"""save list of dictionaries into csv"""
		keys = file[0].keys()
		with open('caroutput.csv', 'wb') as f:
			writer = csv.DictWriter(f, keys)
			writer.writeheader()
			writer.writerows(file)
			print 'Saving file...'


# Main of the program
if __name__ == '__main__':
	D = Cars()
	D.format()
	D.validate()
	#D.addvalue()
	data = D.cars

	# Print to the console the top 10 rows of the data sorted by 'safety' in descending order
	s_sort = sortby(data,'safety', ascending=False)	
	printnrow(s_sort, 10, top=True)

	# Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
	m_sort = sortby(data, 'maint', ascending=True)
	printnrow(m_sort, 15, top=False)

	# Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', 
	# sorted by 'doors' in ascending order.  Find these matches using regular expressions.
	v = ['vhigh','high']
	s1 = subset(data, 'buying', v)
	s2 = subset(s1, 'maint', v)
	s3 = subset(s2, 'safety', v)
	sub_sort = sortby(s3, 'doors', ascending=True)
	printnrow(sub_sort, len(sub_sort))

	# Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, 
	# and 'persons': 4 or more.  The file path can be a hard-coded location (name it output.txt) or 
	# use a dialog box.  
	save_sub1 = subset(data, 'buying', ['vhigh', 'x'])
	save_sub2 = subset(save_sub1, 'maint', ['med', 'x'])
	save_sub3 = subset(save_sub2, 'doors', ['4', 'x'])
	savefile(save_sub3)




