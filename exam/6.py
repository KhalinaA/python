#индексы - используютрся для обозначения эл-ов массива, строк. Нужны, чтобы обращаться к этим эл-ам. Отрицательные индексы нужны, чтобы обращаться к элементам с конца


def first_non_repeating_letter(string):
   for char in string:
      if string.find(char) == string.rfind(char):
         return char
         return None
print(first_non_repeating_letter("hhPPj"))