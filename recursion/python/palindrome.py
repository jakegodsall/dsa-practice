# checks if string is a palindrome

def is_palindrome_iterative(string):
    reversed = ''

    for c in string:
        reversed = c + reversed

    return string == reversed


def is_palindrome_recursive(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        head = string[0]
        middle = string[1:-1]
        tail = string[-1]

        return head == tail and is_palindrome_recursive(middle)


if __name__ == '__main__':
    print(is_palindrome_iterative('racecar'))
    print(is_palindrome_iterative('hello'))

    print(is_palindrome_recursive('racecar'))
    print(is_palindrome_recursive('hello'))
