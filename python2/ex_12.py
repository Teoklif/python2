sum = int(input())
prod = int(input())
#x^2 - sum*x + prod = 0
D = sum**2 - 4*prod
print(f'{D}')

x1 = int((sum+D**(0.5))/2)
x2 = 0
while x1+x2 != sum:
    x2 += 1

print(f'{x1}, {x2}')
