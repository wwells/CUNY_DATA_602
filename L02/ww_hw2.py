#1. fill in this class
#   it will need to provide for what happens below in the
#  main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
#  a function called showEvaluation, and an attribute carCount

class CarEvaluation:
	'A simple class that represents a car evaluation'

	carCount = 0
	def __init__(self, Brand, Price, SafetyR):
		self.Brand = Brand
		self.Price = Price
		self.SafetyR = SafetyR
		self.__class__.carCount += 1

	def showEvaluation(self):
		print "The %s has a %s price and its safety is rated a %d" % (self.Brand, self.Price, self.SafetyR)		

#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
#  otherwise by descending price

def sortbyprice(list, order):
	sorted = []
	for i in list:
		if i.Price == "Low":
			sorted.append(i.Brand)
		elif i.Price == "Med":
			sorted.append(i.Brand)
		else:
			sorted.append(i.Brand)
	if order == "asc":
		sorted.reverse()
	return sorted

#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#  it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false

def searchforsafety(list, rating): 
	exists = False
	for i in list: 
		if i.SafetyR == rating:
			exists = True
			break
	return exists 
            
# This is the main of the program.  Expected outputs are in comments after the function calls.
# Attempted to evaluate using principles of reflection
if __name__ == "__main__": 

	classname = "CarEvaluation"
	eval1 = globals()[classname]("Ford", "High", 2)
	eval2 = globals()[classname]("GMC", "Med", 4)
	eval3 = globals()[classname]("Toyota", "Low", 3)

	print "Car Count = %d" % getattr(CarEvaluation, "carCount") 

	getattr(eval1, "showEvaluation")() 
	getattr(eval2, "showEvaluation")() 
	getattr(eval3, "showEvaluation")() 

	L = [eval1, eval2, eval3]

	print eval("sortbyprice(L, 'asc')")
	print eval("sortbyprice(L, 'des')")
	print eval("searchforsafety(L, 2)")
	print eval("searchforsafety(L, 1)")

