


def triplet(n, arr):
    st = set()

    # check all possible triplets:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))

    # store the set elements in the answer:
    ans = [list(item) for item in st]
    return ans


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    ans = triplet(n, arr)
    for it in ans:
        print("[", end="")
        for i in it:
            print(i, end=" ")
        print("]", end=" ")
    print("\n")
