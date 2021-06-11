'''
fruitList = ["apple", "apricot", "banana", "coconut", "lemen", "plum", "pear"]
for fruit in fruitList :
    print ("Fruit: ", fruit)
'''
'''
fruitList = ["apple", "apricot", "banana", "coconut", "lemen", "plum", "pear"]
print ( fruitList )
# Element count.
print ("Element count: ", len(fruitList) )
for i in range (0, len(fruitList) ) :
    print ("Element at ", i, "= ", fruitList[i] )
# A sub list of elements with index from 1 to 4 (1, 2, 3)
subList = fruitList[1: 4]
# ['apricot', 'banana', 'coconut']
print ("Sub List [1:4] ", subList )
'''

'''
fruitList = ["apple", "apricot", "banana", "coconut", "lemen", "plum", "pear"]
print ( fruitList )
print ("Element count: ", len(fruitList) )
print ("fruitList[-1]: ", fruitList[-1])
print ("fruitList[-2]: ", fruitList[-2])
subList1 = fruitList[-4: ]
print ("\n")
print ("Sub List fruitList[-4: ] ")
print (subList1)
subList2 = fruitList[-4:-2]
print ("\n")
print ("Sub List fruitList[-4:-2] ")
print (subList2)
'''

'''
years = [1991,1995, 1992]
print ("Years: ", years)
print ("Set years[1] = 2000")
years[1] = 2000

print ("Years: ", years)
print ( years )
print ("Append element 2015, 2016 to list")
# Append an element to the end of the list.
years.append( 2015 )
years.append( 2016 )
print ("Years: ", years)
'''

'''
years = [ 1990 , 1991 , 1992 , 1993 , 1994 , 1995 , 1996 ]
print ("Years: ", years)
print ("Update Slice: years[1:5] = [2000, 2001]")
years[1:5] = [ 2000 , 2001 ]
print ("Years: ", years)
years.remove(1996)
print ("Years: ", years)
'''

# User defined values appending to List

years = []
while True:
    year = input('Enter Year : ')
    years.append(year)
    print(years)
    continue

'''Home Work Start

----------Main Menu-----------
1.Add data
2.Display data
3.search data
4.Update data
5.Delete data
6.Exit
----------------------
Enter choice:

Home Work End'''


