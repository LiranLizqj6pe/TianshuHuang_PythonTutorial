import math
area = int(input('Rectangle Area:'))
sq = int(math.sqrt(area))
print(f'Check from 1 to {sq}')
for height in range (1,sq+1):
    if area % height == 0:
        width = int(area/height)
        print(f'{height}x{width}')