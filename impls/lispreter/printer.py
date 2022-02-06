from mal_types import Symbol, list_type_bracket_map, List, Vector, HashMap


def pr_str(ast, print_readably=False):
    if ast is True:
        return 'true'
    elif ast is False:
        return 'false'
    elif ast is None:
        return 'nil'
    elif isinstance(ast, Symbol):
        return ast.val
    elif isinstance(ast, List):
        return '(' + " ".join(map(lambda x: pr_str(x), ast)) + ')'
    elif isinstance(ast, Vector):
        return '[' + " ".join(map(lambda x: pr_str(x), ast)) + ']'
    elif isinstance(ast, HashMap):
        return '{' + " ".join(k + " " + pr_str(v) for k, v in ast.items()) + '}'
    return str(ast) if not print_readably \
        else str(ast).encode().decode('unicode_escape')


def pr_atom(atom, print_readably):
    if atom is True:
        return 'true'
    elif atom is False:
        return 'false'
    elif atom is None:
        return 'nil'
    elif isinstance(atom, Symbol):
        return atom.val
    return str(atom) if not print_readably \
        else str(atom).encode().decode('unicode_escape')


def pr_list(ast):
    result = list_type_bracket_map[type(ast).__name__].left_bracket
    for i, x in enumerate(ast):
        result += pr_str(x) + (' ' if i < len(ast) - 1 else '')
    return result + list_type_bracket_map[type(ast).__name__].right_bracket
