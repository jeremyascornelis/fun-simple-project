listSubj = []
for i in range(1, 7):
    subj = int(input(f"Enter {i} subject marks: "))
    listSubj.append(subj)

#total
totalResult = 0
for j in range (0, len(listSubj)):
    totalResult += listSubj[j]

average = totalResult / 6

print(f"Total subjects marks are {totalResult}")
print("Average mark is {:.2f}".format(average))