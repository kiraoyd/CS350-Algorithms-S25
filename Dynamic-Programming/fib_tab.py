#fib(n) = fib(n-1)  + fib (n-2)
#base cases: fib(1) = 1, fib(2) = 1  assuming no fib(0) exists
def fib_tab(n, table):
    #set my index tracker at the smallest unsolved subproblem
    index = 3 #ignoreing index 0
    while index <= n:
        table[index] = table[index - 1] + table[index - 2]
        index += 1

    #when we breaks I have my answer in table[index - 1]
    return table[n]

def main():
    num = 60
    table = [-1] * (num+1) #account for the 0-index
    #populate base cases
    table[1] = 1
    table[2] = 1

    print(fib_tab(num, table))

main()
