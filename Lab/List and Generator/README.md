1. Objective

To compare list-based and generator-based processing for a large dataset by measuring their execution time and memory consumption

2. Input
   
n = 1000000

The program processes one million integers, calculates the square of each integer, and adds the results.

3.Output

The exact execution time and memory usage depend on your computer and Python environment.

Example output format:

List Result: 333332833333500000
Generator Result: 333332833333500000
List Time: (measured in seconds)
Generator Time: (measured in seconds)
List Memory: (measured in bytes)
Generator Memory: (measured in bytes)

4.Algorithm

1.Start

2.Set n = 100000

3.Record the start time.

4.Create a list of squares from 0 to n-1 and calculate their sum.

5.Calculate the time taken for list processing.

6.Record the start time again

7.Use a generator expression to calculate the sum of squares.

8.Calculate the time taken for generator processing.

9.Display both results and their execution times.

10.Stop

5. Time and Space Complexity

Let n be the number of integers processed.

Complexity	List-based	Generator-based

Time complexity	O(n)	O(n)

Auxiliary space complexity	O(n)	O(1) for the generator's processing state








