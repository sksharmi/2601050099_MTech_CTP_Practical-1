1. Objective

To implement an employee data model using a dataclass and a traditional class, and compare their implementations.

2. Input
   
Name: Ravi

Age: 25

Salary: ₹30,000

3. Output
   
Employee(name='Ravi', age=25, salary=30000.0)

Ravi 25 30000.0

4. Algorithm

1.Start.

2.Import the dataclass decorator.

3.Create an Employee dataclass with name, age, and salary attributes.

4.Create a traditional Employee2 class with the same attributes using __init__().

5.Create objects of both classes with the same employee details.

6.Display the dataclass object and the traditional class attributes.

7.Compare both implementations.

8.Stop.

5. Time Complexity

O(1) — Creating each object and accessing its fixed number of attributes takes constant time.

6. Space Complexity

O(1) — Each employee object stores a fixed number of attributes, so the memory required per object is constant.
