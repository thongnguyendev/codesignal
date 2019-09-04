def knapsackLight(value1, weight1, value2, weight2, maxW):
    if maxW >= weight1 + weight2:
        return value1 + value2
    a = sorted([[value1, weight1], [value2, weight2]], key=lambda x: x[0], reverse=True)
    b = list([x[0] for x in a if maxW >= x[1]])
    return 0 if len(b) == 0 else b[0]
