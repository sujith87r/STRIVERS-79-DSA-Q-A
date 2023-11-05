
from typing import *
def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    for num in arr:
        if num == k:
            return True
    return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    ans = searchInARotatedSortedArrayII(arr, k)
    if not ans:
        print("Target is not present.")
    else:
        print("Target is present in the array.")
