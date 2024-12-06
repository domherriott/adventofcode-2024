import re

def get_input():
    inp = ''

    with open("input.txt", 'r') as f:
        for line in f.readlines():
            inp += line
    return inp

def part_1(inp):
    valid = []
    calc = 0

    regex = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(regex, string=inp)

    for match in matches:
        int1, int2 = match[4:-1].split(',')
        int1, int2 = int(int1), int(int2)
        valid.append([int1, int2])

        calc += (int1 * int2)

    print('calc:', calc)
    return valid

def part_2(inp):

    do = True
    calc = 0

    regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.compile(regex)

    for m in matches.finditer(string=inp):
        if m.group() == 'do()':
            do = True
        elif m.group() == "don't()":
            do = False
        else:
            if do:
                int1, int2 = m.group()[4:-1].split(',')
                int1, int2 = int(int1), int(int2) 
                calc += (int1 * int2)

    
    print('calc:', calc)
    return None

if __name__ == '__main__':
    inp = get_input()
    valid = part_1(inp=inp)
    part_2(inp=inp)
