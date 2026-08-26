1. Objective

To find whether book number 75,000 exists among 10,00,000 books arranged in increasing order and, if it exists, determine its location using Binary Search.

2. Algorithm
Start.
Set low = 1 and high = 10,00,000.
Set the target book number as 75000.
Find the middle position using:
mid = (low + high) // 2
Compare the book number at mid with 75000.
If it is equal to 75000, the book is found. Display its location.
If it is less than 75000, search the right half by setting low = mid + 1.
If it is greater than 75000, search the left half by setting high = mid - 1.
Repeat steps 4–8 until the book is found or low > high.
If low > high, display that the book does not exist.
Stop.
3. Input
Number of books = 10,00,000
Books = 1, 2, 3, 4, ..., 10,00,000
Book to be searched = 75,000
4. Output
Book 75000 exists.
Book location: Position 75000
5. Time Complexity
Best Case: O(1)
Average Case: O(log n)
Worst Case: O(log n)
Space Complexity: O(1)

For 10,00,000 books, Binary Search requires at most approximately 20 comparisons.
