from typing import List
import re

pattern = re.compile(
    r'[\s,]*(~@|[\[\]{}()\'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}(\'"`, ;)]+)')


class Reader:
    def __init__(self, tokens: List[str]):
        self.tokens = tokens
        self.position = 0

    def next(self):
        current_token = self.peek()
        if self.position < len(self.tokens):
            self.position += 1
        return current_token

    def peek(self):
        return None if self.position >= len(self.tokens) \
            else self.tokens[self.position]


def read_str(input):
    tokens = tokenize(input)
    reader = Reader(tokens)
    return read_form(reader)


def tokenize(input: str) -> List[str]:
    return pattern.findall(input)


def read_form(reader: Reader):
    return read_list(reader) if reader.peek() == '(' \
        else read_atom(reader)


def read_list(reader: Reader):
    tokens = []
    reader.next()
    while reader.peek() != ')':
        assert(reader.peek() != None)
        tokens.append(read_form(reader))
    reader.next()
    return tokens


def read_atom(reader: Reader):
    token = reader.next()
    if token == 'true':
        return True
    elif token == 'false':
        return False
    elif token == 'nil':
        return None
    elif token.isnumeric():
        return int(token)
    return token
