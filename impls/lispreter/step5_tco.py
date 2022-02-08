from core import ns
from env import Env
from mal_types import Symbol, List, Vector, HashMap, fn
from printer import pr_str
from reader import read_str

repl_env = Env()
for k, v in ns.items():
    repl_env.set(k, v)


def READ(str):
    return read_str(str)


def EVAL(ast, env):
    while True:
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
            ast = ast[2]
            env = let_env
        elif ast[0] == 'do':
            ast = eval_ast(ast[1:-1], env)[-1]
        elif ast[0] == 'if':
            cond = EVAL(ast[1], env)
            if cond is None or cond is False:
                if len(ast) > 3:
                    ast = ast[3]
                else:
                    ast = None
            else:
                ast = ast[2]
        elif ast[0] == 'fn*':
            return fn(EVAL, ast[1], ast[2], env)
        else:
            l = eval_ast(ast, env)
            f = l[0]
            if hasattr(f, '__ast__'):
                ast = f.__ast__
                env = f.__env__(l[1:])
            else:
                return f(*l[1:])


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


def REP(x):
    PRINT(EVAL(READ(x), repl_env))


if __name__ == '__main__':
    while True:
        try:
            inp = input("user> ")
            REP(inp)
        except Exception as e:
            print(e)