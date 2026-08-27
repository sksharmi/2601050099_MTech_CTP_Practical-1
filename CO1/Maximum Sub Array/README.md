1. Objective

To find the continuous sequence of days that gives the maximum total gain from a list of daily stock gains and losses using Kadane's Algorithm.

2. Algorithm

1.Start.

2.Take the array of daily gains/losses.
 
3.Initialize current_sum and max_sum with the first element.

4.Start traversing the array from the second element.

5.For each element, calculate:
current_sum = max(element, current_sum + element)

6.Compare current_sum with max_sum.
If current_sum is greater, update max_sum.

7.Continue until all elements are processed.

8.The max_sum represents the maximum possible sum of a continuous subarray.

9.Display the maximum subarray and its sum.

10.Stop.

4. Input

Daily stock gains/losses:
[-2, 3, -1, 5, -6, 4, 2]

6. Output
 
Maximum Subarray: [3, -1, 5]
Maximum Gain: 7

Because:
3 + (-1) + 5 = 7

5. Time Complexity
 
Time Complexity: O(n)
Space Complexity: O(1)

Kadane's Algorithm is efficient because it scans the array only once.
