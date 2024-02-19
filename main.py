def my_cook_book():
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


def get_products_from_cook_li(cook_book):
    products = []
    for dish_name in cook_book:
        for ingredient in cook_book[dish_name]:
            if ingredient['ingredient_name'] not in products:
                products.append(ingredient['ingredient_name'])
    return products


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
    return shop_list


import os

import os

import os

def merge_files(files):
    """
    Функция объединяет файлы в один, сортируя их по количеству строк.

    :param files: Список файлов для объединения.
    :return: None
    """

    # Отфильтруем файлы с расширением txt
    txt_files = [file for file in files if file.endswith('.txt')]

    # Создадим словарь с информацией о файлах
    file_info = {}
    for file in txt_files:
        with open(file, encoding='utf-8') as input_file:
            num_lines = len(input_file.readlines())
            file_info[file] = (num_lines, input_file.read())

    # Сортируем словарь по количеству строк
    sorted_files = sorted(file_info, key=lambda file, info=file_info[file]: info[0])

    # Запишем отсортированную информацию в выходной файл
    with open('merged_files.txt', 'w', encoding='utf-8') as output_file:
        for file in sorted_files:
            output_file.write(f'{file}\n')
            output_file.write(f'{file_info[file][0]}\n')
            output_file.write(f'{file_info[file][1]}\n\n')


if __name__ == '__main__':
    # Получим список всех файлов в текущей папке
    files = os.listdir('.')

    # Вызовем функцию для объединения файлов
    merge_files(files)
