import time


def cache(func):
    memo = {}

    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper


def timer(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(
            f"Function {func.__name__} took {end - start:.5f} seconds to execute")
        return result
    return wrapper


@cache
@timer
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(20))



def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
fibonacci(20)
end = time.time()
print(f"Function fibonacci took {end - start:.5f} seconds to execute")

cached_fibonacci = cache(fibonacci)

start = time.time()
cached_fibonacci(20)
end = time.time()
print(f"Function cached_fibonacci took {end - start:.5f} seconds to execute")
