def high_and_low(numbers):
    sorted_numbers = [int(i) for i in sorted(numbers.split(" "))]
    print(sorted_numbers)
    highest = sorted_numbers[-1]
    lowest = sorted_numbers[0]
    highest_lowest = f"{highest} {lowest}"
    return highest_lowest
  
