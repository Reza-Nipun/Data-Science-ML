# Search method
def search(list, n, x):
    for i in range(0, n):
        if (list[i] == x):
            return i
    return -1

# Input List
list = [2, 3, 4, 10, 40]

# Need to find out x from the inputted list
x = 10

# Length of the list
n = len(list)

result = search(list, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)