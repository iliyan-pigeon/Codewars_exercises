def trailing_zeros(n) ->int:
    zeros_amount = 0

    binary = str(bin(n))
    
    for i in range(len(binary)-1 , -1, -1):
        if binary[i] == "0":
            zeros_amount += 1
        else:    
            break    

    return zeros_amount
