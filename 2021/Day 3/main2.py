lines = []
with open('inputsample.txt') as f:
    lines = f.readlines()

arrayDir = []
array = []
i = 0
while i < len(lines[0]):
    if (lines[0][i] == "0" or lines[0][i] == "1"):
        array.append(int(0))
    i += 1

i = 0

#TODO
#This needs to be done dynamically as we remove stuff from oxy and co2
for line in lines:
    i = 0
    while i < len(line):
        if (line[i] != '\n'):
            if (line[i] == "1"):
                array[i] += 1
            elif(line[i] == "0"):
                array[i] -= 1
        i += 1

oxy = lines.copy()
co2 = lines.copy()

oxyNum = ""
co2Num = ""

i = 0
print(array)
while i < len(array):
    for line in lines:
        if (len(oxy) == 1):
            oxyNum = oxy[0]
            break
        if line in oxy:
            if(array[i] >= 0 and line[i] == "0"):
                if len(oxy) > 1:
                    oxy.remove(line)
            elif(array[i] < 0 and line[i] == "1"):
                if len(oxy) > 1:
                    oxy.remove(line)
    i += 1

i = 0

while i < len(array):
    
    for line in lines:
        if (len(co2) == 1):
            co2Num = co2[0]
            break
        if line in co2:
            if(array[i] >= 0 and line[i] == "1"):
                if len(co2) > 1:
                    co2.remove(line)
            elif(array[i] < 0 and line[i] == "0"):
                if len(co2) > 1:
                    co2.remove(line)
    i += 1

print(oxyNum)
print(co2Num)

oxyNum = int(oxyNum, 2)
co2Num = int(co2Num, 2)

print(oxyNum)
print(co2Num)
print(oxyNum * co2Num)