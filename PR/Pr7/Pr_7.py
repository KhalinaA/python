import csv #импортируем модуль csv для чтения csv файлов

def readFile(filename = "input.csv"): #инициализируем функцию readfile которая будет доставать данные из filename
    with open(filename) as csvfile: #используем модуль csv для легкого открытия и чтения csv
        file = csv.reader(csvfile, delimiter="|") #открываем файл
        data = [] #инициализируем список строк файла
        for row in file: #инициализируем обход всех строк файла
            newRow = [] #создаем пустую строку для новых данных
            for element in row: #проходим по элементам строки
                newRow.append(element.lower()) #записываем в пустую строку данные из строчки файла,
                # но записываем в маленьком регистре чтобы упростить поиск
            data.append(newRow) #записываем строку в список строк файла
    return data[1:] #возвращаем список строк исключая первую, так как там хранятся подписи

def searchInRowByWord(row, word): #инициализируем функцию которая ищет ключевое слово в определенной строчке данных
    for element in row: #обходим все элементы строки
        if word.lower() in element: #если в элементе содержится кодовая подстрока то возвращаем true
            return True #
    return False #данный элемент срабатывает если мы ничего не возвращали, те если мы не нашли строчку к кодовым словом
#то функция вернет false

def get_books(word): #функция вовзращает нам строки содержащие ключевое слово
    data = readFile() #вызов функции прочтения файла
    result = [] #инициализация массива, который возвращает данные
    for row in data: #обходим каждую строку в списке строк
        if searchInRowByWord(row, word): #если функция вернет true то данная строка содержит нужное слово
            result.append(row) #добавляем строку которая содержит слово
    return result #вовзращаем список строк

def get_totals(list, limiter, counter): #функция возвращает нам измененные кортежи данных,
    # list-список данных, limiter-число с которым мы сравниваем, counter - число которое прибавляем
    result = [] #список который будет возвращать функция
    for row in list: #проходим строки в списке
        number = (int(row[3]) * int(row[4])) #умножаем quantity*price
        if (number < limiter): #сравниваем с limiter
            number += counter #увеличиваем число
        data = tuple([str(row[0]), str(number)]) #записываем данные
        result.append(data) #добавляем данные в конечный список который вернет функция
    return result

print(get_books('python'))
print(get_totals(get_books(''), 500, 100)) #вызываем функции