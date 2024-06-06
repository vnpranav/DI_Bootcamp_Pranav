my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
sum = 0

for item in my_list:
    try:
        sum += item
    except (TypeError, ValueError):
        print(f'item "{item}" is not a number')

print(f'sum = {sum}')
