from collections import deque

def burn_rope(rope, start):
    rows, cols = len(rope), len(rope[0])
    start_x, start_y = start

    # Check if the starting point is on a rope cell
    if rope[start_x][start_y] != "R":
        return -1

    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y, 0)])  # Each item is (x, y, time)
    visited = set([(start_x, start_y)])

    max_time = 0

    while queue:
        x, y, time = queue.popleft()
        max_time = max(max_time, time)

        # Try all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if within bounds and if it's a rope part that hasn't been visited
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and rope[nx][ny] == "R":
                visited.add((nx, ny))
                queue.append((nx, ny, time + 1))

    return max_time
  
