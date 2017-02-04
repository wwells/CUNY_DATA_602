#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions

def sortwithloops(input):
    l = []
    for val in input:
        l.append(val)
        for i in range(len(l)-1):
            j = i + 1
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
	
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop

def sortwithoutloops(input): 
    input.sort()
    return input

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions

def searchwithloops(input, value):
    result = False
    for i in input:
        if i == value:
            result = True
            break
    return result

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop

def searchwithoutloops(input, value):
    return value in input  

## TEST

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print "sortwithLoops 1: \n %s" %  sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print "sortwithoutLoops 2: \n %s" % sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print "searchwithloops 3a: \n %s" % searchwithloops(L, 5) #true
    print "searchwithloops 3b: \n %s" % searchwithloops(L, 11) #false
    print "searchwithoutloops 4a: \n %s" % searchwithoutloops(L, 5) #true
    print "searchwithoutloops 4b: \n %s" % searchwithoutloops(L, 11) #false