a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c
if d < 0:
    print('нет корней')
else:
    print((-b+d**0.5)/(2*a), (-b-d**0.5)/(2*a))
