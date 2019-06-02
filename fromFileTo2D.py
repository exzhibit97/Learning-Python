import re

data2 = []
tableInterval1Raw = [[0] * 5 for i in range(150)]
file = open('learning.txt', 'r')

r2 = re.compile("[0-9,; ]*\)[0-9;]*|\[[0-9;,]*|[\w]")
for line in file:
    data2.append(re.findall(r2, line))
file.close()

for i in range(150):
    interval1 = (data2[i][0] + data2[i][1])
    tableInterval1Raw[[i][0]] = interval1

unique_list = []
for a in tableInterval1Raw:
    if a not in unique_list:
        unique_list.append(a)

tableInterval1 = [[0] * 5 for i in range(5)]
for j in range(5):
    tableInterval1[j][0] = unique_list[j]

for i in range(len(tableInterval1Raw)):
    for j in range(5):
        if tableInterval1[j][0] == tableInterval1Raw[i]:
            tableInterval1[j][1] = tableInterval1[j][1] + 1

finishedData2 = [[0] * 3 for i in range(150)]

for i in range(150):
    finishedData2[i][0] = data2[i][0] + data2[i][1]
    finishedData2[i][1] = data2[i][2] + data2[i][3]
    finishedData2[i][2] = data2[i][4]

for i in range(len(finishedData2)):
    for j in range(5):
        if finishedData2[i][0] == tableInterval1[j][0] and finishedData2[i][2] == "A":
            tableInterval1[j][2] = tableInterval1[j][2] + 1

for i in range(len(finishedData2)):
    for j in range(5):
        if finishedData2[i][0] == tableInterval1[j][0] and finishedData2[i][2] == "B":
            tableInterval1[j][3] = tableInterval1[j][3] + 1

for i in range(len(finishedData2)):
    for j in range(5):
        if finishedData2[i][0] == tableInterval1[j][0] and finishedData2[i][2] == "C":
            tableInterval1[j][4] = tableInterval1[j][4] + 1
