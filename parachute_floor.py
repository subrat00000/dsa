def attempt(n, k):
    pf = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, k + 1):
        pf[i][0] = 0
        pf[i][1] = 1

    for j in range(1, n + 1):
        pf[1][j] = j

    for i in range(2, k + 1):
        for j in range(2, n + 1):
            low, high = 0, j
            while low + 1 < high:
                mid = (low + high) // 2
                if pf[i - 1][mid - 1] < pf[i][j - mid]:
                    low = mid
                else:
                    high = mid
            pf[i][j] = 1 + min(
                max(pf[i - 1][low - 1], pf[i][j - low]),
                max(pf[i - 1][high - 1], pf[i][j - high]),
            )

    return pf[k][n]


print(attempt(100, 2))
