from functools import cache

def get_input(fn):
    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            l = l.replace('\n','')
            line = [int(char) for char in l.split(' ')]
    
    return line

def sol(line, blinks):

    @cache
    def blink(num, depth):
        new_nums = []
        if depth == 0:
            return 1
        
        if num == 0:
            return blink(1, depth-1)

        elif len(str(num)) % 2 == 0:
            snum = str(num)
            mid = int(len(snum)/2)
            l, r = int(snum[:mid]), int(snum[mid:])
            new_nums += [l,r]
            return blink(l, depth-1) + blink(r, depth-1)

        else:
            return blink(num * 2024, depth-1)
        
    counter = 0
    for i, num in enumerate(line):
        counter += blink(line[i], depth=blinks)
    
    print(f'blinks={blinks}:', counter)



if __name__ == '__main__':
    line = get_input('./input.txt') 
    # line = get_input('./test.txt')

    sol(line, blinks=25)
    sol(line, blinks=75)