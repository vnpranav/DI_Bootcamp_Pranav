def duplicates_count(nums: list):
   nums_set = set(nums)

   return len(nums) - len(nums_set)

print(duplicates_count([1,2,3,4,5,1,2,3,4,5,11,11,345]))