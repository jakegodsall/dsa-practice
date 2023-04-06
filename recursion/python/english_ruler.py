# draw an English ruler recursively.

def draw_line(length, label=''):
    """
        Draws a tick line with optional label.
    """
    line = '-' * length
    if label:
        line += ' ' + label
    print(line)


def draw_interval(length):
    """
        Draws tick interval based on centre length
    """
    if length > 0:
        draw_interval(length - 1)
        draw_line(length)
        draw_interval(length - 1)


def draw_ruler(num_inches, major_length):
    """
        Draws English ruler with given number of inches,
        major tick length
    """
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    draw_ruler(3, 3)
