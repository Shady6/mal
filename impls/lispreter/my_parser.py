import re
from typing import List

from mal_types import brackets, AstAndBracketType

pattern = re.compile(
    r'[\s,]*(~@|[\[\]{}()\'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}(\'"`, ;)]+)')

keywords_map = {
    'true': True,
    'false': False,
    'nil': None
}


def tokenize(input: str) -> List[str]:
    return pattern.findall(input)


class MyParser:
    def __init__(self, reader):
        self.reader = reader
        self.brackets_stack = []

    def read_form(self):
        if self.reader.peek() in map(lambda x: x.left_bracket, brackets):
            self.brackets_stack.append(
                next(x for x in brackets if x.left_bracket == self.reader.peek())
            )
            return self.read_list()
        return self.read_atom()

    def read_list(self):
        ast_and_bracket_type = AstAndBracketType([], self.brackets_stack[-1])
        self.reader.next()
        while self.reader.peek() != self.brackets_stack[-1].right_bracket:
            self.validate_list_current_token()
            ast_and_bracket_type.ast.append(self.read_form())
        self.brackets_stack.pop()
        self.reader.next()
        return ast_and_bracket_type

    def read_atom(self):
        token = self.reader.next()
        if token in keywords_map.keys():
            return keywords_map[token]
        elif token.isnumeric():
            return int(token)
        return token

    def validate_list_current_token(self):
        if self.reader.peek() is None:
            raise Exception('EOF')
        elif self.reader.peek() != self.brackets_stack[-1].right_bracket \
                and self.reader.peek() in map(lambda x: x.right_bracket, brackets):
            raise Exception(f'No matching bracket for: "{self.brackets_stack[-1].left_bracket}"')
