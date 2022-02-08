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
            # TCO
        elif ast[0] == 'quote':
            return ast[1]
        elif ast[0] == 'quasiquote':
            ast = quasiquote(ast[1])
            # TCO
        elif ast[0] == 'quasiquoteexpand':
            return quasiquote(ast[1])
        elif ast[0] == 'do':
            eval_ast(ast[1:-1], env)
            ast = ast[-1]
            # TCO
        elif ast[0] == 'if':
            cond = EVAL(ast[1], env)
            if cond is None or cond is False:
                if len(ast) > 3:
                    ast = ast[3]
                else:
                    ast = None
            else:
                ast = ast[2]
            # TCO
        elif ast[0] == 'fn*':
            return fn(EVAL, ast[1], ast[2], env)
        else:
            l = eval_ast(ast, env)
            f = l[0]
            if hasattr(f, '__ast__'):
                ast = f.__ast__
                env = f.__env__(l[1:])
                # TCO
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


def quasiquote(ast):
    if isinstance(ast, List):
        if len(ast) == 2 and ast[0] == 'unquote':
            return ast[1]
        return qq_acc(ast)
    elif isinstance(ast, HashMap) or isinstance(ast, Symbol):
        return List([Symbol('quote'), ast])
    elif isinstance(ast, Vector):
        return List([Symbol('vec'), qq_acc(ast)])
    return ast


def qq_acc(seq):
    res = List([])
    for elt in reversed(seq):
        if isinstance(elt, List) and elt[0] == 'splice-unquote':
            res = List([Symbol('concat'), elt[1], res])
        else:
            res = List([Symbol('cons'), quasiquote(elt), res])
    return res


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
