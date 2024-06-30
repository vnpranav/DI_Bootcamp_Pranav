def bubble_sort(nums: list):
   for i in range(len(nums)):
      for j in range(len(nums) - 1 - i):
         if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
   return nums

print(bubble_sort([1,2,4,10,11,12]))