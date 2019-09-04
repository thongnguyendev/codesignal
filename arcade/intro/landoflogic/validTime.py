def validTime(time):
    t = time.split(":")
    return False if len(t) != 2 else True if 0 <= int(t[0]) <= 23 and 0 <= int(t[1]) <= 59 else False
