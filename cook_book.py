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
print(cook_book)
