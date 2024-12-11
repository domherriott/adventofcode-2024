def get_input():
    with open("input.txt", 'r') as f:
        for i, line in enumerate(f):
            return line.replace('\n','')

def conv_to_dmap(dense):
    dmap = '[0]' * int(dense[0])
    idnum = 1

    for i in range(1, len(dense), 2):
        dmap += ('.' * int(dense[i]))
        dmap += (f'[{str(idnum)}]' * int(dense[i+1]))
        idnum += 1
    
    return dmap, idnum

def clean_dmap(dmap, p1, max_id):

    if p1:
        while True:
            first_space = dmap.find('.')
            file_l = dmap.rfind('[')
            file_r = dmap.rfind(']')

            if '.' not in dmap or first_space > file_r:
                return dmap
            
            dmap = dmap[:first_space] + dmap[file_l:file_r+1] + dmap[first_space+1:file_l]

            wasted_space = dmap.rfind(']') + 1
            dmap = dmap[:wasted_space]

    else:

        def find_space(dmap, file_full_len):
            
            for i, letter in enumerate(dmap):
                if i == 0:
                    prev = False
                    start, end = 0, 0

                elif letter == '.':
                    if not prev:
                        start = i
                        prev = True
                elif prev:
                    prev = False
                    end = i
                    if end-start >= file_full_len:
                        return [start,end]
                
            return None



        for idx in range(max_id-1, -1, -1):
            print('idx:',idx)

            search_str = f'[{str(idx)}]'
            file_r = dmap.rfind(search_str) + len(search_str) 
            file_l = dmap.find(search_str)
            file_full = dmap[file_l:file_r]
            file_full_len = file_full.count('[')
            space = find_space(dmap, file_full_len)
            
            if space is None:
                continue

            space_l = space[0]
            space_r = space[-1]+1
            space_len = space_r - space_l
            if idx == -1:
                return dmap

            if  space_l < file_l and file_full_len <= space_len:
                spaces_left = space_len - file_full_len
                dmap = dmap[:space_l]  + file_full + (dmap[space_r-spaces_left:file_l]) + ( file_full_len * '.') + dmap[file_r:]
                continue

        return dmap




def checksum(clean):
    print(clean)
    print(clean.split('.'))
    ints = [int(c[0]) for c in clean[1:-1].split('[')]
    print('checksum:', sum(ints))

    li = []
    num_bool=False
    num_str = ''
    for char in clean:
        print(char, num_str)
        if char == ']':
            num_bool=False
            li.append(int(num_str))
            num_str = ''
        if num_bool:
            num_str += char
        if char == '[':
            num_bool=True
        if char == '.':
            li.append(0)

    checksum = 0
    for i in range(0, len(li)):
        checksum += i * li[i]

    print('checksum:', checksum)

def sol(dense, p1):
    dmap, max_id = conv_to_dmap(dense)
    print(dmap)
    clean = clean_dmap(dmap, p1=p1, max_id=max_id)
    checksum(clean)

if __name__ == '__main__':
    dense = get_input()
    # dense = '2333133121414131402'
    sol(dense, p1=False)