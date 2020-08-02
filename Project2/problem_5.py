import random
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_ = -float('inf')
    min_ = float('inf')

    for num in ints:
        if num > max_:
            max_ = num
        if num < min_:
            min_ = num
    return (min_, max_)


## Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 2)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 1) == get_min_max(l)) else "Fail")

l = [i for i in range(10, 1000)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((10, 999) == get_min_max(l)) else "Fail")