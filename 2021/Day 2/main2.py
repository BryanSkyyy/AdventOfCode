lines = []
print("Hello world")
with open('input.txt') as f:
    lines = f.readlines()

arrayDir = []
array = []
for line in lines:
    splitlist = line.split();
    #print(splitlist)
    arrayDir.append(splitlist[0])
    array.append(int(splitlist[1]))

horizontal = 0
depth = 0
aim = 0
i = 0
while i < len(array):
    if (arrayDir[i] == "forward"):
        horizontal += array[i]
        depth += array[i] * aim
    elif (arrayDir[i] == "up"):
        aim -= array[i]
    else:
        aim += array[i]
    i += 1
print(horizontal)
print(depth)
print(horizontal * depth)