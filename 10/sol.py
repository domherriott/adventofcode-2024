def get_input(fn):
    top = []
    with open(fn, 'r') as f:
        for i, line in enumerate(f):
            line = line.replace('\n','')
            top.append([int(char) for char in line])
    
    print(top)
    return top

def sol(top):
    def thds(top):
        thds = []
        for i, line in enumerate(top):
            for j, char in enumerate(line):
                if char == 0:
                    thds.append([i,j])
        return thds

    thds = thds(top)
    print(thds)

    def score(thd):
        peaks = []
        def route(top, pos):
            i, j = pos[0], pos[1]
            height = top[i][j]
            
            if top[i][j] == 9:
                peaks.append([i,j])

            options = []
            if i > 0:
                options.append([i-1, j])
            if i < (len(top)-1):
                options.append([i+1, j])
            if j > 0:
                options.append([i, j-1])
            if j < (len(top[0])-1):
                options.append([i, j+1])

            print('options:',options)

            for option in options:
                if height + 1 == top[option[0]][option[1]]:
                    route(top, option)

        route(top, thd)
        uni_peaks = [list(p) for p in set(tuple(p) for p in peaks)]
        return len(uni_peaks), len(peaks)
    
    total_score, total_rating = 0, 0
    for thd in thds:
        s, r = score(thd)
        total_score += s
        total_rating += r

    print('total_score:', total_score)
    print('total_rating:', total_rating)

if __name__ == '__main__':
    top = get_input('./input.txt')
    # top = get_input('./test.txt')
    sol(top)