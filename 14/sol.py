
def get_input(fn):
    rbts = []

    def add_rbt(l):
        l = l.replace('\n','')
        p, v = l.split(' ')
        pos, vec = p[2:].split(','), v[2:].split(',')
        pos = [int(p) for p in pos]
        vec = [int(v) for v in vec]
        rbts.append([pos,vec])

    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            add_rbt(l)
    
    return rbts


def solve(rbts, t, render):
    maxx = 101
    maxy = 103

    def find_pos(rbt, t):
        pos, vel = rbt
        tx, ty = pos[0] + (vel[0]*t), pos[1] + (vel[1]*t)
        
        def new(tz, maxz):
            if tz < 0:
                if abs(tz)%maxz == 0:
                    return 0
                else:
                    return maxz - (abs(tz)%maxz) 
            else:
                if (tz+1)%maxz == 0:
                    return maxz-1
                else:
                    return ((tz+1) % maxz)-1
            
        new_pos = [new(tx, maxx), new(ty, maxy)]
        return new_pos
    
    poss = []
    for rbt in rbts:
        pos = find_pos(rbt, t)
        poss.append(pos)

    def calc_quads(poss):
        midx, midy = (maxx-1)/2, (maxy-1)/2
        quads = [0, 0, 0, 0]
        for p in poss:
            if p[0] < midx and p[1] < midy:
                quads[0]+=1
            if p[0] < midx and p[1] > midy:
                quads[1]+=1
            if p[0] > midx and p[1] < midy:
                quads[2]+=1
            if p[0] > midx and p[1] > midy:
                quads[3]+=1
        sf = quads[0] * quads[1] * quads[2] * quads[3]
        return sf
    
    def render_image(poss):
        for j in range(maxy):
            l = ''
            for i in range(maxx):
                if [i, j] in poss:
                    l += str(poss.count([i,j]))
                else: 
                    l += '.'
            print(l)
        print('-'*45 + f't={t}' + '-'*45)

    sf = calc_quads(poss)
    print(f't={t} | safety_factor={sf}')
    if render:
        render_image(poss)
    return poss, sf


if __name__ == '__main__':
    rbts = get_input('./input.txt')
    solve(rbts, t=100, render=False)

    min_score = [0, solve(rbts, t=0, render=False)[1]]
    for t in range(1, 10**4, 1):
        score = solve(rbts, t=t, render=False)[1]
        if score < min_score[1]:
            min_score = [t, score]

    solve(rbts, t=min_score[0], render=True)
