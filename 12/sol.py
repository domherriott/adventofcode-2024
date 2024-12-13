from functools import cache

def get_input(fn):
    plants = []
    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            l = l.replace('\n','')
            print(l)
            plants.append([c for c in l])
    
    # print(plants)
    return plants


def sol(plants):

    def perim_of_sq(length):
        return length * 4
    
    searched = [[False for _ in range(0, len(plants))] for _ in range(0, len(plants[0]))]
    # print(searched)

    def find_nns(row, col, sides):

        max_row = len(plants)-1
        max_col = len(plants[0])-1
        nns = []

        if row > 0: 
            nns.append([row-1, col])

        if row < max_row:
            nns.append([row+1, col])

        if col > 0:
            nns.append([row, col-1])

        if col < max_col:
            nns.append([row, col+1]) 


        if row == 0:
            sides['hori'][row][col] = 'above'
        if row == max_row:
            sides['hori'][row+1][col] = 'below'
        if col == 0:
            sides['vert'][col][row] = 'left'
        if col == max_col:
            sides['vert'][col+1][row] = 'right'

        matching_nns = []
        # print(row, col, nns)
        for nn in nns:
            if plants[nn[0]][nn[1]] == plants[row][col]:
                matching_nns.append(nn)
            elif nn[0] == row:
                if nn[1] < col: #left
                    sides['vert'][col][row] = 'left'
                else: #right
                    sides['vert'][col+1][row] = 'right'
            elif nn[1] == col:
                # print('a')
                if nn[0] < row: #above
                    sides['hori'][row][col] = 'above'
                else: #below
                    sides['hori'][row+1][col] = 'below'


        # print(sides)
        # exit()
        return matching_nns, sides
            
                    
    # def find_corners(row,col, nns):
    #     corners = []
    #     print(nns)
    #     for i in range(0, len(nns)):
    #         nn1, nn2 = nns[i-1], nns[i]
    #         if nn1[0] == nn2[0] or nn1[1] == nn2[1]:
    #             pass
    #         else:
    #             check_row = nn2[0] if nn1[0] == row else nn1[0]
    #             check_col = nn2[1] if nn1[1] == col else nn1[1]
    #             if plants[check_row][check_col] == plants[row][col]:
    #                 corner_id = (min(check_row, row), min(check_col, col))
    #                 corners.append(corner_id)

    #     return corners
                

    def search(row, col, sides):

        searched[row][col] = True

        nns, sides = find_nns(row, col, sides)

        perim = 4
        area = 1
        # corners = find_corners(row, col, nns)
        # print(corners)
        # exit()

        for nn in nns:
            nnrow, nncol = nn[0], nn[1]
            perim -= 1
            if not searched[nnrow][nncol]:
                nna, nnp, sides = search(nnrow, nncol, sides)
                area += nna
                perim += nnp
    
        return area, perim, sides
         
        
    tracker = []

    def process_sides(sides):
        num_sides = 0
        def count(lis):
            prev = False
            counter = 0
            for row in lis:
                for char in row:
                    if char:
                        if char != prev:
                            counter += 1
                            prev = char
                        else:
                            prev = char 
                    else:
                        prev = char
            return counter
        
        # print(sides)
        num_sides += count(sides['hori'])
        num_sides += count(sides['vert'])
        # exit()
        return num_sides


    for i in range(0, len(plants)):
        for j in range(0, len(plants[0])):
            
            if isinstance(plants[i][j], str):
                # print(plants[i][j])
                if not searched[i][j]:
                    sides = {
                        'hori':[[False for _ in range(0, len(plants)+1)] for _ in range(0, len(plants[0])+1)],
                        'vert':[[False for _ in range(0, len(plants)+1)] for _ in range(0, len(plants[0])+1)]
                    }
                    area, perim, sides = search(i, j, sides)
                    num_sides = process_sides(sides)
                    # unique_corners = list(set(corners))
                    # print(plants[i][j], num_sides)
                    # exit()
                    # exit()
                    tracker.append([plants[i][j], perim, area, num_sides])
    
    print(tracker)
    p1cost, p2cost = 0, 0
    for area in tracker:
        p1cost += area[1] * area[2]
        p2cost += area[2] * area[3]
    print('part 1 cost:', p1cost)
    print('part 2 cost:', p2cost )
    # def 

    # max_width, max_height = 0, 0

    # perimeter = 




if __name__ == '__main__':
    # plants = get_input('./input.txt') 
    plants = get_input('./test-1.txt')
    sol(plants)

    plants = get_input('./test-2.txt')
    sol(plants)

    plants = get_input('./test-3.txt')
    sol(plants)

    plants = get_input('./test-4.txt')
    sol(plants)

    plants = get_input('./input.txt')
    sol(plants)
    # sol(plants)