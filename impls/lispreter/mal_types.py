from dataclasses import dataclass


class ParseError(Exception): pass


@dataclass
class HashMapKey:
    val: str


@dataclass
class Symbol:
    val: any


@dataclass
class MalBrackets:
    left_bracket: str
    right_bracket: str


class List(list): pass


class Vector(list): pass


class HashMap(dict): pass


def _HashMap(_list):
    hm = HashMap()
    for i in range(0, len(_list), 2):
        key = _list[i].val if isinstance(_list[i], HashMapKey) else _list[i]
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
