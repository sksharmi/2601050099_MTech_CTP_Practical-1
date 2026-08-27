1. Objective

To sort a list of students in descending order of their marks and identify the students who are eligible for a scholarship.

A student is eligible for the scholarship if their marks are greater than or equal to 90.

2. Algorithm
   
1.Start.

2.Store the names of the students and their corresponding marks.

3.Combine each student's name with their marks.

4.Sort the students in descending order of marks.

5.Traverse through the sorted list.

6.Check whether each student's marks are greater than or equal to 90.

7.If the marks are >= 90, add the student to the scholarship-eligible list.

8.Display the students in descending order of marks.

9.Display the students eligible for the scholarship.

10.Stop.

4. Input
   
Student Names
Anitha
Vivek
Lakshmi
Ramesh
Kumar
Marks
95
83
67
97
85
Scholarship Eligibility
Marks >= 90

6. Output

Students Sorted in Descending Order
Rank	Student	Marks
1	Ramesh	97
2	Anitha	95
3	Kumar	85
4	Vivek	83
5	Lakshmi	67
Scholarship-Eligible Students
Ramesh - 97
Anitha - 95

Therefore, Ramesh and Anitha are eligible for the scholarship.

5. Time Complexity

Let n be the number of students.

Sorting: O(n log n)
Checking scholarship eligibility: O(n)
Overall Time Complexity: O(n log n)

6.Space Complexity

O(n) because we store the student names, marks, and sorted list.
