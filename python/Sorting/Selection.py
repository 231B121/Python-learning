nums = [1,4,5,6,8 ,3, 4,5,65]
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        
        min_idx = i 
        for j in range(i+1, n):
            if nums[j] > nums[min_idx]:
                min_idx = j
        nums[i] , nums[min_idx] = nums[min_idx], nums[i]
    print(nums)
        
selection_sort(nums)