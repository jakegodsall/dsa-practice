# calculate the power of a number recursively


def power_of(base, exponent):

    assert int(exponent) == exponent, 'The exponent must be an integer number'

    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / base * power_of(base, exponent + 1)
    else:
        return base * power_of(base, exponent - 1)


if __name__ == '__main__':
    for i in range(-5, 5):
        print(f'2**{i} = {power_of(2, i)}')
