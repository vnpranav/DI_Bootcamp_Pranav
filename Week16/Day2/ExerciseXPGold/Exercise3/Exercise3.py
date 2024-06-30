def pair_sum_zero(nums: list):
   sorted_nums = sorted(nums)
   left = 0
   right = len(nums) - 1

   while left < right and left < len(nums):
      sum = sorted_nums[left] + sorted_nums[right]
      if sum == 0:
         return (nums.index(sorted_nums[left]), nums.index(sorted_nums[right]))
      elif sum > 0:
         right -=1
      else:
         left += 1

   return None
   
print(pair_sum_zero([1,2,3,-1,4,5,6,7]))