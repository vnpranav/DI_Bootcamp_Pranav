def subset_sum(nums: list, target: int):
   complements = set()
   for num in nums:
      complement = target - num
      if complement in complements:
         return True
      complements.add(num)

   return False

print(subset_sum([1,2,3,4,5,-1,2,3,4,6], 14))