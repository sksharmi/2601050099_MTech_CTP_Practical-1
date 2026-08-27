1.Objective:

To arrange the products in ascending order of price using the Quick Sort algorithm.

2.Algorithm:

1.Start.

2.Select an element as the pivot.

3.compare the prices of other products with the pivot.

4.Place products with lower prices on the left side of the pivot.

5.Place products with higher prices on the right side of the pivot.

6.Recursively apply Quick Sort to the left and right portions.

7.Combine the sorted portions.

8.Display the products in ascending order of price.

9.Stop. 

3.Input:

Laptop      - ₹55000
Headphones  - ₹2000
Keyboard    - ₹1200
Mobile      - ₹25000
Mouse       - ₹800

4.Output:

Mouse       - ₹800
Keyboard    - ₹1200
Headphones  - ₹2000
Mobile      - ₹25000
Laptop      - ₹55000

5.Time Complexity:

Best Case: O(n log n)

Average Case: O(n log n)

Worst Case: O(n²)

6.Space Complexity:

O(log n) average case for recursive calls.
