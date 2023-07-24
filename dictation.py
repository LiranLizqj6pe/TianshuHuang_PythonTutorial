key1 = ['python', 'c', 'java']
value1 = [100, 80, 90]
dic1 = dict(zip(key1, value1))
dic1['python'] = 95
dic1.pop('c')
dic1.setdefault('c++', 85)
print(dic1)
