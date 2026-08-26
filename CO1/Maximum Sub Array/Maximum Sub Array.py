# ==========================================
#       MAXIMUM SUBARRAY
#       Stock Market Example
# ==========================================

# Daily stock gains/losses
arr = [-2, 3, -1, 5, -6, 4, 2]

# Initialize values
current_sum = arr[0]
max_sum = arr[0]

# Variables to track the subarray
start = 0
end = 0
temp_start = 0

# Kadane's Algorithm
for i in range(1, len(arr)):

    # Decide whether to start a new subarray
    # or continue the existing one
    if arr[i] > current_sum + arr[i]:
        current_sum = arr[i]
        temp_start = i
    else:
        current_sum = current_sum + arr[i]

    # Update maximum sum
    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i


# Get the maximum subarray
maximum_subarray = arr[start:end + 1]


# Display result
print("Daily Stock Gains/Losses:")
print(arr)

print("\nMaximum Subarray:")
print(maximum_subarray)

print("Maximum Gain:")
print(max_sum)