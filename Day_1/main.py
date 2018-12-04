#!/usr/local/bin/env python3

import time

file = [line for line in open('input.txt')]

def part_1():
    return sum(map(int, file))

def part_2():
    pass


def main():
    time_start = time.time()
    p1 = part_1()
    p2 = part_2()

    print("Answer: {0} => Calculated in: {1}".format(p1, (time.time() - time_start)))
    print("Answer: {0} => Calculated in: {1}".format(p2, (time.time() - time_start)))

if __name__ == '__main__':
    main()
