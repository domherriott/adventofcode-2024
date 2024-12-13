
def get_input(fn):
    prizes = [{}]
    prize_num = 0

    def add_butts(l, but):
        ax, ay = l[10:].split(', ')
        ax, ay = int(ax[2:]), int(ay[2:])
        prizes[-1][but] = [ax, ay]

    with open(fn, 'r') as f:
        for i, l in enumerate(f):
            l = l.replace('\n','')
            if l == '':
                prize_num += 1
                prizes.append({})
            elif 'Button A' in l:
                add_butts(l, 'A')
            elif 'Button B' in l:
                add_butts(l, 'B')
            else:
                px, py = l[7:].split(', ')
                px, py = int(px[2:]), int(py[2:])
                prizes[-1]['P'] = [px, py]
    
    return prizes

def solve(prizes, p2):
    total_cost = 0

    for p in prizes:
        P = [p + 10000000000000 for p in p['P']] if p2 else p['P']
        A, B = p['A'], p['B']
        a = ((P[0] * B[1]) - (P[1] * B[0])) / ((A[0]*B[1])-(A[1]*B[0]))
        b = (P[0] - (a * A[0]))/B[0]
        if a.is_integer() and b.is_integer():
            total_cost += (3*a +b)

    print(f'total cost, p2={p2} | {int(total_cost)}')

def sol(prizes):
    solve(prizes, p2=False)
    solve(prizes, p2=True)

if __name__ == '__main__':
    prizes = get_input('./test-1.txt')
    sol(prizes)

    prizes = get_input('./input.txt')
    sol(prizes)