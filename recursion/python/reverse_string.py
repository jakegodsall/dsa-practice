# reverse values in a string

def reverse_string_iterative(string):
    reversed = ''

    for c in string:
        reversed = c + reversed

    return reversed


def reverse_string_recursive(string):
    if len(string) == 0 or len(string) == 1:
        return string
    else:
        head = string[0]
        tail = string[1:]

        return reverse_string_recursive(tail) + head


if __name__ == '__main__':
    print(reverse_string_iterative('hello'))
    print(reverse_string_recursive('hello'))
