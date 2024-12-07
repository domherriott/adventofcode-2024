import copy

def get_map():
    wmap = []

    with open("map.txt", 'r') as f:

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


    def process_path(wmap, startx, starty, startd, loop):

        x, y, d = startx, starty, startd
        move_hist = []

        while True:

            move_hist.append([x, y, d])
            # Check next pos
            nx, ny = x, y
            if d == 'n':
                ny -= 1
            if d == 'e':
                nx += 1
            if d == 's':
                ny += 1
            if d == 'w':
                nx -= 1

            if nx < 0 or nx == len(wmap[0]) or ny < 0 or ny == len(wmap):
                break

            if wmap[ny][nx] == '#':
                d = nextd[d]
                continue

            if loop:
                if [nx, ny, d] in move_hist:
                    # print(move_hist)
                    return True

            # apply new move
            x, y = nx, ny
            wmap[y][x] = 1

        if not loop:
            return wmap, move_hist
        else:
            return False


    # part 1
    part_1, move_hist = process_path(wmap, startx, starty, startd, loop=False)
    s = 0
    for row in part_1:
        s += row.count(1) + row.count('^')
    
    print('sum:', s)

    # part 2
    def possible_locations_for_obstacle(wmap, move_hist, startx, starty):
        possible_locations = []
        move_hist_xsys = []
        for move in move_hist:

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

            possible_locations.append([nx, ny])

        # Remove dupes
        possible_locations = [list(x) for x in set(tuple(x) for x in possible_locations)]

        return possible_locations

    loop_counter = 0

    locs = possible_locations_for_obstacle(wmap, move_hist, startx, starty)
    print(len(locs))

    nwmap = copy.deepcopy(wmap)
    for i, loc in enumerate(locs):

        print(f'[{i+1}/{len(locs)}]')

        # Implement location change to test
        nwmap[loc[1]][loc[0]] = '#'
        if process_path(nwmap, startx, starty, startd, loop=True):
            loop_counter += 1

        # Reverse the change for the next one
        nwmap[loc[1]][loc[0]] = '.'

    print('loops:', loop_counter)

if __name__ == '__main__':
    wmap = get_map()
    solve(wmap)