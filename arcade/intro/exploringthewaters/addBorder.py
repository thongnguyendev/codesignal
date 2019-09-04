def addBorder(picture):
    borderLen = len(picture[0]) + 2
    top = ''.join(['*' for i in range(borderLen)])
    result = ["*" + s + "*" for s in picture]
    return [top, *result, top]
