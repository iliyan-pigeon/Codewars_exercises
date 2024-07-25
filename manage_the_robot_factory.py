from math import ceil


def calculate_scrap(scraps, number_of_robots):
    one_robot_material = 50

    for i in scraps:
        one_robot_material /= (1 - i / 100)
        
    result = ceil(one_robot_material * number_of_robots)
    
    return result
