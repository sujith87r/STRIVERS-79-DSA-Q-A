from typing import List
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)  # size of the array
    repeating, missing = -1, -1

    # Find the repeating and missing number:
    for i in range(1, n+1):
        # Count the occurrences:
        cnt = 0
        for j in range(n):
            if a[j] == i:
                cnt += 1

        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break

    return [repeating, missing]

if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers(a)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")

