nums = [ 3, 6, 7,5, 53, 3,3,4,5 ,667,5, 4, 3, 2, 1]

def Insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    print(nums)
    
Insertion_sort(nums)