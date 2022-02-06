from mal_types import Symbol, List, Vector, HashMap


def _escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def pr_str(res, print_readably=True):
    if res is True:
        return 'true'
    elif res is False:
        return 'false'
    elif res is None:
        return 'nil'
    elif isinstance(res, Symbol):
        return res
    elif isinstance(res, List):
        return '(' + " ".join(map(lambda x: pr_str(x), res)) + ')'
    elif isinstance(res, Vector):
        return '[' + " ".join(map(lambda x: pr_str(x), res)) + ']'
    elif isinstance(res, HashMap):
        return '{' + " ".join(k + " " + pr_str(v) for k, v in res.items()) + '}'
    elif isinstance(res, str):
        if print_readably:
            return '"' + _escape(res) + '"'
        return res
    return res.__str__()
