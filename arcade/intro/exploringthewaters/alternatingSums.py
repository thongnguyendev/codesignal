def alternatingSums(a):
    a1 = [x for i,x in enumerate(a) if i&1 == 0]
    a2 = [x for i,x in enumerate(a) if i&1 == 1]
    return [sum(a1), sum(a2)]

