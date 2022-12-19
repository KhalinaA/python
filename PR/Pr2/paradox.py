import random

def monty_hall(n):
    answer = []
    rightCnt = 0
    for i in range(n):
        myChoice = random.randrange(1,4)
        rightAnswer = random.randrange(1,4)
        if myChoice == rightAnswer:
            rightCnt += 1

    # print("Вероятность если не меняем выбор: ",rightCnt/n)

    answer.append(rightCnt/n)

    rightCnt = 0
    for i in range(n):
        values = [1,2,3]
        myChoice = random.randrange(1,4)
        rightAnswer = random.randrange(1,4)
        incorrectValues = values.copy()
        incorrectValues.remove(rightAnswer)
        toRemove = 0
        for a in incorrectValues:
            if a != myChoice:
                toRemove = a
        values.remove(toRemove)


    myNewChoice = 0
    for a in values:
        if a != myChoice:
            myNewChoice = a
    # print(values, myChoice, rightAnswer,myNewChoice)

    if myNewChoice == rightAnswer:
        rightCnt += 1

    # print("Вероятность если меняем выбор: ",rightCnt/n)
    answer.append(rightCnt/n)

    return answer


def birthday(n):
    # Расчет вероятности, что все дни рождения будут различными
    p = 1 - 1/365
    for i in range(2, n):
        p *= 1 - i/365

    return 1 - p # Хотя бы у двух совпадут
