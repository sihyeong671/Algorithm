def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    clone_nums1 = nums1[:]

    p_1 = 0
    p_2 = 0
    idx = 0
    while True:
        if p_1 == m:
            for i in range(p_2, n):
                nums1[idx] = nums2[i]
                idx += 1
            print(nums1)
            break
        elif p_2 == n:
            for i in range(p_1, m):
                nums1[idx] = clone_nums1[i]
                idx += 1
            print(nums1)
            break
        if clone_nums1[p_1] > nums2[p_2]:
            nums1[idx] = nums2[p_2]
            p_2 += 1
            idx += 1
        else:
            nums1[idx] = clone_nums1[p_1]
            p_1 += 1
            idx += 1

# 사실 그냥 넣고 sort함수 쓰면 됨
merge([1, 2, 4, 5, 6, 0], 5, [3], 1)
