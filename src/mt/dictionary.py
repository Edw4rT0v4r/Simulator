d = {}
F = set()


def dictionary_mt(data):
    state, val, new_value, position, new_state = data
    if '+' in state:
        state = state.strip('+')
        F.add(state)
    if '+' in new_state:
        new_state = new_state.strip('+')
        F.add(new_state)
    d[state, val] = [new_value, position.lower(), new_state]
