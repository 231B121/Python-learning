nums = [2, 8, 5, 4, 3, 3, 6, 55, 3, 2, 23, 5, 77, 4, 3, 2, 1]


class Solution:

    def quickSort(self, arr, low, high):
        if low < high:
            pivot_id = self.partition(arr, low, high)

            self.quickSort(arr, low, pivot_id - 1)
            self.quickSort(arr, pivot_id + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]

        i = low
        j = high

        while i < j:

            while i <= high - 1 and arr[i] <= pivot:
                i += 1

            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        return j


solution = Solution()

solution.quickSort(nums, 0, len(nums) - 1)

print(nums)