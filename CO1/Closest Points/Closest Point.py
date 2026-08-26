import math

# Ambulance locations
points = [
    ("Ambulance A", 2, 3),
    ("Ambulance B", 5, 4),
    ("Ambulance C", 1, 1),
    ("Ambulance D", 6, 7),
    ("Ambulance E", 3, 2)
]

# Function to calculate distance
def distance(point1, point2):
    x1, y1 = point1[1], point1[2]
    x2, y2 = point2[1], point2[2]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Find closest pair
min_distance = float("inf")
closest_pair = None

for i in range(len(points)):
    for j in range(i + 1, len(points)):

        current_distance = distance(points[i], points[j])

        if current_distance < min_distance:
            min_distance = current_distance
            closest_pair = (points[i], points[j])


# Display result
print("Closest Pair of Ambulances")
print("--------------------------")

print(
    closest_pair[0][0],
    "->",
    (closest_pair[0][1], closest_pair[0][2])
)

print(
    closest_pair[1][0],
    "->",
    (closest_pair[1][1], closest_pair[1][2])
)

print("Minimum Distance:", round(min_distance, 3))