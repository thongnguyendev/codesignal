def sortByHeight(a):
    b = [x for x in a if x > -1]
    b.sort()
    i = 0
    for j in range(len(a)):
        if a[j] == -1:
            continue
        a[j] = b[i]
        i = i + 1
    return a
