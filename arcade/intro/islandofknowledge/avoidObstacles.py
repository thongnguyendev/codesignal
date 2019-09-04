def avoidObstacles(inputArray):
    _max = max(*inputArray)
    i = 0
    while i <= _max:
        i = i + 1
        n = i
        if n > _max:
            return n
        while n <= _max:
            if n in inputArray:
                break
            n = n + i
            if n > _max:
                return i

