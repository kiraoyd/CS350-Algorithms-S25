def coin_naiive(n):
    if n == 4 or n == 3:
        return 1
    if n <= 2:
        return n

    a = coin_naiive(n-4) #pick up 4-coin
    b = coin_naiive(n-3) # pick up the 3-coin
    c = coin_naiive(n-1) # pick up 1-coin

    min = a
    if b < min:
        min = b
    if c < min:
        min = c

    return 1 + min


#Memoized recursive solution
def coin_memo(n, table):
    if n == 0:
        return
    #Check the table, has this value for n been solved?
    if table[n] != -1:
        return table[n]

    a = coin_memo(n-4, table) #pick up 4-coin
    b = coin_memo(n-3, table) # pick up the 3-coin
    c = coin_memo(n-1, table) # pick up 1-coin

    min = a
    if b < min:
        min = b
    if c < min:
        min = c

    table[n] = 1 + min #count the coin I pick up, and the min of my kids
    return table[n]


#Iterative tabulated solution
def coin_tab(n, table):
    i = 5 #start an index tracker at the smallest, UNSOLVED subproblem

    #Keep solving each subproblem, working our way up to the biggest, n-problem
    while i <= n:
        #Look back into the table to query the earlier solved subproblems
        a = table[i-4] #pick up a 4-coin, answer to f(n-4) is at table[i-4]
        b = table[i-3] #pick up a 3-coin, answer to f(n-3) is at table[i-3]
        c = table[i-1] #pick up a 1-coin, answer to f(n-1) is at table[i-1]

        #Which previous answer is the least number of coins?
        min = a
        if b < min:
            min = b
        if c < min:
            min = c

        #DON'T FORGET: add your answer to the table to set up future generations
        table[i] = 1 + min #add one to account for the fact that we must pick up one coin at this call

        #solve the next smallest unsolved subproblem
        i = i + 1

        #After the loop finishes, the answer for n, will be stored at table[n]
    return table[n]


def main():
    n = 10
    table = [-1] * (n+1)

    #prepopulate table with base cases
    table[0] = 0
    table[1] = 1
    table[2] = 2
    table[3] = 1
    table[4] = 1

    #print(coin_naiive(n))
    #print(coin_memo(n, table))
    print(coin_tab(n, table))

main()