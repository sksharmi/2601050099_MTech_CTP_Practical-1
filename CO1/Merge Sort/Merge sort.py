# ==========================================
#   MERGE SORT - STUDENT SCHOLARSHIP SYSTEM
# ==========================================

students = [
    ("Anitha", 95),
    ("Vivek", 83),
    ("Lakshmi", 67),
    ("Ramesh", 97),
    ("Kumar", 85)
]


# ------------------------------------------
# Merge Sort Function
# ------------------------------------------
def merge_sort(students):

    # Base condition
    if len(students) <= 1:
        return students

    # Find middle
    mid = len(students) // 2

    # Divide into two halves
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    # Merge the two halves
    return merge(left, right)


# ------------------------------------------
# Merge Function
# ------------------------------------------
def merge(left, right):

    result = []

    i = 0
    j = 0

    # Compare marks and sort in descending order
    while i < len(left) and j < len(right):

        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# ------------------------------------------
# Sort Students
# ------------------------------------------
sorted_students = merge_sort(students)


# ------------------------------------------
# Display Sorted Students
# ------------------------------------------
print("Students Sorted by Marks")
print("----------------------------")

for rank, (name, marks) in enumerate(sorted_students, start=1):
    print(f"{rank}. {name} - {marks}")


# ------------------------------------------
# Scholarship Eligibility
# ------------------------------------------
print("\nScholarship Eligible Students")
print("----------------------------")

for name, marks in sorted_students:

    if marks >= 90:
        print(f"{name} - {marks}")