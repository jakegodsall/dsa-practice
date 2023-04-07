# sum the digits of a positive integer using recursion

def sum_digits(num):

    assert num >= 0 and int(
        num) == num, 'The number has to be a positive integer'

    div, mod = divmod(num, 10)

    if div == 0:
        return num
    else:
        return (mod) + sum_digits(div)


if __name__ == '__main__':
    print(sum_digits(-1235))
