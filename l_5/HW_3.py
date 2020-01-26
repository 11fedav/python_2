with open("salary.txt") as s:
    lines = s.readlines()
    salaries = []

    for line in lines:
        second_name, salary = line.split()
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
        else:
            print("Таких сотрудников нет")
print("Средняя з/п сотрудников составила: ", sum(salaries) / len(lines))

