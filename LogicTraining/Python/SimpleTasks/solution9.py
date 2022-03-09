T = int(input())
ansList = []
for tc in range(T):
    a, b = map(int, input().split())
    ans = a + b
    ansList.append(ans)

for i in range(len(ansList)):
    print(ansList[i])