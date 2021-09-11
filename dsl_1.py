# Group A Question (part a and d)

groupA = ['Sejal', 'Rajesh', 'Atharva', 'Ruchita', 'Snehal']
groupB = ['Sejal', 'Saloni', 'Atharva', 'Varad', 'Aditya', 'Snehal']
groupC = ['Rajesh', 'Ruchita', 'Vaibhav', 'Atharva']

# Length of array:-

lenA = len(groupA)
lenB = len(groupB)
lenC = len(groupC)

# List of students who play both Cricket and Badminton

print("List of students who play both Cricket and Badminton : ")

listCB = []
for i in range(lenA):
    for var in range(lenB):
        if groupB[var] == groupA[i]:
            listCB.append(groupA[i])

print(listCB)

# List of Students who play cricket and football but not badminton:-

print("list of students who play cricket and football but not badminton : ")

E = listCB
lenE = len(E)
listY = []
p = 0

for i in range(lenC):
    for var in range(lenE):
        if groupC[i] == E[var]:
            p = 1

    if p == 0:
        listY.append(groupC[i])

print(listY)
