
def get_lists():
    l1, l2 = [], []

    with open("lists.txt", 'r') as f:
        for line in f.readlines():
            i1, i2 = line.split('   ')
            l1.append(int(i1.strip()))
            l2.append(int(i2.strip()))
    
    l1.sort()
    l2.sort()

    return l1, l2


def part_1(l1, l2):
    dist = 0

    for i in range(0, len(l1)):
        dist += abs(l2[i] - l1[i])

    print(dist)


def part_2(l1, l2):

    for i in range(0, len(l1)):
        l1[i] = l1[i] * l2.count(l1[i])

    print(sum(l1))

if __name__ == '__main__':
    l1, l2 = get_lists()
    part_1(l1, l2)
    part_2(l1, l2)