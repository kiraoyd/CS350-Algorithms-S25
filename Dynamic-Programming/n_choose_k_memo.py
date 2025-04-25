def n_choose_memo(n, k, table):
    if table[n][k] != -1:
        return table[n][k]

    #if I need to do the work
    if k == 0:
        return 1
    if k == 1:
        return n
    if k == n:
        return 1

    table[n][k] = n_choose_memo(n-1, k-1, table) + n_choose_memo(n-1, k, table)
    return table[n][k]

def main():
    n = 40
    k = 17
    table = [[-1]*(k+1) for _ in range(n+1)]
    print(n_choose_memo(n, k, table))

main()


