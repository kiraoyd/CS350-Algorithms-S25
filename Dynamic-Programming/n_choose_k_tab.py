
def n_choose_tab(n, k, table):
    #start at the smallest unsolved subproblem at table[3][2]
    row = 3
    while row <= n:
        col = 2
        while col <= k:
            table[row][col] = table[row-1][col-1] + table[row-1][col]
            col +=1
        row += 1

    return table[row-1][col-1]
    #return table[n][k]

def main():
    n = 40
    k = 17

    #create table
    table = [[0]*(k+1) for _ in range(n+1)]

    #initialize table
    #fill in the base cases!

    #fill down the left most column  (k==0)
    row_max = n
    col = 0
    row = 0
    while row <= row_max:
        table[row][col] = 1
        row += 1

    #fill down the diagonal (k==n)
    col_max = k
    row = 0
    col = 0
    while col <=col_max:
        table[row][col] = 1
        row += 1
        col += 1

    #fill down the second column (k==1)
    row_max = n
    col = 1
    row = 0
    while row <= row_max:
        table[row][col] = row
        row += 1

    print(n_choose_tab(n, k, table))


main()