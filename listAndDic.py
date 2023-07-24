data1 = [10, 25, 30]
data2 = [120, 150]
data1.pop(0)
data1.append(50)
data1.insert(1, 20)
data3 = data1 + data2
for index, value in enumerate(data3):
    print(f'{index}: {value}')