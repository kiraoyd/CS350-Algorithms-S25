#f(n,k) = f(n-1, k-1) + f(n-1, k)

def n_choose(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if k == n:
        return 1

    return n_choose(n-1, k-1) + n_choose(n-1, k)

def main():
    n = 40
    k = 17
    print(n_choose(n, k))

main()
