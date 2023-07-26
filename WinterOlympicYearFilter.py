def olympic_year_w(y):
    if y % 4 == 2:
        return True
    else:
        return False


year = [i for i in range(1994, 2095)]

print(list(filter(olympic_year_w, year)))
