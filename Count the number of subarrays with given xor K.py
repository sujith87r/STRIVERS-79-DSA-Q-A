


def subarraysWithXorK(a: [int], b: int) -> int:
    n = len(a)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = 0
            for K in range(i, j + 1):
                xorr = xorr ^ a[K]

            # step 3: check XOR and count:
            if (xorr == k):
                cnt += 1

    return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans) 
