
def get_input():
    tasks = []

    with open("input.txt", 'r') as f:

        for line in f.readlines():
            answer, nums = line.split(":")
            nums = [int(num) for num in nums.strip().split(' ')]
            tasks.append([int(answer), nums])

    return tasks


def is_sol(answer, curr_num, rem_nums, third_op):

    if curr_num > answer:
        return False
    
    if len(rem_nums) < 1:
        if curr_num == answer:
            return True
        else:
            return False
    
    if is_sol(answer=answer, curr_num=curr_num + rem_nums[0], rem_nums=rem_nums[1:], third_op=third_op):
        return True
    if is_sol(answer=answer, curr_num=curr_num * rem_nums[0], rem_nums=rem_nums[1:], third_op=third_op):
        return True
    if third_op:
        if is_sol(answer=answer, curr_num=int(str(curr_num) + str(rem_nums[0])), rem_nums=rem_nums[1:], third_op=third_op):
            return True
        
    return False
    
    


def solve(tasks):
    p1 = 0
    p2 = 0
    for task in tasks:
        answer = task[0]
        nums = task[1]

        if is_sol(answer=answer, curr_num=nums[0], rem_nums=nums[1:], third_op=False):
            p1 += answer
        if is_sol(answer=answer, curr_num=nums[0], rem_nums=nums[1:], third_op=True):
            p2 += answer

    print('part1:', p1)
    print('part2:', p2)


if __name__ == '__main__':
    tasks = get_input()
    solve(tasks=tasks)