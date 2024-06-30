def longest_sequence(nums: list):
   sorted_nums = sorted(nums)
   sequence = []
   for i in range(len(nums) - 2):
      if sorted_nums[i] + 1 == sorted_nums[i+1]:
         sequence.append(sorted_nums[i])
      else:
         sequence.append(sorted_nums[i])
         return sequence
      
print(longest_sequence([10,1,4,2,3,9,9,5]))