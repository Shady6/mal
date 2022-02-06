from dataclasses import dataclass


class ParseError(Exception): pass


@dataclass
class Symbol:
    val: any


@dataclass
class MalBrackets:
    left_bracket: str
    right_bracket: str


class List(list): pass


class Vector(list): pass


class HashMap(list): pass


list_types = [List, Vector, HashMap]

regular_bracket = MalBrackets('(', ')')
square_bracket = MalBrackets('[', ']')
curly_bracket = MalBrackets('{', '}')

list_type_bracket_map = {
    List.__name__: regular_bracket,
    Vector.__name__: square_bracket,
    HashMap.__name__: curly_bracket
}
