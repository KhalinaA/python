def read_file(name):
    words = set()

    f = open(name, 'r') # Открываем файл

    for line in f: # Читаем строку
        for word in line.split(): # Разбиваем строку на слова
            words.add(word.lower()) # Записываем в сет слова в нижнем регистре

    f.close() # Закрываем файл
 
    return list(words) # Возвращаем список уникальных слов
        

def save_file(name, words):
    f = open(name, 'w') # Открываем файл

    # Записываем кол-во уникальных слов
    f.write(f"Уникалных слов: {len(words)}\n") 
    f.write(f"===============\n")

    # Записываем слова в алфавитном порядке
    for word in sorted(words):
        f.write(word + '\n')

    f.close() # Закрываем файл


words = read_file('data.txt')
print(words)

save_file('saved.txt', words)
