# concatenate elements in an array of strings

def concat_array_iterative(arr):
    string = ''

    for i in arr:
        string += i

    return string


def concat_array_recursive(arr):
    if len(arr) == 0:
        return ''
    else:
        head = arr[0]
        tail = arr[1:]
        return head + concat_array_recursive(tail)


if __name__ == '__main__':
    print(concat_array_iterative(['this', 'is', 'a', 'test']))
    print(concat_array_recursive(['this', 'is', 'a', 'test']))
