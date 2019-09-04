def evenDigitsOnly(n):
    a = list(map(int, set(str(n))))
    return len([x for x in a if x % 2 == 1]) == 0
