import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def showMenu():#эта менюшка показывает нам что можно выбрать
    print("Текущая директория:" + os.getcwd())   #эта функция показывает нам путь к рабочей папке
    print("0:Сменить рабочий каталог")
    print("1:Преобразовать PDF в DOCX")
    print("2:Преобразовать DOCX в PDF")
    print("3:Произвести сжатие изображений")
    print("4:Удалить группу файлов")
    print("5:Выход")

def showFilesInDir(filesInDirectory):
    for i in range(0,len(filesInDirectory)):
        print(f"{i} : {filesInDirectory[i]}")    #эта функция показывает нам какие файлы есть в директории

def play():  #это точка входа во всю программу, с нее она начинается
    showMenu()
    choise = int(input("Введите номер"))
    while choise != 5:
        if choise == 0:
            print(changeDir())
        elif choise == 1:
            print(convertPDFtoDOCX())
        elif choise == 2:
            print(convertDOCXtoPDF())
        elif choise == 3:
            print(changeResolution())
        elif choise == 4:
            print(deleteGroupOfFiles())
        else:
            break
        showMenu()
        choise = int(input("Введите номер"))

def changeDir(): # эта функция меняет рабочую директорию
    newdirname = input("Введите название директории")
    if(os.path.exists(newdirname)): #проверяем есть ли такой путь
        if(os.path.isdir(newdirname)): #проверяем является ли конец пути директорией
            os.chdir(newdirname) #переходим в директорию
    return "вы перешли в директорию:" + newdirname

def convertPDFtoDOCX():
    filesInDirectory = os.listdir(os.getcwd())
    choise = showFilesInDir(filesInDirectory)
    choise = int(input("выберите файл"))
    pdfFile = filesInDirectory[choise]
    wordFile = pdfFile.replace('.pdf', '.docx')
    cv = Converter(pdfFile) #вызов функции пакета, которая преводит пдф в докикс
    cv.convert(wordFile)
    cv.close()


def convertDOCXtoPDF():
    filesInDirectory = os.listdir(os.getcwd())
    choise = int(input("выберите файл"))
    showFilesInDir(filesInDirectory)
    docxFile = filesInDirectory[choise]
    pdfFile = docxFile.replace('.docx', '.pdf')
    convert(docxFile) #вызов функции которая переводит докикс в пдф

def changeResolution():
    filesInDirectory = os.listdir(os.getcwd())
    choise = int(input("выберите файл"))
    showFilesInDir(filesInDirectory)
    imagePath = filesInDirectory[choise]
    with Image.open(imagePath) as img:
        print(img.format, img.size, img.format_description)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(imagePath, "JPEG", optimize=True, quality=1) #данная функция сжимает изображение до 1%


def deleteGroupOfFiles():
    filesInDirectory = os.listdir(os.getcwd())
    showFilesInDir(filesInDirectory)
    patternType = int(input("Введите тип паттерна: 0-префикс 1-постфикс 2-подстрока 3-расширение"))
    if patternType == 0:
        substr = input('Введите префикс')
        for i in range(0, len(filesInDirectory)):
            if filesInDirectory[i].lower().startswith(substr.lower()):
                path = f"{os.getcwd()}\{filesInDirectory[i]}"
                os.remove(path) #удаляет объект по его адресу
    elif patternType == 1:
        substr = input('Введите постфикс')
        for i in range(0, len(filesInDirectory)):
            if filesInDirectory[i].lower().endswith(substr.lower()):
                path = f"{os.getcwd()}\{filesInDirectory[i]}"
                os.remove(path)
    elif patternType == 2:
        substr = input('Введите подстроку')
        for i in range(0, len(filesInDirectory)):
            if substr.lower() in filesInDirectory[i].lower():
                path = f"{os.getcwd()}\{filesInDirectory[i]}"
                os.remove(path)
    elif patternType == 3:
        substr = input('Введите расширение')
        for i in range(0, len(filesInDirectory)):
            if ('.'+substr.lower()) in filesInDirectory[i].lower():
                path = f"{os.getcwd()}\{filesInDirectory[i]}"
                os.remove(path)