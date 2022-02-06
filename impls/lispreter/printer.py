from mal_types import Symbol, list_type_bracket_map


def pr_str(element, print_readably=False):
    if isinstance(element, list):
        return pr_list(element)
    else:
        return pr_atom(element, print_readably)


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
