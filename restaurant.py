menu = ['Ramen', 'Hamburger', 'Pasta']
price = [800, 1000, 900]
menu_list = dict(zip(menu, price))
for key, value in menu_list.items():
    print(key, value)
print(f'Total Price is {sum(menu_list.values())}')