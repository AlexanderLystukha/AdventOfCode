print("hello")

fh = open("sample.txt")

totalSafe = 0
for line in map(str.rstrip, fh):

    isIncreasing = True
    isValid = True
    nums = line.split(" ")
    dif = abs(int(nums[0]) - int(nums[1]))
    print(nums)
    print(dif)
    if (int(nums[0]) > int(nums[1])):
        isIncreasing = False

    if(1 > dif or dif > 3):
        isValid = False


    for num in range(1, len(nums) - 1):

        dif = abs(int(nums[num]) - int(nums[num + 1]))
        if(isIncreasing and isValid):
            if(int(nums[num]) > int(nums[num + 1]) or (1 > dif or dif > 3)):
                isValid = False
                break

        elif(not isIncreasing and isValid):
            if(int(nums[num]) < int(nums[num + 1]) or (1 > dif or dif > 3)):
                isValid = False
                break


    if(isValid):
        print("valid")
        totalSafe += 1

print(totalSafe)