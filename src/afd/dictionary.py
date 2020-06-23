d = {}
F = set()
message = {True: 'Aceptada', False: 'Rechazada'}


def dictionary_afd(data):
    q, s, n = data
    if '*' in q:
        q = q.strip('*')
        F.add(q)
    d[q, s] = n
