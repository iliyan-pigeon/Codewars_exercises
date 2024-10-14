from collections import Counter


def find_key(nums):
    passcode = ""
    columns_count = len(str(nums[0]))

    for i in range(columns_count):
        unique = [list(str(number))[i] for number in nums]

        count = Counter(unique)
        for num, freq in count.items():
            if freq == 1:
                passcode += str(num)

    return passcode
  
