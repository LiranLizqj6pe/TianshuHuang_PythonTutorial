def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


i = int(input("Please enter an integer: "))
while i != 1:
    i = collatz(i)
print(i)

