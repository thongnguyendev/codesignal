def digitDegree(n):
    times = 0
    while n > 9:
        n = sum(list(map(int, list(str(n)))))
        times = times + 1
    return times
