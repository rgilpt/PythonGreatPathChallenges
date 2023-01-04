PLAYED = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def store_result(i, j, m, n):
    if m > n:
        PLAYED[i-1][j-1] += 1
    elif m < n:
        PLAYED[j - 1][i - 1] += 1
    else:
        PLAYED[j - 1][j - 1] += 1
        PLAYED[i - 1][i - 1] += 1


def main():

    store_result(2, 3, 6, 1)
    store_result(1, 3, 1, 3)
    store_result(2, 3, 1, 1)
    store_result(3, 4, 0, 1)
    store_result(1, 4, 0, 0)

    store_result(2, 3, 1, 0)
    store_result(1, 3, 0, 2)
    store_result(2, 3, 4, 2)
    store_result(3, 4, 1, 1)
    store_result(1, 4, 1, 1)
    print(PLAYED)


main()