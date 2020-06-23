from src.afd.dictionary import *


def afd(q='0', data=None):
    if data is None:
        data = []
    for sym in data:
        q = d[q, sym]
    return q in F
