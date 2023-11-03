from collections import deque

def path_finder(maze):
    # Convert the input string into a 2D list for easier access.
    maze = [list(row) for row in maze.split('\n')]

    # Get the dimensions of the maze.
    N = len(maze)

    # Define the four possible directions (up, down, left, right).
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Create a queue for BFS.
    queue = deque()
    queue.append((0, 0, 0))  # (row, column, steps)

    # Mark the starting position as visited.
    maze[0][0] = 'W'

    while queue:
        row, col, steps = queue.popleft()

        # Check if we've reached the exit position.
        if row == N - 1 and col == N - 1:
            return steps

        # Explore the four possible directions.
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new position is within the maze boundaries and is an empty cell.
            if 0 <= new_row < N and 0 <= new_col < N and maze[new_row][new_col] == '.':
                # Mark the new position as visited and enqueue it with the updated step count.
                maze[new_row][new_col] = 'W'
                queue.append((new_row, new_col, steps + 1))

    # If we can't reach the exit, return False.
    return False

# Example usage:
maze = "....W.W...W\n...W......W\n...W.W....W\n.........."
result = path_finder(maze)
if result is not False:
    print(f"Minimal number of steps to exit: {result}")
else:
    print("Cannot reach the exit.")