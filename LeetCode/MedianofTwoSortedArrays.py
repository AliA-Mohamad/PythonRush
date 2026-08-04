def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    tamanho = len(nums)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        r = nums[meio-1] + nums[meio]
        return r/2.0
    else:
        return nums[meio]


print(findMedianSortedArrays([1, 3, 4, 5], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))

