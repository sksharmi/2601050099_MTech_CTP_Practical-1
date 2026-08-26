# Binary Search for a Book

# Books arranged in increasing order
books = list(range(1, 1000001))

# Book to be searched
target = 75000

# Initial positions
low = 0
high = len(books) - 1

found = False

while low <= high:

    # Find middle position
    mid = (low + high) // 2

    # Check if the middle book is the target
    if books[mid] == target:
        print("Book", target, "exists.")
        print("Book location: Position", mid + 1)
        found = True
        break

    # Search in the right half
    elif books[mid] < target:
        low = mid + 1

    # Search in the left half
    else:
        high = mid - 1


# If book is not found
if not found:
    print("Book", target, "does not exist.")