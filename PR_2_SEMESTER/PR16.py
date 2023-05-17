import PySimpleGUI as sg
import os
import pdf2docx
import docx2pdf
from PIL import Image


def showMenu():
    sg.theme("DefaultNoMoreNagging")
    layout = [
        [sg.Text("Текущая директория: " + os.getcwd())],
        [sg.Button("Сменить рабочий каталог")],
        [sg.Button("Преобразовать PDF в DOCX")],
        [sg.Button("Преобразовать DOCX в PDF")],
        [sg.Button("Произвести сжатие изображений")],
        [sg.Button("Удалить группу файлов")],
        [sg.Button("Выход")]
    ]
    window = sg.Window("Меню", layout=layout)
    event, values = window.read()
    window.close()
    return event


def showFilesInDir(filesInDirectory):
    for i in range(0, len(filesInDirectory)):
        print(f"{i} : {filesInDirectory[i]}")

def play():
    event = showMenu()
    while event != "Выход":
        if event == "Сменить рабочий каталог":
            sg.popup(changeDir())
        elif event == "Преобразовать PDF в DOCX":
            sg.popup(convertPDFtoDOCX())
        elif event == "Преобразовать DOCX в PDF":
            sg.popup(convertDOCXtoPDF())
        elif event == "Произвести сжатие изображений":
            sg.popup(changeResolution())
        elif event == "Удалить группу файлов":
            sg.popup(deleteGroupOfFiles())
        event = showMenu()


def changeDir():
    newdirname = sg.popup_get_folder("Введите название директории")
    if os.path.exists(newdirname):
        if os.path.isdir(newdirname):
            os.chdir(newdirname)
    return "вы перешли в директорию:" + newdirname

def convertPDFtoDOCX():
    filesInDirectory = os.listdir(os.getcwd())
    choise = sg.popup_get_text("выберите файл")
    choise = int(choise)
    pdfFile = filesInDirectory[choise]
    wordFile = pdfFile.replace('.pdf', '.docx')
    cv = pdf2docx.Converter(pdfFile)
    cv.convert(wordFile)
    cv.close()
    sg.popup("PDF успешно преобразован в DOCX.")

def convertDOCXtoPDF():
    filesInDirectory = os.listdir(os.getcwd())
    choise = sg.popup_get_text("выберите файл")
    choise = int(choise)
    showFilesInDir(filesInDirectory)
    docxFile = filesInDirectory[choise]
    pdfFile = docxFile.replace('.docx', '.pdf')
    docx2pdf.convert(docxFile, pdfFile)
    sg.popup("DOCX успешно преобразован в PDF.")

def changeResolution():
    filesInDirectory = os.listdir(os.getcwd())
    choise = sg.popup_get_text("выберите файл")
    choise = int(choise)
    showFilesInDir(filesInDirectory)
    imagePath = filesInDirectory[choise]
    if not Image.isImageFile(imagePath):
        sg.popup("Выбранный файл не является изображением.")
        return
    with Image.open(imagePath) as img:
        print(img.format, img.size, img.format_description)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(imagePath, optimize=True, quality=1)

def deleteGroupOfFiles():
    filesInDirectory = os.listdir(os.getcwd())
    showFilesInDir(filesInDirectory)
    patternType = sg.popup_get_text("Введите тип паттерна: 0-префикс 1-постфикс 2-подстрока 3-расширение")
    patternType = int(patternType)
    if patternType == 0:
        substr = sg.popup_get_text('Введите префикс')
        for i in range(0, len(filesInDirectory)):
            if filesInDirectory[i].lower().startswith(substr.lower()):
                path = os.path.join(os.getcwd(), filesInDirectory[i])
                os.remove(path)
    elif patternType == 1:
        substr = sg.popup_get_text('Введите постфикс')
        for i in range(0, len(filesInDirectory)):
            if filesInDirectory[i].lower().endswith(substr.lower()):
                path = os.path.join(os.getcwd(), filesInDirectory[i])
                os.remove(path)
    elif patternType == 2:
        substr = sg.popup_get_text('Введите подстроку')
        for i in range(0, len(filesInDirectory)):
            if substr.lower() in filesInDirectory[i].lower():
                path = os.path.join(os.getcwd(), filesInDirectory[i])
                os.remove(path)
    elif patternType == 3:
        substr = sg.popup_get_text('Введите расширение')
        for i in range(0, len(filesInDirectory)):
            if ('.' + substr.lower()) in filesInDirectory[i].lower():
                path = os.path.join(os.getcwd(), filesInDirectory[i])
                os.remove(path)

if __name__ == "__main__":
    play()
