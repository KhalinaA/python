import random

sym = '\u25A0' 
heart = '\u2661'
WORDS = [
    'книга', 'месяц', 'ручка', 
    'шарик', 'олень', 'носок', 
    'информатика', 'газонокосилка',
    'динозавр','автомобиль'    
]


def play(answer, lives):
    # Формирование начальной строки с закрытыми символами
    word = len(answer) * sym 

    # Игра не заканчивается, пока не кончатся жизни или слово не будет угадано
    while word != answer and lives > 0:
        print(f"{word} | {heart} x {lives}")
        guess = input("Назовите букву или слово целиком: ")
        
        # Если вводится слово целиком
        if len(guess) != 1:
            if guess != answer:
                print("Неправильно, вы теряете жизнь")
                lives -= 1
            else:
                break
            
        # Если вводится одна буква 
        elif len(guess) == 1:
            word_copy = list(word)
            # Поиск буквы в загаданном слова
            for i in range(len(answer)):
                # Если буква есть, меняем символ закрытой буквы
                if answer[i] == guess:
                    word_copy[i] = guess
            
            word_copy = ''.join(word_copy)

            # Если слово осталось неизменным (буквы нет в загаданном слове)
            # то теряем жизнь
            if word == word_copy:
                print("Неправильно, вы теряете жизнь")
                lives -= 1
            else:
                word = word_copy

    # Игра проиграна, если цикл был покинут из-за отсутствия жизней
    if lives == 0:
        print(f"Вы проиграли. Правильное слово: {answer}")
    else:
        print(f"Вы выиграли!!!")


def main():
    word_list = WORDS
    difficulties = [7, 5, 3] # Кол-во жизней на различных уровнях сложности
    
    diff = int(input("Выберите сложность (1 - Легкий, 2 - Средний, 3 - Сложный): "))
    lives = difficulties[diff-1]

    game_over = False
    while not game_over and len(word_list) > 0:
        answer = word_list[random.randint(0, len(word_list)-1)] # Выбор случайного слова
        word_list.remove(answer) # После выбора слова, удаляем из списка,
                                 # чтобы не было повторяющихся слов

        play(answer, lives) # Запуск игры

        # Если слова в списке еще не закончились, предложить поиграть еще раз
        if len(word_list) > 0 and input("Сыграем еще раз? (n - чтобы выйти): ") == 'n':
            game_over = True


if __name__ == "__main__":
    main()