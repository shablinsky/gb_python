import random

with open('num_for_6task.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0, 10)} ')

with open('num_for_6task.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)
