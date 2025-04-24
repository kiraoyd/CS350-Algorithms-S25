def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib (n-2)

def main():
    num = 60
    fibnum = fib(num)
    print(f"{num} fib number is: {fibnum}")

main()