import re #загружаем пакет re для обработки регулярных выражений
def getInfo(filename = "input.txt"): # инициализируем функцию
    file = open(filename, mode="r", encoding="UTF-8") #открываем файл с кодировкой UTF-8
    trips = []
    pattern = r"(?:^Рейс) (\d+) (?:прибыл|отправился) (\w+) (\w+) (?:\w) (\d+:\d+:\d+)" #прописываем паттерн поиска для re
    for line in file: #инициализируем цикл проверки строк по паттерну
        if re.findall(pattern, line): #проверяем для каждой строки наш паттерн
            trips.append(re.findall(pattern, line)) #добавим кортеж подходящей строки в список trips
    file.close() #закрываем файл
    return trips #возвращаем данные которые мы взяли из filename

def returnInfo(filename = "output.txt"): # инициализируем функцию
    file = open(filename, mode="w", encoding="UTF-8") #открываем файл с кодировкой UTF-8 и правами на запись в файл
    trips = getInfo() #вызываем данные из предыдущей функции
    for trip in trips: #обработаем каждую поездку
        file.write(f"[{trip[0][3]}] - Поезд №{trip[0][0]} {trip[0][1]} {trip[0][2]} \n") #запишем поездку в filename
    file.close() #закрываем файл
returnInfo() #вызываем файл