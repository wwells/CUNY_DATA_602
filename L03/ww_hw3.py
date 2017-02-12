'''
    Loads in the data from cars.data.csv.  The data can be stored anyway you choose, in any data structure you choose (probably a list of some kind).  The data should load on start-up by referencing a file path, or even better, a file picker dialog box.
    In the main portion of your program you should run the following operations and print the result to the console (except number 4).  How you achieve this is up to you.  However, operations need to be performed on the data itself (don't hard code the solution).
        Print to the console the top 10 rows of the data sorted by 'safety' in descending order
        Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
        Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order.  Find these matches using regular expressions.
        Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.  The file path can be a hard-coded location (name it output.txt) or use a dialog box.  
    Your code needs to be able to handle exceptions.  It should handle all data as specified by the data definition document from Lesson 2, and throw some kind of error when it encounters data that doesn't match that format.  To test this, I will add the line 'vlow, vlow, 1, 1, vbig, vhigh' to the .csv file.  Your program should gracefully handle this line in all cases from the previous part.
'''


#load data from csv
f = open('cars.data.csv', 'r')
print(f.read())