def find_min_platforms(arr, dep):
    # Convert time to integers for easier comparison (e.g., 9:00 -> 900)
    arr = [int(time.replace(":", "")) for time in arr]
    dep = [int(time.replace(":", "")) for time in dep]
    
    # Sort arrival and departure times
    arr.sort()
    dep.sort()

    n = len(arr)
    i, j = 0, 0  # Pointers for arrival and departure
    platforms_needed = 0
    max_platforms = 0

    # Traverse both arrays
    while i < n and j < n:
        if arr[i] <= dep[j]:  # A train arrives before the current train departs
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:  # A train departs before the next train arrives
            platforms_needed -= 1
            j += 1

    return max_platforms

# Example usage
arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(find_min_platforms(arr, dep))  # Output: 3

arr = ["9:00", "9:40"]
dep = ["9:10", "12:00"]
print(find_min_platforms(arr, dep))  # Output: 1
