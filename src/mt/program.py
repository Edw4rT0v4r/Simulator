import re
import time

import colorama
from colorama import Fore, Back

from src.mt.dictionary import *

colorama.init(autoreset=True)


def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)


def print_result(data):
    for x, z in data.items():
        data[x] = z if escape_ansi(z) != '_' else ' '
    print('\n')
    print(' '.join(map(str, data.values())))


def mt(q='0', v='_', n_v='_', position=0, n_q='0', a=None):
    aux_p = position
    aux_v = v

    if a is None:
        a = {}
    if v == ' ':
        v = '_'

    if (q, v) in d.keys():
        v = v
    elif (q, '*') in d.keys():
        v = '*'

    if (q, v) in d.keys():
        n_v = d[q, v][0]
        if n_v == '*':
            n_v = aux_v
        po = d[q, v][1]
        n_q = d[q, v][2]
        if po == 'r':
            position += 1
        else:
            position -= 1
    elif q in F:
        print_result(a)
        print('\nHalted in state ' + q)
        return
    else:
        print_result(a)
        print('No rule for state ' + q + ' and symbol ' + v)
        return

    w = False
    if position in a.keys():
        v = escape_ansi(a[position])
    else:
        v = '_'
        w = True

    for f, g in a.items():
        a[f] = Fore.WHITE + escape_ansi(g)

    if w is False:
        a[aux_p] = Fore.WHITE + n_v
        a[position] = Fore.RED + v
    else:
        a[aux_p] = Back.BLACK + Fore.WHITE + n_v
        if v == '_':
            v = ' '
        a[position] = Back.RED + Fore.RED + v

    a = {k: a[k] for k in sorted(a)}

    print(' '.join(map(str, a.values())))

    time.sleep(0.1)

    mt(n_q, v, n_v, position, n_q, a)
