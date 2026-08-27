1.Objective:

To find the closest pair of points among a set of ambulance locations using the Closest Pair of Points algorithm.

2.Algorithm:

1.Start.

2.Store the coordinates of all ambulance locations.

3.Calculate the distance between pairs of points.

4.Keep track of the minimum distance found.

5.Compare all relevant pairs.

6.Identify the two points having the smallest distance.

7.Display the closest points and their distance.

8.Stop.

3.Input:

Ambulance A → (2, 3)
Ambulance B → (5, 4)
Ambulance C → (1, 1)
Ambulance D → (6, 7)
Ambulance E → (3, 2)

4.Output:

Closest pair of ambulances:
Ambulance A (2, 3)
Ambulance E (3, 2)

Minimum distance: 1.414

The distance is calculated using:
$$ d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2} $$

Time Complexity
If we compare every pair directly:

5.Time Complexity: O(n²)

A more efficient Divide and Conquer Closest Pair algorithm can achieve:
Time Complexity: O(n log n)
