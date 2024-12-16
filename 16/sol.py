import sys
sys.setrecursionlimit(2000)

def print_array(arr):
    for row in arr:
        print(''.join(row))

def get_input(fn):
    G = []

    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            l = l.replace('\n', '')
            G.append([c for c in l])
            if 'S' in l:
                S = [l.find('S'), i]
            if 'E' in l:
                E = [l.find('E'), i]
       
    print_array(G)
    print('start:',S)
    print('end:',E)

    return G, S

nextd = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^',
}


counter = 0 
def solve(G, S):
    def options(G, pos):
        options = []

        x, y, d = pos

        nd = d
        rot = ''
        while True:
            if nd == '^':
                ox, oy = x, y-1
            elif nd == '>':
                ox, oy = x+1, y
            elif nd == 'v':
                ox, oy = x, y+1
            elif nd == '<':
                ox, oy = x-1, y

            if G[oy][ox] != '#':
                options.append([ox, oy, nd, rot])
            
            if nextd[nd] == d:
                return options
            else:
                nd = nextd[nd]
                rot = (rot + 'c').replace('ccc','a')

    scores = []
    been = {}

    pos = (S[0], S[1], '>')


    def route(pos, score, moves, locs, p2):

        while True:
            global counter
            counter += 1
            
            x, y, d = pos

            if G[y][x] == 'E':
                scores.append([score, moves, locs])
                return True
            
            if p2==0: #part1
                if pos in been and score >= been[pos]:
                    return False
            else: # part 2
                if pos in been and score > been[pos]:
                    return False
                if score > p2:
                    return False
            
            been[pos] = score
            G[y][x] = '%'

            ops = options(G, pos)

            if counter > 1 and len(ops)==1:
                return False
            else:
                # recursion for other options
                op0 = ops[0]
                for op in ops[1:]:
                    nx, ny, nd, rot = op
                    new_pos = (nx, ny, nd)
                    new_score = score + 1+(len(rot)*1000)
                    if p2 == 0:
                        route(pos=new_pos, score=new_score, moves=moves+nd, locs=locs, p2=p2)
                    else:
                        route(pos=new_pos, score=new_score, moves=moves+nd, locs=locs+[(nx,ny)], p2=p2)
                
                # loop through for option 0
                nx, ny, nd, rot = op0
                new_pos = (nx, ny, nd)
                pos = new_pos
                score = score + 1+(len(rot)*1000)
                if p2 != 0:
                    locs.append((nx,ny))

    print('part 1')
    global counter
    counter = 0
    route(pos, score=0, moves='', locs=[], p2=0)

    print('counter:', counter)
    
    min_score = min([s[0] for s in scores])
    print('min_score:',min_score)

    print('part 2')
    counter = 0
    route(pos, score=0, moves='', locs=[(pos[0],pos[1])], p2=min_score)

    li_best_seats = []
    for s in scores:
        if s[0] == min_score:
            li_best_seats += s[2]
    
    num_best_seats = len(list(set(li_best_seats))) 

    print('num_best_seats:', num_best_seats)

def main(fn):
    G, S = get_input(fn)
    solve(G, S)

if __name__ == '__main__':
    main('./test-1.txt')
    main('./test-2.txt')
    main('./input.txt')

