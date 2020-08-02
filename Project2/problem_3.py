def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort the list in descending order
    input_list.sort(reverse=True)

    # fill x with digits at the odd indices of sorted list
    x = 0
    for i in range (0, len(input_list), 2):
        x = x * 10 + input_list[i]

    # fill y with digits at the even indices of sorted list
    y = 0
    for i in range (1, len(input_list), 2):
        y = y * 10 + input_list[i]

    return [x, y]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)