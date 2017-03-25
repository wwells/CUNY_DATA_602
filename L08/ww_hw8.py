"""HW8 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'

This homework will give you a chance to explore some image processing techniques in Python.  
These are some of the most basic tasks done in image processing.  First, download the image 
package attached to this lesson.  On each image you will count the number of objects in the 
image and find their center points.  The images in order of complexity are circles.png, 
objects.png and peppers.png. Using Python's built-in functionality, scipy, or any other 
module, perform the following tasks:


Thresholding: First convert the image to a binary image.  This is done with a technique 
called thresholding, which is covered in the reading.  There are functions for it in 
scipy, although it is very easy to do manually.  Essentially read each pixel and if it 
above a specified gray level make it white, otherwise make it black.

Count objects:  Count the number of objects in the image.  If you are interested in how 
this is done, refer to the additional readings.  An object will be a group of white pixels 
surrounded by black pixels.  Doing this by hand is also fairly easy, but try to use 
functions found in the modules available.

Find center points: For each object, find the center point in terms of x,y coordinates.  
As with part 3, you can do this directly, but it's better to use something from a 
module.

Image files can be read in directly or you can use a dialog box.  Your output will list 
the objects and midpoints for each image.  Remember, the focus here is to use readily 
available Python functions to do image processing rather than gain a deep understanding 
of the theory of the techniques.   

"""
import scipy.ndimage as ndimage
import scipy.misc as misc


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
		self.thres = self.img > self.img.mean()
		if save: misc.imsave(self.outfile, self.thres)






if __name__ == '__main__':
	objects = ImageCount('objects.png')
	objects.threshold(1, 'objects_BW.png')

