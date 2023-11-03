from typing import List
def majorityElement(v: List[int]) -> List[int]:
    n = len(v) # size of the list
    ls = [] # list of answers

    for i in range(n):
        # selected element is v[i]:
        # Checking if v[i] is not already
        # a part of the answer:
        if len(ls) == 0 or ls[0] != v[i]:
            cnt = 0
            for j in range(n):
                # counting the frequency of v[i]
                if v[j] == v[i]:
                    cnt += 1

            # check if frquency is greater than n/3:
            if cnt > (n // 3):
                ls.append(v[i])

        if len(ls) == 2:
            break

    return ls

arr = [11, 33, 33, 11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()

