def commonCharacterCount(s1, s2):
    _count = 0
    for c1 in s1:
        for c2 in s2:
            if c2 == c1:
                _count += 1
                s2 = s2.replace(c2, '', 1)
                break
    return _count


def commonCharacterCount2(s1, s2):
    s = set(s1) & set(s2)
    return sum([min(s1.count(c), s2.count(c)) for c in s])
