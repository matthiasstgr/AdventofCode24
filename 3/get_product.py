import re
input = open('/Users/matthiassteger/Documents/projects/AoC/AdventofCode24/3/input.txt', 'r')

def calculate_product(data) -> int:
    product = 0
    for line in data:
        nums = line[4:-1].split(',')
        product += int(nums[0]) * int(nums[1])
    return product

text = input.read()
correct_data = re.findall(r'mul\(\d+,\d+\)', text)
product = calculate_product(correct_data)
print(product)

