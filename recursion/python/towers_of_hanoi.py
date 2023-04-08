# Solving the Towers of Hanoi problem recursively

import sys


class TowersOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.TOWERS = {'A': [], 'B': [], 'C': []}

        self.initialise_towers(num_disks)

    def initialise_towers(self, num_disks):
        # Initialise the towers of hanoi start state with given number of disks
        self.TOWERS['A'] = list(reversed(range(1, num_disks + 1)))

    def print_disk(self, disk_num):
        """
            Print a single disk with diskNum.
        """
        empty_space = ' ' * (self.num_disks - disk_num)

        if disk_num == 0:
            # draw the pole
            sys.stdout.write(empty_space + '||' + empty_space)
        else:
            # draw the disk
            disk_space = '@' * disk_num
            disk_num_label = str(disk_num).rjust(2, '_')
            sys.stdout.write(empty_space + disk_space +
                             disk_num_label + disk_space + empty_space)

    def print_towers(self):
        # Print all three towers.
        for level in range(self.num_disks, -1, -1):
            for tower in (self.TOWERS['A'], self.TOWERS['B'], self.TOWERS['C']):
                if level >= len(tower):
                    self.print_disk(0)
                else:
                    self.print_disk(tower[level])
            sys.stdout.write('\n')
        # Print the tower labels A, B, and C
        empty_space = ' ' * self.num_disks
        print('%s A%s%s B%s%s C\n' %
              (empty_space, empty_space, empty_space, empty_space, empty_space))

    def move_one_disk(self, start_tower, end_tower):
        """
            Move one top disk from start_tower to end_tower
        """
        disk = self.TOWERS[start_tower].pop()
        self.TOWERS[end_tower].append(disk)

    def solve(self, num_disks, start_tower, end_tower, temp_tower):
        """
            Move the top num_disks disks from start_tower to end_tower.
        """
        if num_disks == 1:
            # base case
            self.move_one_disk(start_tower, end_tower)
            self.print_towers()
        else:
            # recursive case
            # move n-1 disks from start tower to temp tower
            self.solve(num_disks - 1, start_tower, temp_tower, end_tower)
            # move disk n from start tower to end tower
            self.move_one_disk(start_tower, end_tower)
            self.print_towers()
            # move n-1 disks from temp tower to end tower
            self.solve(num_disks - 1, temp_tower, end_tower, start_tower)
            return


if __name__ == '__main__':
    toh = TowersOfHanoi(10)
    toh.print_towers()
    toh.solve(10, 'A', 'B', 'C')
