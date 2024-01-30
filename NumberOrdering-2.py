from re import A


print(f'Enter three numbers!\n')

#Input Numbers
a = input('Number one:')
b = input('Number two:')
c = input('Number three:\n')

#Defining Order for Numbers
mini, mid, maxi = 0,0,0

try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a>b and a>c:
        if b>c:
            mini, mid, maxi = c, b, a
    else:
        mini, mid, maxi = b, c, a
    if b>a and b>c:
        if a>c:
            mini, mid, maxi = c, a, b
    else:
        mini, mid, maxi = a, c, b
    if c>a and c>b:
        if a>b: 
            mini, mid, maxi = b, a, c
    else:
        mini, mid, maxi = a, b, c
    if a >= 0 and b >= 0 and c>= 0:
        print(f'Your numbers are positive!')
        print("Asceding Ordering:", mini, mid, maxi)
    else:
        print(f'Error! You have negative values!')

except: 
 print(f'Error! You have string values!')
