"""HW6 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'

Do both of the following:

Using your submission of homework 1 as a base, replace as many of the functions 
as you can with numpy functions.  For example, instead of using your sort function that you 
wrote, use numpy.sort.  Refer to here for most of the functions you'll need.   

Using the timeit function measure the execution times of all the sort and search functions 
you have.  You'll most likely need to do a large number of tests on each one to get a meaningful 
result.  Something like 10000 or more.  

Your submission will be a single file that has all the functions from homework 1 
and the additional approach using numpy.  Additionally, you will have the timing of all 
the functions output to the console. Something like.

    Sort using iteration:  x loops = y seconds
    Sort using built in python: x' loops = y' seconds
    Sort using numpy: x'' loops  = y''seconds

You fill in all the values for x and y.
"""
import timeit

setup = '''
import random
import numpy
import copy

## sorting
def sortwithloops(input):
    l = []
    for val in input:
        l.append(val)
        for i in range(len(l)-1):
            j = i + 1
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def sortwithoutloops(input): 
    input.sort()
    return input

def numpysort(input): 
	return numpy.sort(input)

## searching
def searchwithloops(input, value):
    result = False
    for i in input:
        if i == value:
            result = True
            break
    return result

def searchwithoutloops(input, value):
    return value in input  

def numpysearch(input, value):
	return value in input

L = [random.randint(0,1000) for r in xrange(100)]
NL = numpy.array(L)

'''


def timing(function, n, numpy=False, search=False):
	DF = 'L'
	if numpy: DF = 'NL'
	call = 'x=copy.copy(' + DF + ');' + function + '(x)'
	if search: 
		call = 'x=copy.copy(' + DF + ');' + function + '(x, 1)'
	t = timeit.Timer(call, setup=setup)
	print '%s: %s loops = %s seconds' % (function, n, t.timeit(n))


if __name__ == '__main__':
	
	n = 10000	
	timing('sortwithloops', n)
	timing('sortwithoutloops', n)
	timing('numpysort', n, numpy=True)
	print ''
	timing('searchwithloops', n, search=True)
	timing('searchwithoutloops', n, search=True)
	timing('numpysearch', n, numpy=True, search=True)
	print ''


