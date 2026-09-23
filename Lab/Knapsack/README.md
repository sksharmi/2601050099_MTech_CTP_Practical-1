1.Objective

To find the maximum value of items that can be placed in a knapsack without exceeding its capacity using Dynamic Programming.

2.Input

Weights: [1, 3, 4]

Values: [15, 20, 30]

Capacity: 4

3.Algorithm

1.Initialize a DP array with zeros.

2.Traverse each item.

3.Check capacities from the maximum down to the item's weight.

4.Update the DP value by choosing the maximum between taking or skipping the item.

5.Return the maximum value.

4.Complexity

1.Time Complexity: O(nW)

2.Space Complexity: O(W)

Here, n is the number of items and W is the knapsack capacity.
