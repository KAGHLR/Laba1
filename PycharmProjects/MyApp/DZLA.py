a, b, c = float(input()), float(input()),float(input())
d = b**2 - 4*(a*c)
if d>0:
    x1 = (-1 * b + d**0.5)/2
    x2 = (-1 * b - d**0.5)/2
    print(x1,x2)
elif d == 0:
    x = (-1 * b)/2
    print(x)
else:
    print('korney net')