def my_cook_book() :
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
    return cook_book
cook_book = my_cook_book()




