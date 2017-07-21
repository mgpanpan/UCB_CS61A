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

x = 10

def test_scope(y):
    print(x)

x = 20

test_scope(10)
