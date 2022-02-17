def binarySearch(array, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2   # getting mid value

        if array[mid] == x:
            return mid  #   the cursor result
        elif array[mid] < x:
            low = mid + 1   # Reset the value of `low`
        else:
            high = mid - 1  # Reset the value of `high`
    return -1   # Not Exist


array = [10, 20, 30, 40, 50, 60]    # Inputted List
x = 70  # Expected Output
low = 0  # Lowest Index
high = len(array) - 1  # Highest Index

# Binary Searching the value
result = binarySearch(array, low, high, x)

# Decision making on result
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Element is not present in this list!")