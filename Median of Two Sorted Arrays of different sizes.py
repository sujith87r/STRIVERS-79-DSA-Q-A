def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)

    arr3 = []
    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1

    # copy the left-out elements:
    arr3.extend(a[i:])
    arr3.extend(b[j:])

    # Find the median:
    n = n1 + n2
    if n % 2 == 1:
        return float(arr3[n // 2])

    median = (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    return median


if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))
