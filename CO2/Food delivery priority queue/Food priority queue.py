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