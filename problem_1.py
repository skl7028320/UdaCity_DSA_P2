def sqrt_naive(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1

    i = 1
    while i ** 2 <= number:
        i += 1

    return i - 1


print("Test naive approach:")
print ("Pass" if  (3 == sqrt_naive(9)) else "Fail")
print ("Pass" if  (0 == sqrt_naive(0)) else "Fail")
print ("Pass" if  (4 == sqrt_naive(16)) else "Fail")
print ("Pass" if  (1 == sqrt_naive(1)) else "Fail")
print ("Pass" if  (5 == sqrt_naive(27)) else "Fail")


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1

    lower_bound = 0
    upper_bound = number

    while lower_bound < upper_bound:
        mid = (upper_bound + lower_bound) // 2
        if mid ** 2 <= number < (mid + 1) ** 2:
            return mid
        elif mid ** 2 > number:
            upper_bound = mid
        elif (mid + 1) ** 2 <= number:
            lower_bound = mid

    return None


print("\nTest binary search approach:")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
