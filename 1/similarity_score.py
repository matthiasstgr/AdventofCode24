input = open('/Users/matthiassteger/Documents/projects/AoC/AdventofCode24/1/input.txt', 'r')
similarity_score = 0
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

for i in left:
    times = 0
    for j in right:
        if i == j:
            times += 1
    similarity_score += i * times

print(similarity_score)