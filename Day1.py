print("hello")

numArr = []
numArr2 = []
totalDistance:int = 0
multipliedTotal:int = 0

fh = open("test-input-2.txt")
for line in map(str.rstrip, fh):
    nums = line.split("   ")
    numArr.append(int(nums[0]))
    numArr2.append(int(nums[1]))

numArr.sort()
numArr2.sort()

for num in range(len(numArr)):
    totalDistance += abs(numArr[num] - numArr2[num])

for num in range(len(numArr)):
    frequency = 0
    for num2 in range(len(numArr2)):
        if numArr[num] == numArr2[num2]:
            frequency += 1

    multipliedTotal += (numArr[num] * frequency)

print(multipliedTotal)
print(totalDistance)

# TODO: optimization

# Part 1

# what zip does --> goes through all lists inputed, stops at the last item in any of the lists
#(so if last item in list 2 is in index 6 but there is in list 7 an item at index 7, then it will
# stop at item on index 6)

for l1, l2 in zip(numArr, numArr2):
    totalDistance += abs(l2- l1)

# Part 2
num_freq1 = {}

for line in map(str.strip, fh):
    n1, n2 = line.split("   ")
    if n1 in num_freq1:
        num_freq1[n1] += 1
    else:
        num_freq1[n1] = 1

for n1 in num_freq1:
    totalDistance += num_freq1[n1] * num_freq2[n1]