from typing import List

from parser import tokenize, read_form


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


def read_str(_input):
    tokens = tokenize(_input)
    reader = Reader(tokens)
    try:
        return read_form(reader)
    except Exception as ex:
        return [ex]
