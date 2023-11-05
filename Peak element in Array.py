


def findPeakElement(arr: [int]) -> int:
    n = len(arr) # Size of the array

    for i in range(n):
        # Checking for the peak:
        if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
            return i

    # Dummy return statement
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)


