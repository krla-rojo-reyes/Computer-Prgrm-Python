#How many numbers we want to display
def main():
    num = input("How many Fibonacci numbers do you want?: ")
    try:
        num = int(num)
    except:
        print(f'\n{num} is an invalid input.')
    fib (num)


#Number of Fib that will be display
def fib(n):
    ls = [0, 1]
    try:
        n = int(n)
        for i in range(n):
            if len(ls) < n:
                ls.append(ls[-1] + ls[-2])
        print(ls)
    except:
        print(f'Try again!\n')
main()