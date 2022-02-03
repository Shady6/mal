from collections import namedtuple
from dataclasses import dataclass

@dataclass
class Symbol:
    val: any

@dataclass
class MalBrackets:
    left_bracket: str
    right_bracket: str


regular_bracket = MalBrackets('(', ')')
square_bracket = MalBrackets('[', ']')
curly_bracket = MalBrackets('{', '}')
brackets = [regular_bracket, square_bracket, curly_bracket]

AstAndBracketType = namedtuple('AstAndBracketType', ['ast', 'bracket_type'])
