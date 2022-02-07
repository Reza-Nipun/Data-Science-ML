def solution(A):
    # String to list conversion
    chars_list = list(A)

    # initialize counter of odd elements
    counter = 0
    # initialize a null list
    unique_list = []

    # Preparing the list of the unique elements
    for x in chars_list:
        if x not in unique_list:
            unique_list.append(x)

    # Counting the odd number of elements
    for y in unique_list:
        if y in chars_list:
            if (chars_list.count(y) % 2) != 0:
                counter += 1
    return counter

A='aaaa'
print(solution(A))