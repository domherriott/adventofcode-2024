
def get_reports():
    reports = []

    with open("reports.txt", 'r') as f:
        for line in f.readlines():
            report = line.split(' ')
            report = [int(s.replace('\n', '')) for s in report]
            reports.append(report)

    return reports

def part_1(reports):

    def is_safe(report):

        ascending = report[1] >= report[0]

        for i in range(1, len(report)):
        
            diff = report[i] - report[i-1]
            if not ascending:
                diff = -diff
            
            if diff <= 0 or diff > 3:
                return False
                        
        return True
        

    safe, unsafe = [], []
    for report in reports:
        if is_safe(report):
            safe.append(report)
        else:
            unsafe.append(report)

    print('safe:', len(safe))
    print('unsafe:', len(unsafe))


def part_2(reports):

    def check_dampener(d):
        if d > 1:
            return False
        else:
            return True

    def is_safe(report):
        d = 0
        ascending = report[1] >= report[0]

        for i in range(1, len(report)):
        
            diff = report[i] - report[i-1]
            if not ascending:
                diff = -diff
            
            if diff <= 0 or diff > 3:
                d += 1
          
        return check_dampener(d)
        

    safe, unsafe = [], []
    for report in reports:
        if is_safe(report):
            safe.append(report)
        else:
            unsafe.append(report)

    print('safe:', len(safe))
    print('unsafe:', len(unsafe))


if __name__ == '__main__':
    reports = get_reports()
    part_1(reports)
    part_2(reports)
