import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_pairs_sum_to_target(numbers, target):
    count = 0
    num_count = {}
    
    for num in numbers:
        complement = target - num
        if complement in num_count:
            count += num_count[complement]
        
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    return count

pair_count = find_pairs_sum_to_target(list_of_numbers, target_number)
print(f"Number of pairs in list_of_numbers that sum up to {target_number}: {pair_count}")