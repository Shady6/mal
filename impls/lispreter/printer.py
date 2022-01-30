def pr_str(element):
    if type(element).__name__ == 'list':
        return pr_list(element)
    else:
        return pr_atom(element)


def pr_atom(atom):
    parsedAtom = next((key for key in keywords_map.keys()
                       if keywords_map[key] is atom), None)
    return parsedAtom if parsedAtom else str(atom)


def pr_list(list):
    result = '('
    for i, x in enumerate(list):
        result += pr_str(x) + \
            (' ' if i < len(list) - 1 else '')
    return result + ')'


keywords_map = {
    'true': True,
    'false': False,
    'nil': None
}
