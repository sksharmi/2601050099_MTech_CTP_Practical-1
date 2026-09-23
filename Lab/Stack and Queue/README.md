Stack and Queue Using Python

1. Objective

To implement Stack and Queue data structures using Python classes, type hints, and data classes.

2. Input
   
Stack elements: 10, 20

Queue elements: 10, 20

3. Output
    
Stack pop: 20

Queue dequeue: 10

4. Algorithm

 1.Stack:

 1.1 Create an empty stack.
 
 1.2 Insert elements using push().
 
 1.3 Remove the last inserted element using pop().
 
 1.4 Display the removed element.

2.Queue:

2.1 Create an empty queue.

2.2 Insert elements using enqueue().

2.3 Remove the first inserted element using dequeue().

2.4 Display the removed element.

5. Time Complexity

Operation	Time Complexity

Stack push	O(1) amortized

Stack pop	O(1)

Queue enqueue	O(1)

Queue dequeue (using list)	O(n)

6. Space Complexity

O(n) for storing n elements in the data structure.
