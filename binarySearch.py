def binary_search(lst, n):
    l = 0
    u = len(lst) - 1
    while l <= u:
        m = (l + u) // 2
        if lst[m] == n:
            return m  # Return index if found
        elif lst[m] < n:
            l = m + 1
        else:
            u = m - 1
    return -1  # Return -1 if not found

# Take input from user
user_input = input("Enter numbers separated by spaces: ")
lst = list(map(int, user_input.split()))

# Sort the list
lst.sort()
print("Sorted list:", lst)

# Number to search
n = int(input("Enter number to search: "))

# Perform binary search
pos = binary_search(lst, n)
if pos != -1:
    print(f"Found at position {pos + 1} (index {pos})")
else:
    print("Not found")
