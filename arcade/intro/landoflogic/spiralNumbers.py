def spiralNumbers(n):
    a = [[0] * n for i in range(n)]
    v = 1
    k = l = 0
    m = n
    while k < m and l < n:
        for i in range(l, n):
            a[k][i], v = v, v + 1
        k += 1
        for i in range(k, m):
            a[i][n - 1], v = v, v + 1
        n -= 1
        if k < m:
            for i in range(n - 1, l - 1, -1):
                a[m - 1][i], v = v, v + 1
            m -= 1
        if l < n:
            for i in range(m - 1, k - 1, -1):
                a[i][l], v = v, v + 1
            l += 1
    return a
