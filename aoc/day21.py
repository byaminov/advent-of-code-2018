from cycle_detector import CycleDetector


def solve1():
    a, b, c, d = 0, 0, 0, 0

    iteration = 0
    b = a | 65536
    a = 8725355
    while True:
        d = b & 255
        a = a + d
        a &= 16777215
        a *= 65899
        a &= 16777215
        if 256 > b:
            return a

        else:
            d = b // 256
            b = d

        iteration += 1


def solve2():
    cd = CycleDetector()

    a, b, c, d = 0, 0, 0, 0
    iteration = 0
    b = a | 65536
    a = 8725355
    while True:
        d = b & 255
        a = a + d
        a &= 16777215
        a *= 65899
        a &= 16777215
        if 256 > b:
            if cd.next_and_check(a):
                # cycle is detected, the last element in the cycle
                # is the X that would give the most iterations
                return cd.cycle_[-1]

            b = a | 65536
            a = 8725355
            continue

        else:
            d = b // 256
            b = d

        iteration += 1
        # if iteration % 1000 == 0:
        #     print('at iteration', iteration)
