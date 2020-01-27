with open("numbers.txt", "r+") as n:
    num = input("Введите несколько чисел, разделённых пробелами: ")
    n.write(num)

    numbers = map(int, num.split())
    sum_num = sum(numbers)
    print(sum_num)