with open("text.txt") as my_f:
    line = my_f.readlines()
    print("Строк в файле: ", len(line))
    for num, line in enumerate(line, start=1):
        if len(line.split()) <= 1:
            print('В {} строке находится - {} слово'.format(num, len(line.split())))
        elif len(line.split()) <= 4 and len(line.split()) > 1:
            print('В {} строке находится - {} слова'.format(num, len(line.split())))
        elif len(line.split()) >= 5:
            print('В {} строке находится - {} слов'.format(num, len(line.split())))