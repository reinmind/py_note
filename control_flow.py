# chose

def f1(pm=10):
    if 0 <= pm < 75:
        return 'fine'
    else:
        return 'bad'


# loop

def f2():
    for c in 'hello':
        if c == 'l':
            continue
        print(c + ' ')
        if c == 'l':
            break
