strings = ["apple", "banana", "orange", "banana", "grape", "banana", "kiwi"]
target = "banana"
count = 0
for s in strings:
    if s == target:
        count += 1
print(count)