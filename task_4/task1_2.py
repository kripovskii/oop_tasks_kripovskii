from time import time
cache = {}
def time_decorator(func):
    def time_check(*args, **kwargs):
        time1 = time()
        func(*args, **kwargs)
        time2 = time()
        result = time2 - time1
        print(result)
    return time_check

def cache_decorator(func):
    def cache_check(*args, **kwargs):
        if not cache.get(args):
            result = func(*args, **kwargs)
            cache[args] = result
            return result
        else:
            return cache[args]
    return cache_check

@time_decorator
@cache_decorator
def test(x):
    if not cache.get(x):
        print(x + 1 * 10 + 1)
    else:
        print(cache[x])

while (True):
    inp = int(input())
    if inp != 0:
        test(inp)
    else:
        break