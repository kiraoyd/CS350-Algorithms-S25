def fib(n, table):
    if table[n] != -1:
        return table[n]

    table[n] = fib(n-1, table) + fib (n-2, table)
    return table[n]

def main():
    num = 60
    table = [-1] * (num+1) #account for the 0-index
    #populate base cases
    table[1] = 1
    table[2] = 1

    fibnum = fib(num, table)
    print(f"{num} fib number is: {fibnum}")

main()