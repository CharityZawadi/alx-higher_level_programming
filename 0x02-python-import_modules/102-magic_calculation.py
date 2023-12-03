def magic_calculation(a, b):
    add = 0
    sub = ('add', 'sub')

    if a < b:
        c = a + b
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub[1](a, b)

