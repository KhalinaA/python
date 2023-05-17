class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a+self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        return self.a / self.b

    def substraction(self):
        return self.a-self.b


calc = Math(255, 11)
print(calc.addition(), calc.multiplication(),
      calc.division(), calc.substraction())
