def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    left_list = input_list[:pivot + 1]
    right_list = input_list[pivot + 1:]

    if number <= right_list[-1]:
        #return binary_search(right_list, number) + pivot + 1
        return binary_search_recursive(right_list, number, 0, len(right_list) - 1) + pivot + 1
    elif number >= left_list[0]:
        #return binary_search(left_list, number)
        return binary_search_recursive(left_list, number, 0, len(left_list) - 1)


def find_pivot(input_list, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2

    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid

    if mid > low and input_list[mid] < input_list[mid - 1]:
        return mid - 1

    if input_list[low] >= input_list[mid]:
        return find_pivot(input_list, low, mid)

    if input_list[mid] >= input_list[high]:
        return find_pivot(input_list, mid, high)


def binary_search(input_list, number):
    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if number == input_list[mid]:
            return mid
        if number < input_list[mid]:
            end = mid - 1
        if number > input_list[mid]:
            start = mid + 1

    return -1


def binary_search_recursive(input_list, number, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if number == input_list[mid]:
        return mid
    if number < input_list[mid]:
        return binary_search_recursive(input_list, number, start, mid - 1)
    if number > input_list[mid]:
        return binary_search_recursive(input_list, number, mid + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Extreme case with empty input list
test_function([[], -1])
# Extreme case with two-element input list
test_function([[2, 1], 1])
