from mal_types import Symbol, List, Vector, HashMap


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
