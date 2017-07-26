def fib(n):
    pre, curr = 0, 1
    k = 2
    while k <= n:
        pre, curr = curr, pre + curr
        k = k + 1
    if n == 0: return pre
    else:      return curr

for i in range(10):
    print(i, ":", fib(i))

def fib_v2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_v2(n-1) + fib_v2(n-2)

for i in range(10):
    print(i, ":", fib(i))

def test_scope(y):
    def inner(z):
        return z + y
    y = 40
    print(inner(10))

test_scope(20)

def iter_eval(guess, iter_next, isgoodenough):
    # while not isgoodenough(guess):
    #     guess = iter_next(guess)
    # return guess
    if isgoodenough(guess):
        return guess
    else:
        return iter_eval(iter_next(guess), iter_next, isgoodenough)

def isapprox(x, y, eps = 1e-5):
    return abs(x - y) < eps

def golden_value():
    def iter_next(guess):
        return 1 / guess + 1
    def test(guess):
        return isapprox(guess ** 2, guess + 1)
    return iter_eval(1.0, iter_next, test)

def sqrt(x):
    def iter_next(guess):
        return 0.5 * (guess + x / guess)
    def test(guess):
        return isapprox(guess ** 2, x)
    return iter_eval(x / 2, iter_next, test)

def newton_method(f, initial_value):
    def newton_next(x):
        return x - f(x) / f_dev(x, f)
    def f_dev(x, f, delta = 1e-5):
        return (f(x+delta) - f(x)) / delta
    return iter_eval(initial_value, newton_next, lambda x : isapprox(f(x), 0))

print(newton_method(lambda x : (x ** 2 - 16), 1.0))
print(newton_method(lambda x : (2 ** x - 32), 1.0))
    
from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant
    
# def area_square(r):
#     assert r > 0, 'A length must be positive'
#     return r * r

# def area_circle(r):
#     assert r > 0, 'A length must be positive'
#     return r * r * pi

# def area_hexagon(r):
#     assert r > 0, 'A length must be positive'
#     return r * r * 3 * sqrt(3) / 2

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_circle(r):
    return are(r, 3 * sqrt(3) / 2)



