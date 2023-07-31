def cakes(recipe, available):
    cakes_baked = 0
    enough_quantity = True

    while enough_quantity:
        for ingredient, amount in recipe.items():
            if ingredient not in available:
                enough_quantity = False
                break

            if amount > available[ingredient]:
                enough_quantity = False
                break

        if enough_quantity:
            for ingredient, amount in recipe.items():
                available[ingredient] -= amount

            cakes_baked += 1

    return cakes_baked


cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
