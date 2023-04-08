# function which calculates the space taken by all files and directories within a given directory.

import os


def disk_usage(path):
    """
        Return the number of bytes used by a file/folder and any descendents.
    """
    total = os.path.getsize(path)  # account for direct usage
    if os.path.isdir(path):  # if this is a directory
        for filename in os.listdir(path):  # then for each child
            # compose full path to child
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)

    print('{0:<7}'.format(total), path)
    return total


if __name__ == '__main__':
    disk_usage('./')
