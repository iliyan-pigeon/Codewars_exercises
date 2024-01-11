def min_umbrellas(weather):
    umbrellas_needed = 0
    umbrellas_home = 0
    umbrellas_at_work = 0

    for i in range(len(weather)):
        if i % 2 == 0:
            if weather[i] == 'rainy' or weather[i] == 'thunderstorms':
                if umbrellas_home > 0:
                    umbrellas_home -= 1
                umbrellas_at_work += 1
        else:
            if weather[i] == 'rainy' or weather[i] == 'thunderstorms':
                if umbrellas_at_work > 0:
                    umbrellas_at_work -= 1
                umbrellas_home += 1

    umbrellas_needed = umbrellas_home + umbrellas_at_work
    return umbrellas_needed


print(min_umbrellas(["rainy", "rainy", "rainy", "rainy"]))