import random

def brute_search(search_value, array):
    count = 0
    for value in array:
        count += 1
        if value == search_value:
            break

    print(f'It took {count} passes to found the number using brute searching')

def binary_search(search_value, array):
    sorted_list = sorted(array)
    lower = 0
    upper = len(array) - 1
    count = 0
    found = False

    while not (lower > upper) and found == False:
        count += 1
        middle = (upper + lower) // 2

        if sorted_list[middle] == search_value:
            found = True
            break
        elif sorted_list[middle] > search_value:
            upper = middle -1 
        else:
            lower = middle + 1
    
    if found == True:
        print(f'It took {count} passes to find the number using binary search\n')

#try to guess a random number between 1 and 100
numbers = [*range(1,101)]
random_choice = random.choice(numbers)
print(f'number to guess: {random_choice}')
brute_search(random_choice, numbers)
binary_search(random_choice, numbers)
