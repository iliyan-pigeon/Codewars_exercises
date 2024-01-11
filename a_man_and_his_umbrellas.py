def min_umbrellas(weather):
    umbrellas_needed = 0

    for i in range(len(weather)):
        if i % 2 == 0:
            if weather[i] == 'rainy' or weather[i] == 'thunderstorms':
                umbrellas_needed += 1
        else:
            if weather[i] == 'rainy' or weather[i] == 'thunderstorms':
                if not weather[i-1] == 'rainy' or not weather[i-1] == 'thunderstorms':
                    umbrellas_needed += 1

    return umbrellas_needed