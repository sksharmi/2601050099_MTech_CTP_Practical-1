1. Objective

To find the continuous sequence of days that gives the maximum total gain from a list of daily stock gains and losses using Kadane's Algorithm.

2. Algorithm

Start.

Take the array of daily gains/losses.
 
Initialize current_sum and max_sum with the first element.

Start traversing the array from the second element.
For each element, calculate:
current_sum = max(element, current_sum + element)
Compare current_sum with max_sum.
If current_sum is greater, update max_sum.
Continue until all elements are processed.
The max_sum represents the maximum possible sum of a continuous subarray.
Display the maximum subarray and its sum.
Stop.

4. Input
Daily stock gains/losses:
[-2, 3, -1, 5, -6, 4, 2]

5. Output
Maximum Subarray: [3, -1, 5]
Maximum Gain: 7

Because:
3 + (-1) + 5 = 7

5. Time Complexity
Time Complexity: O(n)
Space Complexity: O(1)

Kadane's Algorithm is efficient because it scans the array only once.
