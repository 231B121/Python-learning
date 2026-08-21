nums = [1,4,5,6,8 ,3, 4,5,65]
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0 ,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
    
bubble_sort(nums)