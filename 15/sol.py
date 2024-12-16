
def print_array(arr):
    for row in arr:
        print(''.join(row))

def get_input(fn, p1):
    mp = []
    mvs = []

    with open(fn, 'r') as f:
        parse_map = True
        for i, l in enumerate(f):
            l = l.replace('\n', '')

            if l == '':
                parse_map = False
                continue

            if parse_map:
                if not p1:
                    l = l.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')
                mp.append([c for c in l])
            else:
                mvs += [c for c in l]
       
    print_array(mp)

    return mp, mvs



def solve(mp, mvs, p1):
    def get_char(pos):
        return mp[pos[1]][pos[0]]

    def move(pos, new_pos):
        temp = mp[new_pos[1]][new_pos[0]] 
        mp[new_pos[1]][new_pos[0]] = mp[pos[1]][pos[0]]
        mp[pos[1]][pos[0]] = temp

    def get_new_pos(pos, mv):
        if mv == '<':
            new_pos = [pos[0]-1, pos[1]]
        elif mv == '>':
            new_pos = [pos[0]+1, pos[1]]
        elif mv == 'v':
            new_pos = [pos[0], pos[1]+1]
        elif mv == '^':
            new_pos = [pos[0], pos[1]-1]
        return new_pos


    def can_move(pos, new_pos, mv, p1, do_move):
        char, new_char = get_char(pos), get_char(new_pos)

        if new_char == '.':
            return True
        
        if new_char == '#':
            return False
        
        if new_char == 'O':
            if can_move(new_pos, get_new_pos(new_pos, mv), mv, p1, do_move):
                move(new_pos, get_new_pos(new_pos, mv))
                return True
            
        if new_char in ['[',']']:
            if mv in ['<','>']:
                if can_move(new_pos, get_new_pos(new_pos, mv), mv, p1, do_move):
                    move(new_pos, get_new_pos(new_pos, mv))
                    return True
            
            if mv in ['^', 'v']:
                if new_char == '[':
                    r_pos = [new_pos[0]+1,new_pos[1]]
                    if can_move(new_pos, get_new_pos(new_pos, mv), mv, p1, do_move) and can_move(r_pos, get_new_pos(r_pos, mv), mv, p1, do_move):
                        if do_move:
                            move(new_pos, get_new_pos(new_pos, mv))
                            move(r_pos, get_new_pos(r_pos, mv))
                        return True
                if new_char == ']':
                    l_pos = [new_pos[0]-1,new_pos[1]]
                    if can_move(new_pos, get_new_pos(new_pos, mv), mv, p1, do_move) and can_move(l_pos, get_new_pos(l_pos, mv), mv, p1, do_move):
                        if do_move:
                            move(new_pos, get_new_pos(new_pos, mv))
                            move(l_pos, get_new_pos(l_pos, mv))
                        return True

    
    def curr_pos():
        for i, l in enumerate(mp):
            for j, c in enumerate(l):
                if c == '@':
                    pos = [j, i]
                    return pos

    for i, mv in enumerate(mvs):
        pos = curr_pos()
        new_pos = get_new_pos(pos, mv)

        if can_move(pos, new_pos, mv, p1, do_move=False):
            can_move(pos, new_pos, mv, p1, do_move=True) 
            move(pos, new_pos)

    def calc_gps(mp):
        gps_tot = 0
        for i, l in enumerate(mp):
            for j, c in enumerate(l):
                if c in ['O','[']:
                    gps_tot += ((i*100) + j)
        print(f'gps_tot:{gps_tot}')

    print_array(arr=mp)
    calc_gps(mp)

def main(fn, p1):
    mp, mvs = get_input(fn, p1=p1)
    mvs = mvs[:]
    solve(mp, mvs, p1)

if __name__ == '__main__':
    # main('./test-1.txt', p1=False)
    # main('./test-2.txt', p1=False)
    # main('./test-3.txt', p1=False)
    # main('./input.txt', p1=True)
    main('./input.txt', p1=False)

