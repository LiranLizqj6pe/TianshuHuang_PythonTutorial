import random as ran
num = int(input('Num: '))
coin = 0
for i in range (num):
    if ran.random() > 0.5:
        coin += 1
print(f'Total Games{num}, Coin Times{coin}')
print(f'Coin Probability{coin/num}')