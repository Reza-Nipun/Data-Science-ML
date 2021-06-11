while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')

'''
while True:
    s = input('Enter something or write quit to exit : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
    print('Done')
'''


# x = 1
# sum = 0
# while x < 10:
#     print (x)
#     x+=1
#     sum+=x
    
# print(sum)

#all the print statement must be in parenthesis for version 3.4.0 x = x - 1 
#the algebra need not be done within the parenthesis

# x = 5 
# y = x
# while y > 1: 
#     y = y - 1
#     print (y)
# else:
#     print (x)