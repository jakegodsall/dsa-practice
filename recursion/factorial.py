def factorial_iterative(n):
    val = 1
    for i in range(1, n + 1):
        val *= i

    return val


def factorial_recursive(n):
    if n == 0:
        # recursive case
        return 1
    else:
        # factorial case
        return factorial_recursive(n - 1) * n


if __name__ == '__main__':
    print(factorial_iterative(5))
    print(factorial_recursive(5))
