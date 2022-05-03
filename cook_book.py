with open('recipe.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    key = None
    for cook in file:
        if cook != "\n":
            cook = cook.strip()
            if key == None:
                cook_book[cook] = []
                key = cook
            else:
                ingredient = cook.split(' | ')
                cook_book[key] += [
                    dict(ingredient_name=ingredient[0], quantity=int(ingredient[1]), measure=ingredient[2])]
        else:
            key = None


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dishe in dishes:
        for ingredient in cook_book[dishe]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}
    return print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Утка по-пекински'], 2)
