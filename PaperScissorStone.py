import random as ran
for i in range(10):
    out = ran.randint(0,2)
    if out % 3 == 0:
        print('Stone')
    elif out % 3 == 1:
        print('Scissor')
    else:
        print("Paper")