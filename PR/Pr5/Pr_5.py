def getDataFromFile(filename = "input.txt"): #инициализация функции по получению данных из файла
    try: #просим попытаться python выполнить алгоритм внутри try
        file = open(filename, mode="r") #открываем файл
        counter = int(file.readline()) #считываем количество цифр
        for i in range(0,counter): #инициализируем цикл по выводу чисел из файла
            print(int(file.readline().replace('\n', ''))) #выводим число из файла
        file.close() #закрываем файл
    except ValueError: #если значения получаемые из файла неверные, то срабатывает данный exception
        print('Данные в файле либо повреждены, либо не имеют целостности')
    except FileNotFoundError:#если файла не существует то срабатывает данный exception
        print('Данного файла нет, либо путь указан неверно')
    finally:#срабатывает после обработки всех ошибок
        print('Работа программы окончена')

getDataFromFile() #вызываем функцию
