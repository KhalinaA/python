import timeit

# Функция, создающая список четных чисел с помощью метода append
def even_numbers_append(n):
    result = []
    for i in range(n+1):
        if i % 2 == 0:
            result.append(i)
    return result

# Функция, создающая список четных чисел с помощью генератора списков
def even_numbers_comprehension(n):
    return [i for i in range(n+1) if i % 2 == 0]

# Декоратор для измерения времени работы функций
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"{func.__name__}: {end_time - start_time:.10f} seconds")
        return result
    return wrapper

# Использование декоратора для измерения времени работы функций
N = 1000000
even_numbers_append = measure_time(even_numbers_append)
even_numbers_comprehension = measure_time(even_numbers_comprehension)
even_numbers_append(N)
even_numbers_comprehension(N)
