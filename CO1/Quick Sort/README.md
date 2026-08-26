Objective

To arrange the products in ascending order of price using the Quick Sort algorithm.

Algorithm
Start.
Select an element as the pivot.
Compare the prices of other products with the pivot.
Place products with lower prices on the left side of the pivot.
Place products with higher prices on the right side of the pivot.
Recursively apply Quick Sort to the left and right portions.
Combine the sorted portions.
Display the products in ascending order of price.
Stop. 

Input
Laptop      - ₹55000
Headphones  - ₹2000
Keyboard    - ₹1200
Mobile      - ₹25000
Mouse       - ₹800

Output
Mouse       - ₹800
Keyboard    - ₹1200
Headphones  - ₹2000
Mobile      - ₹25000
Laptop      - ₹55000

Time Complexity
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n²)
Space Complexity: O(log n) average case for recursive calls.
