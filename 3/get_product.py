import re
input = open('/Users/matthiassteger/Documents/projects/AoC/AdventofCode24/3/input.txt', 'r')

def calculate_product(data) -> int:
    product = 0
    for line in data:
        nums = line[4:-1].split(',')
        product += int(nums[0]) * int(nums[1])
    return product

def get_filtered_data(data) -> str:
    filtered_data = data
    while True:
        old_filtered_data = filtered_data
        filtered_data = re.sub(r'don\'t\(\)(.|\n)*?do\(\)', '', filtered_data, re.DOTALL)
        if filtered_data == old_filtered_data:
            break
    return(filtered_data)

text = input.read()
correct_data = re.findall(r'mul\(\d+,\d+\)', text)
product = calculate_product(correct_data)
print('Without do and dont:', product)

filtered_text = get_filtered_data(text)
correct_filtered_data = re.findall(r'mul\(\d+,\d+\)', filtered_text)
filtered_product = calculate_product(correct_filtered_data)
print('With do and dont:', filtered_product)

