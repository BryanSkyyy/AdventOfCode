lines = []
with open('input1.txt') as f:
    lines = f.readlines()

array = []
for line in lines:
    array.append(int(line))

total = 0
i = 1
while i < len(array):
    if(array[i] > array[i - 1]):
        total += 1
    i += 1

print(total)