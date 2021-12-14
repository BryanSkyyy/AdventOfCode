lines = []
print("Hello world")
with open('input.txt') as f:
    lines = f.readlines()

arrayDir = []
array = []
i = 0
while i < len(lines[0]):
    if (lines[0][i] == "0" or lines[0][i] == "1"):
        array.append(int(0))
    i += 1

i = 0

for line in lines:
    i = 0
    while i < len(line):
        if (line[i] != '\n'):
            if (line[i] == "1"):
                array[i] += 1
            elif(line[i] == "0"):
                array[i] -= 1
        i += 1

i = 0

gamma = ""
epsilon = ""

while i < len(array):
    if (array[i] >= 0):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    i += 1
        
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma)
print(epsilon)
print(gamma * epsilon)