import random
i = 0

n = int(input("How many numbers do you want in your list? "))

initialList = list(range(1, n+1))
random.shuffle(initialList)
finalList = initialList.copy()

while True:
    changes = 0
    for i in range(len(finalList) - 1):
        if finalList[i] > finalList[i + 1]:
            finalList[i], finalList[i + 1] = finalList[i + 1], finalList[i]
            changes += 1

    if changes == 0:
        break

with open(f'result.txt', 'w') as f:
    f.write(f'''
Initial list:
{initialList}

Final list:
{finalList}
            ''')