input = open('/Users/matthiassteger/Documents/projects/AoC/AdventofCode24/1/input.txt', 'r')
total_distance = 0
left = []
right = []

while True:
    pair = input.readline()
    if not pair:
        break
    pair = pair[:-1]
    pair_list = pair.split("   ")

    left.append(int(pair_list[0]))
    right.append(int(pair_list[1]))

left.sort()
right.sort()

for i in range(len(left)):
    if left[i] > right[i]:
        total_distance += left[i] - right[i]
    else:
        total_distance += right[i] - left[i]

print(total_distance)