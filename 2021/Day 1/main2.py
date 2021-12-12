lines = []
with open('input1.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    array.append(int(line))

total = 0
i = 3
while i < len(array):
    first = array[i - 3] + array[i - 2] + array[i - 1]
    second = array[i - 2] + array[i - 1] + array[i]
    print(first)
    print(second)
    if(second > first):
        total += 1

    i += 1

print(total)