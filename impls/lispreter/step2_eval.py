import functools
import getopt
import operator
import sys

from mal_types import Symbol, ParseError, List, Vector
from printer import pr_str
from reader import read_str

repl_env = {
    '+': lambda *args: functools.reduce(operator.add, args),
    '-': lambda *args: functools.reduce(operator.sub, args),
    '*': lambda *args: functools.reduce(operator.mul, args),
    '/': lambda *args: functools.reduce(operator.truediv, args),
}


def READ(str):
    return read_str(str)


def EVAL(ast, env):
    if isinstance(ast, ParseError):
        return ast
    elif not isinstance(ast, List):
        return eval_ast(ast, env)
    elif len(ast) == 0:
        return ast

    try:
        res = eval_ast(ast, env)
        return res[0](*res[1:])
    except KeyError:
        return "Invalid symbol"


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        return repl_env[ast.val]
    elif isinstance(ast, List):
        return List(map(lambda x: EVAL(x, env), ast))
    elif isinstance(ast, Vector):
        return Vector(map(lambda x: EVAL(x, env), ast))
    return ast


def PRINT(x):
    print(pr_str(x))


def rep(x):
    PRINT(EVAL(READ(x), repl_env))


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'd')
    isDebug = True if '-d' in [x[0] for x in opts] else False

    if isDebug:
        inp = '( + 2 (* 3 4) ) '
        rep(inp)

    else:
        while True:
            inp = input("user> ")
            rep(inp)
