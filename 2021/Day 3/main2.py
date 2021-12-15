lines = []
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

oxy = lines.copy()
co2 = lines.copy()
oxyNum = ""
co2Num = ""

i = 0
temp = oxy.copy()
while i < len(array):
    oxy.clear()
    oxy = temp.copy()
    temp.clear()
    
    j = i
    while j < len(array):
        array[j] = 0
        j += 1
    j = i
    while j < len(array):
        for line in oxy:
            if (line[j] != '\n'):
                if (line[j] == "1"):
                    array[j] += 1
                elif(line[j] == "0"):
                    array[j] -= 1
        j += 1
    for line in oxy:
        if(array[i] >= 0 and line[i] == "1"):
            temp.append(line)
        elif(array[i] < 0 and line[i] == "0"):
            temp.append(line)
    i += 1
    if (len(temp) == 1):
        oxy = temp.copy()
        break

i = 0
temp.clear()
temp = co2.copy()
while i < len(array):
    co2.clear()
    co2 = temp.copy()
    temp.clear()
    
    j = i
    while j < len(array):
        array[j] = 0
        j += 1
    j = i
    while j < len(array):
        for line in co2:
            if (line[j] != '\n'):
                if (line[j] == "1"):
                    array[j] += 1
                elif(line[j] == "0"):
                    array[j] -= 1
        j += 1
    for line in co2:
        if(array[i] >= 0 and line[i] == "0"):
            temp.append(line)
        elif(array[i] < 0 and line[i] == "1"):
            temp.append(line)
    i += 1
    if (len(temp) == 1):
        co2 = temp.copy()
        break


oxyNum = int(oxy[0], 2)
co2Num = int(co2[0], 2)
print (oxyNum * co2Num)