my_dict = dict()

with open("lessons.txt") as less:
    l = less.readlines()
    for line in l:
        lines = line.split()
        subj = lines[0]
        sum_less = sum([int(x[:x.find('(')]) for x in lines[1:] if '(' in x])
        my_dict[subj] = sum_less

print(my_dict)
