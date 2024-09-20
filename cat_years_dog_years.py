def owned_cat_and_dog(cat_years, dog_years):
    converted_cat_years = 0
    converted_dog_years = 0

    if cat_years < 15:
        converted_cat_years = 0
    elif 24 > cat_years >= 15:
        converted_cat_years = 1
    elif cat_years == 24:
        converted_cat_years = 2
    elif cat_years > 24:
        cat_years_left = cat_years - 24

        converted_cat_years = 2 + (cat_years_left // 4)

    if dog_years < 15:
        converted_dog_years = 0
    elif 24 > dog_years >= 15:
        converted_dog_years = 1
    elif dog_years == 24:
        converted_dog_years = 2
    elif dog_years > 24:
        dog_years_left = dog_years - 24

        converted_dog_years = 2 + (dog_years_left // 5)

    return [converted_cat_years, converted_dog_years]
