top_food = ['Sushi', 'Hamburguesa', 'HotDog', 'Torta', 'Tamales', 'Pizza', 'Subway']
for food in top_food:
    print('Current food:', food)

# Nuevo ejemplo
top_food = ['Sushi', 'Hamburguesa', 'HotDog', 'Torta', 'Tamales', 'Pizza', 'Subway']
for food_index in range(len(top_food)):
    print('Current index:', food_index, '| Current food:', top_food[food_index], )

# Otro ejemplo
spendings = [52.36, 15.23, 14.98, 78.45, 19.82]
sum = 0.0
for spendings in spendings:
    sum += spendings
print('\n''Dinero gastado: ', sum)