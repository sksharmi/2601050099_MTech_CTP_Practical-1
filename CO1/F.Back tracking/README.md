N-Queens Problem Using Backtracking

Objective:

To solve the N-Queens problem using the Backtracking technique by placing N queens on an N × N chessboard such that no two queens attack each other.

Problem Statement:

The N-Queens problem requires placing N queens on an N × N chessboard.


No two queens should be in the same:

.Row

.Column

.Diagonal

.Input

An integer N representing the number of queens.

Example:
N = 4

Algorithm:

1.Start from the first row.

2.Try placing a queen in each column.

3.Check whether the position is safe.

4.If the position is safe, place the queen.

5.Move to the next row.

6.If no safe position is available, backtrack.

7.Remove the previously placed queen.

8.Try another position.

9.Continue until all N queens are placed.

Output:

For N = 4, one possible solution is:

. Q . .
. . . Q
Q . . .
. . Q .

Where:

Q represents a queen.
. represents an empty position.
Backtracking

If placing a queen results in an invalid configuration, the algorithm removes the queen and goes back to the previous row.
It then tries another possible position.
Place → Check → If invalid, go back → Try another position

Time Complexity:

O(N!)

Space Complexity:

O(N)

Technologies Used:

Python

Backtracking

Conclusion

The N-Queens problem can be solved using backtracking by trying possible queen positions and undoing invalid choices until a valid solution is found.
