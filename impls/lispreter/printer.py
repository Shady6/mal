def pr_str(tree):
    result = '('

    for i, x in enumerate(tree):
        if type(x) == 'list':
            result += pr_str(x) + ' '

        elif len([v for v in keywords_map.values() if x is v]) == 1:
            result += next(k for k in keywords_map.keys()
                           if keywords_map[k] == x) + ' '
        else:
            result += str(x)
            if i < len(tree) - 1:
                result += ' '

    return result + ')'


keywords_map = {
    'true': True,
    'false': False,
    'nil': None
}
