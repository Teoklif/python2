coins = int(input())
k = 0
for i in range(coins):
    coins_side = int(input())
    if coins_side == 1:
        k += 1
print(f'{k if k<coins/2 else coins-k}')



