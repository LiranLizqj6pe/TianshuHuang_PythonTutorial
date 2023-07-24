area = int(input('Rectangle Area: '))
print(f'Check from 1 to {area}')
print('Stop when height is greater than width')
for height in range (1, area+1):
    width = int(area / height)
    if height > width:
        break
    if area % height == 0:
        print (f'{height}x{width}')