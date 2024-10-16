def wave(people):
    result = []

    for i in range(len(people)):
        if people[i] == " ":
            continue
        elif i == 0:
            current = f"{people[i].upper()}{people[i+ 1:]}"
        elif i == len(people) - 1:
            current = f"{people[:i]}{people[i].upper()}"
        else:
            current = f"{people[:i]}{people[i].upper()}{people[i+1:]}"

        result.append(current)

    return result
  
