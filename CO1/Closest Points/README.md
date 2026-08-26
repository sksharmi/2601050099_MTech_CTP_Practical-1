Objective:
To find the closest pair of points among a set of ambulance locations using the Closest Pair of Points algorithm.

Algorithm:
Start.
Store the coordinates of all ambulance locations.
Calculate the distance between pairs of points.
Keep track of the minimum distance found.
Compare all relevant pairs.
Identify the two points having the smallest distance.
Display the closest points and their distance.
Stop.

Input:
Ambulance A → (2, 3)
Ambulance B → (5, 4)
Ambulance C → (1, 1)
Ambulance D → (6, 7)
Ambulance E → (3, 2)

Output:
Closest pair of ambulances:
Ambulance A (2, 3)
Ambulance E (3, 2)

Minimum distance: 1.414

The distance is calculated using:
$$ d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2} $$

Time Complexity
If we compare every pair directly:

Time Complexity: O(n²)

A more efficient Divide and Conquer Closest Pair algorithm can achieve:
Time Complexity: O(n log n)
