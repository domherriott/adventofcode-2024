
def get_ws():
    ws = []

    with open("wordsearch.txt", 'r') as f:
        for line in f.readlines():
            ws.append(list(line.replace('\n', '')))
    
    return ws


def part_1(ws):
    n = 0

    rows = ['' for _ in range(len(ws))]
    cols = ['' for _ in range(len(ws[0]))]

    for i, row in enumerate(ws):
        
        for j, char in enumerate(row):
            rows[i] += char
            cols[j] += char
 

    def scan_for_diag(ws):
        diags = []

        def scan(ws):
            d = {}
            for i, row in enumerate(ws):
                
                for j, char in enumerate(row):

                    s = i + j
                    if s in d:
                        d[s] += char
                    else:
                        d[s] = str(char)
            
            for k, v in d.items():
                diags.append(v)

        scan(ws)
        reflected_ws = [line[::-1] for line in ws]
        scan(reflected_ws)

        return diags
    
    diags = scan_for_diag(ws)
  
    # print('rows:',rows)
    # print('cols:', cols)
    # print('diags:', diags)

    n += rows.count('')
    strings = rows + cols + diags
    for string in strings:
        n += string.count('XMAS')
        n += string[::-1].count('XMAS')
    
    print('XMAS count:', n)

def part_2(ws):
    n = 0

    for i, row in enumerate(ws):
        for j, char in enumerate(row):
            surrounding = ''
            if i >= 1 and j >= 1 and i < len(ws)-1 and j < len(ws[0])-1 and char == 'A':
                tl = ws[i-1][j-1]
                tr = ws[i-1][j+1]
                bl = ws[i+1][j-1]
                br = ws[i+1][j+1]
                surr = ''.join([tl, tr, bl, br])

                if surr.count('M') == 2 and surr.count('S') == 2 and tl != br:
                    n += 1

 
    print('X-MAS count:', n)

if __name__ == '__main__':
    ws = get_ws()
    part_1(ws)
    part_2(ws)
