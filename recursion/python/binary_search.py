# binary search algorithm

def binary_search(array, target, low=0, high=None):
    """
        Return True if target is found in indicated portion
        of a Python list.
    """

    # if high is not explicitly given, set it to the end of the array.
    if high == None:
        high = len(array) - 1

    if low > high:
        return False  # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == array[mid]:  # found a match
            return True
        elif target < array[mid]:
            return binary_search(array, target, low, mid - 1)
        else:
            return binary_search(array, target, mid + 1, high)


if __name__ == '__main__':
    array = [1, 23, 55, 92, 84]
    print(binary_search(array, 92))
    print(binary_search(array, 32))
