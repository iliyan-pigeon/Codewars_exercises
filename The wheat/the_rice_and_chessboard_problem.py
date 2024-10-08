# First solution
squares_needed = int.bit_length

# Second solution
def squares_needed(grains):
    if grains < 1:
        return 0
    else:
        return 1 + squares_needed(grains // 2)

  #Third solution
  def the_squares_needed(grains):
    grains_count = 1
    moves = 0

    while grains_count <= grains:
        grains_count *= 2
        moves += 1

    return moves
