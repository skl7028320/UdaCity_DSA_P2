import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None

    min_value = ints[0]
    max_value = ints[0]

    for element in ints[1:]:
        if element < min_value:
            min_value = element
        if element > max_value:
            max_value = element

    return min_value, max_value


# Test case 1
test_list = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_list)

print("Pass" if ((0, 9) == get_min_max(test_list)) else "Fail")

# Test case 2
test_list = [0 for i in range(0, 10)]

print("Pass" if ((0, 0) == get_min_max(test_list)) else "Fail")

# Test case 3
test_list = []

print("Pass" if ((None, None) == get_min_max(test_list)) else "Fail")
