print("hello")

numArr = []
numArr2 = []
totalDistance:int = 0
multipliedTotal:int = 0

fh = open("sample.txt")
for line in map(str.rstrip, fh):
    nums = line.split(" ")

for num in range(len(numArr)):
    totalDistance += abs(int(numArr[num]) - int(numArr2[num]))

for num in range(len(numArr)):
    frequency = 0
    for num2 in range(len(numArr2)):
        if int(numArr[num]) == int(numArr2[num2]):
            frequency += 1

    multipliedTotal += (int(numArr[num]) * frequency)

print(multipliedTotal)
print(totalDistance)