from mal_types import AstAndBracketType
from my_parser import keywords_map


def pr_str(element, print_readbly=False):
    if type(element).__name__ == AstAndBracketType.__name__:
        return pr_list(element)
    else:
        return pr_atom(element, print_readbly)


def pr_atom(atom, print_readbly):
    parsedAtom = next((key for key in keywords_map.keys()
                       if keywords_map[key] is atom), None)

    return parsedAtom if parsedAtom else \
        str(atom).encode().decode('unicode_escape') if print_readbly else str(atom)


def pr_list(ast_listtype):
    result = ast_listtype.list_type.left_bracket
    for i, x in enumerate(ast_listtype.ast):
        result += pr_str(x) + \
                  (' ' if i < len(ast_listtype.ast) - 1 else '')
    return result + ast_listtype.list_type.right_bracket
