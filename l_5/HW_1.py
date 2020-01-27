with open("text.txt", "w") as my_f:
    while True:
        text = input("Введите текст, который вы хотите записать в файл: ")
        if text == '':
            break
        my_f.write(text + "\n")

