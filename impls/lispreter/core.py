import functools
import operator

import printer
from mal_types import List

ns = \
    {
        '=': lambda x, y: x == y,
        'pr-str': lambda *args: " ".join(map(lambda x: printer.pr_str(x, True), args)),
        'str': lambda *args: "".join(map(lambda x: printer.pr_str(x, False), args)),
        'prn': lambda *args: print(" ".join(map(lambda x: printer.pr_str(x, True), args))),
        'println': lambda *args: print(" ".join(map(lambda x: printer.pr_str(x, False), args))),

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

        'empty?': lambda x: len(x) == 0,
        'count': lambda x: 0 if x is None else len(x)
    }
