import pymorphy2
from translate import Translator #особое внимание этим библиотекам)
import csv

def getWordsNormalized(filename = "input.txt"):
    words = ""
    file = open(filename, encoding="UTF-8")
    for line in file:
        words += line.replace('\n', '')
    words = words.replace(' ', '')
    wordsNormalized = []
    morph = pymorphy2.MorphAnalyzer(lang="ru") #инициализируем полиморфный анализатор который приводит слова к нормальной форме
    for element in words:
        wordsNormalized.append(morph.parse(element)[0].normal_form) #приводим все слова к нормальной форме
    wordsStat = {}
    for element in wordsNormalized:
        if element in wordsStat:
            wordsStat[element] += 1
        else:
            wordsStat[element] = 1
    return dict(sorted(wordsStat.items(), key=lambda item: -item[1])) #сортируем словарь конечных данных

def translateWords():
    translator = Translator(from_lang='ru', to_lang='en', provider='mymemory')#инициализируем класс переводчика
    words = getWordsNormalized()
    data = []
    for word in words.keys():
        data.append([translator.translate(word),word,words[word]]) #переводим каждое слово
    with open('output.csv', 'w', encoding="utf-8") as csvfile: #записываем в csv файл
        writer = csv.writer(csvfile, delimiter='|',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['перевод|слово|количество упомнинаний'])
        for element in data:
            writer.writerow(element)
    return data

print(translateWords())

