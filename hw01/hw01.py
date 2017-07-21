from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    # if a > b:
    #     if b > c:
    #         return a * a + b * b
    #     else:
    #         return a * a + c * c
    # else:
    #     if a > c:
    #         return a * a + b * b
    #     else:
    #         return b * b + c * c
    return a * a + b * b + c * c - min(a, b, c) ** 2

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    return 1

def f():
    "*** YOUR CODE HERE ***"
    return 1 / 0

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    cnt, m = 1, n
    while m != 1:
        print(m)
        if m % 2 == 0:
            m = m // 2
        else:
            m = m * 3 + 1
        cnt = cnt + 1
    print(m)
    return cnt

# 还未明白
challenge_question_program = """
s = 'print("s = " + repr(s) + "; eval(s)")'; eval(s)
"""
# Reference for last question:
# http://www.madore.org/~david/computers/quine.html
# http://switchb.org/kpreid/quines
# https://github.com/mame/quine-relay
