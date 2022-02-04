import re

from mal_types import HashMap, List, Symbol, regular_bracket, square_bracket, curly_bracket, Vector

pattern = re.compile(
    r'[\s,]*(~@|[\[\]{}()\'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}(\'"`, ;)]+)')


def tokenize(_input):
    return pattern.findall(_input)


def read_form(reader):
    if reader.peek() == ';':
        return None
    elif reader.peek() == ')':
        raise Exception('Unexpected bracket: ")"')
    elif reader.peek() == '(':
        return read_list(reader, regular_bracket, List)
    elif reader.peek() == ']':
        raise Exception('Unexpected bracket: "]"')
    elif reader.peek() == '[':
        return read_list(reader, square_bracket, Vector)
    elif reader.peek() == '}':
        raise Exception('Unexpected bracket: "}"')
    elif reader.peek() == '{':
        return read_list(reader, curly_bracket, HashMap)

    return read_atom(reader)


def read_list(reader, bracket_type, list_type):
    ast = list_type()
    reader.next()
    while reader.peek() != bracket_type.right_bracket:
        if reader.peek() is None:
            raise Exception('EOF')
        ast.append(read_form(reader))
    reader.next()
    return ast


def read_atom(reader):
    token = reader.next()
    if token == 'true':
        return True
    elif token == 'false':
        return False
    elif token == 'nil':
        return None
    elif re.match(r'^-?[0-9]+$', token):
        return int(token)
    elif re.match(r'^-?[0-9]\.[0-9]*$', token):
        return float(token)
    elif token.startswith('"'):
        return parse_string(token)
    return Symbol(token)


def parse_string(string):
    if not string.endswith('"') or len(string) == 1 or not re.match(r'^"(?:\\.|[^\\"])*"$', string):
        raise Exception(f'No matching closing double quotation for string {string[1:]}')
    return string
