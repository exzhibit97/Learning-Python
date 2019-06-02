import re

data2 = []
tableInterval2Raw = [[0] * 5 for i in range(150)]
file = open('learning.txt', 'r')

r2 = re.compile("[0-9,; ]*\)[0-9;]*|\[[0-9;,]*|[\w]")
for line in file:
    data2.append(re.findall(r2, line))
file.close()

for i in range(150):
    interval2 = (data2[i][2] + data2[i][3])
    tableInterval2Raw[[i][0]] = interval2

unique_list2 = []
for a in tableInterval2Raw:
    if a not in unique_list2:
        unique_list2.append(a)

tableInterval2 = [[0] * 5 for i in range(6)]
for j in range(6):
    tableInterval2[j][0] = unique_list2[j]

for i in range(len(tableInterval2Raw)):
    for j in range(6):
        if tableInterval2[j][0] == tableInterval2Raw[i]:
            tableInterval2[j][1] = tableInterval2[j][1] + 1

finishedData22 = [[0] * 3 for i in range(150)]

for i in range(150):
    finishedData22[i][0] = data2[i][0] + data2[i][1]
    finishedData22[i][1] = data2[i][2] + data2[i][3]
    finishedData22[i][2] = data2[i][4]

for i in range(len(finishedData22)):
    for j in range(6):
        if finishedData22[i][1] == tableInterval2[j][0] and finishedData22[i][2] == "A":
            tableInterval2[j][2] = tableInterval2[j][2] + 1

for i in range(len(finishedData22)):
    for j in range(6):
        if finishedData22[i][1] == tableInterval2[j][0] and finishedData22[i][2] == "B":
            tableInterval2[j][3] = tableInterval2[j][3] + 1

for i in range(len(finishedData22)):
    for j in range(6):
        if finishedData22[i][1] == tableInterval2[j][0] and finishedData22[i][2] == "C":
            tableInterval2[j][4] = tableInterval2[j][4] + 1
