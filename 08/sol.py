def get_input():
    all_coords = {}
    with open("input.txt", 'r') as f:
        for i, line in enumerate(f):
            line = line.replace('\n','')
            grid_max = len(line)

            for j, char in enumerate(line):
                if char != '.':
                    coord = [i, j]
                    if char not in all_coords.keys():
                        all_coords[char] = [coord]
                    else:
                        all_coords[char].append(coord)

    return all_coords, grid_max

def solve(all_coords, grid_max, p1):
    ans = [[[] for _ in range(grid_max)] for _ in range(grid_max)]

    def find_ans(coords, ans, p1):

        for idx1 in range(0, len(coords)-1):
            c1 = coords[idx1]

            for idx2 in range(idx1+1, len(coords)):
                c2 = coords[idx2]
                y_delt = c2[0]-c1[0]
                x_delt = c2[1]-c1[1]

                if p1:

                    an1 = [c1[0] - y_delt, c1[1] - x_delt]
                    an2 = [c2[0] + y_delt, c2[1] + x_delt]

                    if min(an1) >= 0 and max(an1) < grid_max:
                        ans[an1[0]][an1[1]] = True

                    if min(an2) >= 0 and max(an2) < grid_max:
                        ans[an2[0]][an2[1]] = True

                else:

                    def extrapolate(pos, y_delt, x_delt, back):
                        an = pos

                        while True:
                            if min(an) >= 0 and max(an) < grid_max:
                                ans[an[0]][an[1]] = True 
                            else:
                                return

                            if back:
                                an = [an[0] - y_delt, an[1] - x_delt]
            
                            else:
                                an = [an[0] + y_delt, an[1] + x_delt]
                        
                    extrapolate(c1, y_delt, x_delt, back=True)
                    extrapolate(c2, y_delt, x_delt, back=False)

        return ans

                
    for char, coords in all_coords.items():
        ans = find_ans(coords=coords, ans=ans, p1=p1)

    count = 0
        
    for line in ans:
        l = ''
        for place in line:
            if place:
                count += 1
                l += '#'
            else:
                l += '.'
        print(l)
        
    print('count:', count)

if __name__ == '__main__':
    all_coords, grid_max = get_input()

    solve(all_coords=all_coords, grid_max=grid_max, p1=True)
    solve(all_coords=all_coords, grid_max=grid_max, p1=False)