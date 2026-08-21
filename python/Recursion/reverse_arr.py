nums = [2, 4, 1, 7, 6, 3, 8, 9, 5]

def func(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    func(arr, left + 1, right - 1)


func(nums, 0, len(nums) - 1)


# def reverseArray(nums):
#     func(nums, 0, len(nums) - 1)
#     print(nums)


# reverseArray(nums)