import functools
import operator
from itertools import chain

import printer
from mal_types import List, Vector, HashMap


def eq(x, y):
    if type(x).__name__ != type(y).__name__:
        return False
    elif isinstance(x, List) or isinstance(x, Vector) and len(x) == len(y):
        return True if len(x) == 0 else len(
            [0 for xel, yel in zip(x, y) if eq(xel, yel)]
        ) > 0
    elif isinstance(x, HashMap) and len(x.keys()) == len(y.keys()):
        return True if len(x.keys()) == 0 else len(
            [0 for xk, xv in x.items() if xk in y.keys() and eq(xv, y[xk])]
        ) > 0
    return x == y


ns = \
    {
        'pr-str': lambda *args: " ".join(map(lambda x: printer.pr_str(x, True), args)),
        'str': lambda *args: "".join(map(lambda x: printer.pr_str(x, False), args)),
        'prn': lambda *args: print(" ".join(map(lambda x: printer.pr_str(x, True), args))),
        'println': lambda *args: print(" ".join(map(lambda x: printer.pr_str(x, False), args))),

        '=': eq,
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '+': lambda *args: functools.reduce(operator.add, args),
        '-': lambda *args: functools.reduce(operator.sub, args),
        '*': lambda *args: functools.reduce(operator.mul, args),
        '/': lambda *args: functools.reduce(operator.floordiv, args),
        'not': lambda x: True if x is None or x is False else False,

        'list': lambda *args: List(args),
        'list?': lambda x: isinstance(x, List),
        'cons': lambda x, seq: List(List([x]) + seq),
        'concat': lambda *args: List(chain(*args)),
        'vec': lambda x: Vector(x),
        'empty?': lambda x: len(x) == 0,
        'count': lambda x: 0 if x is None else len(x)
    }
