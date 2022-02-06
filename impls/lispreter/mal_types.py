from dataclasses import dataclass

from env import Env


class ParseError(Exception): pass


@dataclass
class HashMapKey:
    val: str


class Symbol(str): pass


@dataclass
class MalBrackets:
    left_bracket: str
    right_bracket: str


class List(list):
    def __getitem__(self, i):
        if type(i) == slice:
            return List(list.__getitem__(self, i))
        elif i >= len(self):
            return None
        else:
            return list.__getitem__(self, i)

    def __getslice__(self, *a):
        return List(list.__getslice__(self, *a))


class Vector(list): pass


class HashMap(dict): pass


def _HashMap(_list):
    hm = HashMap()
    for i in range(0, len(_list), 2):
        key = _list[i] if isinstance(_list[i], HashMapKey) else _list[i]
        hm[key] = _list[i + 1]
    return hm


list_types = [List, Vector, HashMap]

regular_bracket = MalBrackets('(', ')')
square_bracket = MalBrackets('[', ']')
curly_bracket = MalBrackets('{', '}')

list_type_bracket_map = {
    List.__name__: regular_bracket,
    Vector.__name__: square_bracket,
    HashMap.__name__: curly_bracket
}


def fn(EVAL, params, ast, env):
    def _fn(*args):
        fnEnv = Env(env, params, List(args))
        return EVAL(ast, fnEnv)

    return _fn
