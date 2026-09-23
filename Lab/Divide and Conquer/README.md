Merge Sort Using Divide and Conquer

1. Objective

To implement the Merge Sort algorithm in Python using the Divide and Conquer technique to sort a list of elements in ascending order.

2. Input

A list of unsorted integers.

Example:

[38, 27, 43, 3, 9, 82, 10]

3. Output

The list of integers arranged in ascending order.

Example:

[3, 9, 10, 27, 38, 43, 82]

4. Algorithm

1.Start

2.If the array has zero or one element, return it because it is already sorted.

3.Find the middle index of the array.

4.Divide the array into a left half and a right half.

5.Recursively apply Merge Sort to the left half.

6.Recursively apply Merge Sort to the right half.

7.Merge the two sorted halves:

8.Compare the first unmerged elements of both halves.

9.Append the smaller element to the result.

10.Continue until one half has no remaining elements.

11.Append any remaining elements from the other half.

12.Return the merged, sorted array.

13.Stop

5. Time Complexity

The recurrence relation for Merge Sort is:

T(n) = 2T(n/2) + O(n)

Best case: O(n log n)

Average case: O(n log n)

Worst case: O(n log n)

At each level of recursion, merging takes O(n) time. The array is divided into halves for approximately log₂ n levels. Therefore, the total time complexity is O(n log n).

6. Space Complexity

Auxiliary space complexity: O(n)

Additional storage is used to merge the elements into temporary result lists.

7. Conclusion

Merge Sort sorts elements by repeatedly dividing the list into smaller sublists, sorting them recursively, and merging the sorted sublists. It guarantees O(n log n) time complexity in the best, average, and worst cases.
