def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        head = arr[0]
        tail = arr[1:]
        return head + sum_array(tail)


if __name__ == '__main__':
    print(sum_array([1, 2, 3, 4, 5]))
