from random import randrange
import string
def generatePassword(l):
    password = ""
    typeSym = input("Выбрать формат кодирования:")
    for i in range(l):   
        if i < 4:
            typeSym = i
        if typeSym == 0:
            password += string.ascii_lowercase[randrange(len(string.ascii_lowercase))]
        elif typeSym == 1:
            password += string.ascii_uppercase[randrange(len(string.ascii_uppercase))]
        elif typeSym == 2:
            password += string.punctuation[randrange(len(string.punctuation))]
        elif typeSym == 3:
            password += string.digits[randrange(10)]
    return password

n = int(input("Введите кол-во паролей: "))
passwords_file = open("passwords.txt", "w")
for i in range(n):
    l = int(input("Введите длину пароля: "))
    p = generatePassword(l)
    print(p)
    passwords_file.write(p + '\n')
passwords_file.close()
