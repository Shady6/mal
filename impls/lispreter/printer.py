from mal_types import AstAndBracketType, Symbol
from my_parser import keywords_map


def pr_str(element, print_readably=False):
    if type(element).__name__ == AstAndBracketType.__name__:
        return pr_list(element)
    else:
        return pr_atom(element, print_readably)


def pr_atom(atom, print_readbly):
    parsedAtom = next((key for key in keywords_map.keys()
                       if keywords_map[key] is atom), None)
    if parsedAtom:
        return parsedAtom
    if type(atom).__name__ == Symbol.__name__:
        return atom.val
    return str(atom).encode().decode('unicode_escape') if print_readbly else str(atom)


def pr_list(ast_and_bracket_type):
    result = ast_and_bracket_type.bracket_type.left_bracket
    for i, x in enumerate(ast_and_bracket_type.ast):
        result += pr_str(x) + \
                  (' ' if i < len(ast_and_bracket_type.ast) - 1 else '')
    return result + ast_and_bracket_type.bracket_type.right_bracket
