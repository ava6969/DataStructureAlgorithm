def binary_search(array, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search(array, start_index, mid_index - 1,target)
    else:
        return binary_search(array, mid_index + 1, end_index, target)


def rotated_array_search(input_list, number):
    def findPivot(arr, low, high):
        # base cases
        if high < low:
            return -1
        if high == low:
            return low

            # low + (high - low)/2;
        mid = (low + high) // 2

        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return (mid - 1)
        if arr[low] >= arr[mid]:
            return findPivot(arr, low, mid - 1)
        return findPivot(arr, mid + 1, high)

    n = len(input_list)
    pivot = findPivot(input_list, 0, n - 1)

    if pivot == -1:
        return binary_search(input_list, 0, n - 1, number)

    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)
    return binary_search(input_list, pivot + 1, n - 1, number)


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