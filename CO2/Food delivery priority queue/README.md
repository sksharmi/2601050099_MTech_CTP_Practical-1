1. Objective

To implement a Priority Queue for food-delivery orders using Python's heapq module, so that higher-priority orders are processed before normal orders.

2. Data Structure Used

We use Python's heapq module.

heapq implements a min-heap, so the order with the smallest priority number is processed first.

Priority	Order Type

1	Emergency

2	Premium

3	Normal

3. Steps to Follow

Step 1

Import the heapq module.

Step 2

Create an empty priority queue.

Step 3

Assign a priority to each order:

Emergency → 1
Premium → 2
Normal → 3
Step 4

Insert orders using heapq.heappush().

Step 5

The order with the smallest priority value becomes the highest-priority order.

Step 6

Retrieve and remove the highest-priority order using heapq.heappop().

Step 7

Continue removing orders until the priority queue becomes empty.

4. Algorithm
: Food Priority Queue using Heap

1.Start.

2.Import the heapq module.

3.Create an empty priority queue.

4.Insert each order using heappush().

5.Assign priority values to the orders.

6.Use heappop() to retrieve the highest-priority order.

7.Display the processed order.

8.Repeat until all orders are processed.

9.Stop.

5. Example

Suppose the application receives these orders:

Emergency Order       → Priority 1
Premium Order         → Priority 2
Normal Order          → Priority 3
Emergency Order 2     → Priority 1

The processing order will be:

Emergency Order
Emergency Order 2
Premium Order
Normal Order

Because 1 is the highest priority and 3 is the lowest priority.

6. Python Code
import heapq

# Create an empty priority queue
priority_queue = []

# Insert orders
heapq.heappush(priority_queue, (1, "Emergency Order"))
heapq.heappush(priority_queue, (2, "Premium Customer Order"))
heapq.heappush(priority_queue, (3, "Normal Order"))
heapq.heappush(priority_queue, (1, "Emergency Order 2"))

# Display the orders
print("Processing Orders:")

# Retrieve highest-priority orders
while priority_queue:
    priority, order = heapq.heappop(priority_queue)
    print(order, "- Priority:", priority)

7. Output
   
Processing Orders:

Emergency Order - Priority: 1
Emergency Order 2 - Priority: 1
Premium Customer Order - Priority: 2
Normal Order - Priority: 3

9. Time Complexity
 
Insertion

heapq.heappush() takes:

O(log n)

Removal

heapq.heappop() takes:

O(log n)

Therefore:

Operation	Time Complexity

Insertion	O(log n)
Removal	O(log n)

9. Space Complexity

The heap stores all n orders.

Therefore:

Space Complexity = O(n)


Data Structure:

heapq Priority Queue

Insertion:

heappush() → O(log n)

Removal:

heappop() → O(log n)

Space Complexity:

O(n)

Main idea:

Emergency → Premium → Normal

because smaller priority numbers are processed first.
