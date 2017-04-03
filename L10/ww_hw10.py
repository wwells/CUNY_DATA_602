"""HW10 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'

In this homework we will explore the matplotlib library and its features by 
plotting the results of previous assignments.  

1) Express the cars.data.csv data as a series of bar graphs.  The x-axis represents 
a feature and the y-axis is the frequency in the sample.  Do this with the 'buying', 
'maint', 'safety', and 'doors' fields with one plot for each for a total of four.  
Make each graph a subplot of a single output.  

2) Plot your results from the linear regression in homework 5 and 7 (for any of the 
provided data sets).  The plot should include.  1) a scatter of the points in the 
.csv file 2) a line showing the regression line (either from the calculation in 
homework 5 or line-fitting from homework 7).  3) something on the plot that specifies 
the equation for the regression line.  

3) Create an overlay of the center points found in objects.png from homework 8.  The 
image should be in the background and the object centers can be small circles or 
points at or around the center points.

4) Plot a line graph that shows the hour by hour change in number of server requests 
from the HTTP in homework 9.  The x-axis is the discrete hour intervals (e.g. 13:00 – 
14:00) and the y-axis is the number of requests.  

References: 


"""
import scipy.ndimage as ndimage
import scipy.misc as misc
import mahotas as mh


class ImageCount:
	'a class for thresholding, counting objects, and finding the center of objects in an image'

	def __init__(self, file):
		self.file = file
		self.raw = misc.imread(self.file)

	def threshold(self, value, outfile, save=True):
		"""use scipy gaussian_filter to convert a greyscale image to B&W based on threshold"""
		
		self.value = value
		self.outfile = outfile
		self.img = ndimage.gaussian_filter(self.raw, self.value)
		self.T = mh.thresholding.otsu(self.img)
		self.result = self.img > self.T
		
		if save: misc.imsave(self.outfile, self.result)

	def count_and_measure(self):
		"""find number of white obj in converted image, count center"""

		self.labels, self.count = mh.label(self.result)
		print 'Image: %s | Number of Objects: %d ' % (self.file, self.count)

		for i in range(1,self.count+1):
			self.center = ndimage.measurements.center_of_mass(self.result, self.labels, i)
			print 'Object %s with center at: %s ' % (i,  self.center[0:2])
		print ""


if __name__ == '__main__':
	objects = ImageCount('objects.png')
	objects.threshold(3, 'objects_BW.png')
	objects.count_and_measure()

	circles = ImageCount('circles.png')
	circles.threshold(10, 'circles_BW.png')
	circles.count_and_measure()

	peppers = ImageCount('peppers.png')
	peppers.threshold(3, 'peppers_BW.png')
	peppers.count_and_measure()