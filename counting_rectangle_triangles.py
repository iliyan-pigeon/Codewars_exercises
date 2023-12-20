from itertools import combinations

def count_rect_triang(points):
    def is_right_angle(p1, p2, p3):
        # Calculate distances between points
        distances = [
            (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2,
            (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2,
            (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
        ]
        distances.sort()  # Sort distances

        # Check if it forms a right-angled triangle
        return distances[0] + distances[1] == distances[2]

    # Get unique points
    unique_points = list(set(map(tuple, points)))

    count = 0
    # Check all combinations of 3 unique points
    for p1, p2, p3 in combinations(unique_points, 3):
        if is_right_angle(p1, p2, p3):
            count += 1

    return count

# Test cases
print(count_rect_triang([[1, 2],[3, 3],[4, 1],[1, 1],[4, -1]]))  # Output: 3
print(count_rect_triang([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]))  # Output: 3