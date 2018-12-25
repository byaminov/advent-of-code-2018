from day16 import run_opcode


def solve1(text: str):
    lines = text.split('\n')
    ip_register = int(lines[0].split(' ')[1])
    instructions = []
    for line in lines[1:]:
        if not line:
            continue
        opcode, a, b, c = line.split(' ')
        a, b, c = int(a), int(b), int(c)
        instructions.append((opcode, a, b, c))

    rs = [0] * 6
    ip_value = rs[ip_register]
    iteration = 0

    while True:
        if ip_value < 0 or ip_value >= len(instructions):
            break
        iteration += 1

        rs[ip_register] = ip_value
        opcode, a, b, c = instructions[ip_value]
        rs = run_opcode(opcode, a, b, c, rs)

        # print(f'iteration={iteration}, ip={ip_value:2d}, rs[0]={rs[0]}, rs={rs}')

        ip_value = rs[ip_register]
        ip_value += 1

    return rs[0]


def solve2(number: int):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    return result + number
