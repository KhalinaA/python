# getName, getAge, getGroupNumber,setNameAge, setGroupNumber.

class student():

    def __init__(self, name="Ivan", age=18, groupNumber="10A"):

        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def setName(self, name):
        return "Имя студента %s" % name

    def setAge(self, age):
        return "Возраст студента %s" % age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber
        return "Номер группы студента %s" % groupNumber


Ivan = student()
Stas = student("Stas", 20, "ПИ-3")
Alina = student("Alina", 21, "ПИ-4")


print(Stas.setGroupNumber("ПИ-3"))
print(Alina.setAge("21"))
print(Ivan.name, Ivan.age, Ivan.setGroupNumber("10А"))
