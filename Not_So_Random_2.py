def not_so_random(b,w):
  return ['White', 'Black'][b % 2]


print(not_so_random(1, 1))
print(not_so_random(6, 9))
print(not_so_random(11111, 22222))