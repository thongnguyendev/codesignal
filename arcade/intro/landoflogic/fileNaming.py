def fileNaming(names):
    for i in range(1, len(names)):
        n = names[i]
        c = 0
        while n in names[:i]:
            c += 1
            n = names[i] + "(" + str(c) + ")"
        names[i] = n
    return names
