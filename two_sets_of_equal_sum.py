def divide_into_two_sets(n):
    total_sum = n * (n + 1) // 2
    
    if total_sum % 2 != 0:
        return []
    
    target = total_sum // 2
    set1 = []
    set2 = []
    
    current_sum = 0
    for num in range(n, 0, -1):
        if current_sum + num <= target:
            set1.append(num)
            current_sum += num
        else:
            set2.append(num)
    
    return [set1, set2]

# Example Usage:
n = 8
result = divide_into_two_sets(n)
print(result)
