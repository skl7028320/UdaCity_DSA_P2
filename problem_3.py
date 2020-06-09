def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []

    input_list = merge_sort(input_list)

    number_1 = 0
    number_2 = 0

    for i, element in enumerate(input_list):
        if i % 2 == 0:
            number_1 = number_1 * 10 + element
        else:
            number_2 = number_2 * 10 + element

    return [number_1, number_2]


def merge_sort(input_list):
    # Base case
    if len(input_list) <= 1:
        return input_list

    # Find mid point
    mid = len(input_list) // 2

    # Divide input list into to two sub-lists
    left_list = input_list[:mid]
    right_list = input_list[mid:]

    # Run merge sort on two sub-lists
    left_result = merge_sort(left_list)
    right_result = merge_sort(right_list)

    return merge(left_result, right_result)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)
test_case_2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_2)
test_case_3 = [[], []]
test_function(test_case_3)
test_case_4 = [[1, 1, 1, 1, 1, 1], [111, 111]]
test_function(test_case_4)
