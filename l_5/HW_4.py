with open("english.txt") as f:
    my_f = f.readlines()
    print(my_f)

with open("russian.txt", "w") as r:
    for line in my_f:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        r.write(line)
