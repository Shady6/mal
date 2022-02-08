import functools
import operator

from env import Env
from mal_types import Symbol, List, Vector, HashMap
from printer import pr_str
from reader import read_str

repl_env = Env()
repl_env.set('+', lambda *args: functools.reduce(operator.add, args))
repl_env.set('-', lambda *args: functools.reduce(operator.sub, args))
repl_env.set('*', lambda *args: functools.reduce(operator.mul, args))
repl_env.set('/', lambda *args: functools.reduce(operator.truediv, args))


def READ(str):
    return read_str(str)


def EVAL(ast, env):
    if not isinstance(ast, List):
        return eval_ast(ast, env)
    elif len(ast) == 0:
        return ast
    elif ast[0] == 'def!':
        return env.set(ast[1], EVAL(ast[2], env))
    elif ast[0] == 'let*':
        let_env = Env(outer=env)
        for i in range(0, len(ast[1]), 2):
            let_env.set(ast[1][i], EVAL(ast[1][i + 1], let_env))
        return EVAL(ast[2], let_env)
    else:
        f = eval_ast(ast, env)
        return f[0](*f[1:])


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        return env.get(ast)
    elif isinstance(ast, List):
        return List(map(lambda x: EVAL(x, env), ast))
    elif isinstance(ast, Vector):
        return Vector(map(lambda x: EVAL(x, env), ast))
    elif isinstance(ast, HashMap):
        return HashMap(((k, EVAL(v, env)) for k, v in ast.items()))
    return ast


def PRINT(x):
    print(pr_str(x))


def rep(x):
    PRINT(EVAL(READ(x), repl_env))


if __name__ == '__main__':
    while True:
        try:
            inp = input("user> ")
            rep(inp)
        except Exception as e:
            print(e)
