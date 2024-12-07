def get_data():
    rules, updates = [], []

    with open("data.txt", 'r') as f:
        rules_flag = True

        for line in f.readlines():

            if line == '\n':
                rules_flag = False
                continue

            if rules_flag:
               l, r = line.split('|')
               rules.append([int(l), int(r.replace('\n',''))])

            else:
                pages = line.split(',')
                updates.append([int(page.replace('\n','')) for page in pages])

    return rules, updates

def parse_rules(rules):
    drules = {}
    for rule in rules:
        l, r = rule[0], rule[1]

        if l in drules:
            drules[l].append(r)
        else:
            drules[l] = [r]

    return drules


def sum_middle(updates):
    summ = 0
    for update in updates:
        mid_idx = int((len(update)-1)/2)
        summ += update[mid_idx]
    return summ


def sol(drules, updates):

    def get_valid_updates(updates, drules):

        def is_valid(update):
            for i, num in enumerate(update):
                if i == 0:
                    continue
                if len(set(drules[num]).intersection(update[:i])) > 0:
                    return False
                
            return True
        
        valid, invalid = [], []

        for update in updates:
            if is_valid(update):
                valid.append(update)
            else:
                invalid.append(update)

        return valid, invalid
    

    def solve_invalid(invalid, drules):
        solved = []

        def bubble(update, drules):
            for n in range(0, len(update)):
                swaps = False

                for i in range(1, len(update)):
                    if i == 0:
                        continue
                    if len(set(drules[update[i]]).intersection(update[:i])) > 0:
                        update[i], update[i-1] = update[i-1], update[i]
                        swaps = True

                if not swaps:
                    break

            return update


        for update in invalid:
            solved.append(bubble(update, drules))

        return solved


    

    valid, invalid = get_valid_updates(updates, drules)

    solved_invalid = solve_invalid(invalid, drules)
     



    print('valid - sum_middle:', sum_middle(valid))
    print('solved - sum_middle:', )




if __name__ == '__main__':
    rules, updates = get_data()

    drules = parse_rules(rules)


    invalid = sol(drules, updates)
