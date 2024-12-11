import copy

def get_map(fn):
    wmap = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            wmap.append(list(line.replace('\n', '')))
    return wmap


            # # Calculate possible loops
            # if wmap[ny][nx] == nextd[d]:
            #     loops += 1 
            # else:
            #     if d == 'w':
            #         pot_path = [row[nx] for row in wmap[ny-1::-1]]
            #     if d == 'e':
            #         pot_path = [row[nx] for row in wmap[ny+1::]]
            #     if d == 'n':
            #         pot_path = wmap[ny][nx+1::]
            #     if d == 's':
            #         pot_path = wmap[ny][nx-1::-1]
            #     if nextd[d] in pot_path:
            #         if ny == starty and nx == startx:
            #             pass
            #         else:
            #             loops += 1

def solve(wmap):
    original_wmap = copy.deepcopy(wmap)
    
    # find starting pos
    startd = 'n'
    for i, row in enumerate(wmap):
        for j, char in enumerate(row):
            if char == '^':
                x, y = j, i
                startx, starty = x, y
                wmap[y][x] = '^'

    nextd = {
        'n':'e',
        'e':'s',
        's':'w',
        'w':'n'
    }


    loops = 0
    moves = 0 

    # def process_route(startx, starty, startd)

    # move_hist = [[startx, starty, startd]]

    # 1. Process route as normal
    # 2. At each step:
    #   - What would happen if directly ahead was a new #?
    #           Exceptions being:
    #               - It can't be the starting point
    #               - It can't be a point in path history (as then it'd block being here in the first place)
    #   - Work out remaining route given this condition
    #   - If I go off the map then it's invalid
    #   - If any point along that way the nx, ny, nd are IN the history of that path THEN +1


    def move(wmap, mv):
        # Check next pos
        nx, ny, d = mv[0], mv[1], mv[2]
        if d == 'n':
            ny -= 1
        if d == 'e':
            nx += 1
        if d == 's':
            ny += 1
        if d == 'w':
            nx -= 1

        if nx < 0 or nx == len(wmap[0]) or ny < 0 or ny == len(wmap):
            return False

        if wmap[ny][nx] == '#':
            d = nextd[d]
            nx, ny = mv[0], mv[1]

        return [nx, ny, d]
    

    def process_path(wmap, startx, starty, startd, move_hist):

        mv = [startx, starty, startd]

        while True:
            mv = move(wmap, mv)
            if mv == False:
                break
            else:
                # print(move_hist, mv)
                if mv in move_hist:
                    # print('a', mv, move_hist)
                    return wmap, move_hist, True
                move_hist.append(mv)
                wmap[mv[1]][mv[0]] = 'X'

        return wmap, move_hist, False


    # part 1
    part_1, move_hist, looping = process_path(wmap, startx, starty, startd, move_hist=[[startx, starty, startd]])
    # print(looping)
    s = 0
    for row in part_1:
        s += row.count('X') + row.count('^')
        print(''.join(row))
    
    
    print('sum:', s)

    # part 2
    def num_loops(wmap, move_hist, startx, starty):
        move_hist_xsys = []

        loop_counter = 0

        for i, move in enumerate(move_hist):
            print(f'[{i}/{len(move_hist)}] = {move}')

            # Check next pos
            nx, ny, d = move[0], move[1], move[2]
            move_hist_xsys.append([move[0], move[1]])
            if d == 'n':
                ny -= 1
            if d == 'e':
                nx += 1
            if d == 's':
                ny += 1
            if d == 'w':
                nx -= 1

            if nx < 0 or nx == len(wmap[0]) or ny < 0 or ny == len(wmap):
                continue

            if wmap[ny][nx] == '#':
                continue
            
            if nx == startx and ny == starty:
                continue

            if [nx, ny] in move_hist_xsys:
                continue

            # possible_locations.append([nx, ny])
            
            nwmap = copy.deepcopy(original_wmap)
            # Implement location change to test
            # print('move', move, 'new-ob', ny, nx)
            nwmap[ny][nx] = '#'
       
            new_move_hist = move_hist[:i]
            # print(new_move_hist)

            pathed_map, temp_move_hist, looping = process_path(nwmap, move[0], move[1], move[2], move_hist=new_move_hist)
            if looping:
                # for row in nwmap:
                #     print(''.join(row))
                # for row in pathed_map:
                #     print(''.join(row))
                loop_counter += 1
                # exit()

        return loop_counter
        # Remove dupes
        # possible_locations = [list(x) for x in set(tuple(x) for x in possible_locations)]

        # return possible_locations


    loops = num_loops(wmap, move_hist, startx, starty)
    print(loops)
    exit()

    nwmap = copy.deepcopy(wmap)
    for i, loc in enumerate(possible_locs):

        print(f'[{i+1}/{len(possible_locs)}]')

        # Implement location change to test
        nwmap[loc[1]][loc[0]] = '#'
        if process_path(nwmap, startx, starty, startd, loop=True):
            loop_counter += 1

        # Reverse the change for the next one
        nwmap[loc[1]][loc[0]] = '.'

    print('loops:', loop_counter)

if __name__ == '__main__':
    wmap = get_map(fn='map.txt')
    # wmap = get_map(fn='test.txt')
    solve(wmap)