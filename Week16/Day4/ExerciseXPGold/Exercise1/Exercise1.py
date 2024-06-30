def recursive_sum(nums: list):
   if not nums:
      return 0
   else:
      return nums[0] + recursive_sum(nums[1:])
   
print(recursive_sum([1,2,3,4]))