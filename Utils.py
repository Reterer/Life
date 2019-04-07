# -*- coding: utf-8 -*-


def bordered(title, body):
    lines = body.splitlines()
    width = max(len(s) for s in lines)
    res = ['╒═' + title + '═' * (width - len(title) - 1) + '╕']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('╘' + '═' * width + '╛')
    return '\n'.join(res)
