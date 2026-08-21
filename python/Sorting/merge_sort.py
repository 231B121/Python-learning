nums = [2, 8, 5, 4, 3, 3, 6, 55, 3, 2, 23, 5, 77, 4, 3, 2, 1]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_half = nums[:mid]
    right_half = nums[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(nums))