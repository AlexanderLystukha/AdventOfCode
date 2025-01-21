import sys
import time

DEFAULT_PART: int = 1
DEFAULT_INPUT_FILE_NAME: str = "test-input-2.txt"

numArr = []
numArr2 = []

def timeit(func):
    """
    A python decorator for measuring function's running time.
    Adapted from: https://stackoverflow.com/questions/35656239/
    """

    def measure_time(*args, **kw):
        start_time: float = time.time()
        result = func(*args, **kw)
        end_time: float = time.time()
        print(f"Processing time of {func.__qualname__}(): {end_time - start_time: .5f} seconds.", file=sys.stderr)
        return result

    return measure_time


@timeit
def part1(input_file_name: str):
    totalDistance: int = 0

    fh = open(input_file_name)
    for line in map(str.rstrip, fh):
        nums = line.split("   ")
        numArr.append(int(nums[0]))
        numArr2.append(int(nums[1]))

    numArr.sort()
    numArr2.sort()

    for num in range(len(numArr)):
        totalDistance += abs(numArr[num] - numArr2[num])
        # TODO: replace with your solution


@timeit
def part2(input_file_name: str):

    multipliedTotal: int = 0

    fh = open(input_file_name)
    for line in map(str.rstrip, fh):
        nums = line.split("   ")
        numArr.append(int(nums[0]))
        numArr2.append(int(nums[1]))

    numArr.sort()
    numArr2.sort()

    for num in numArr:
        frequency = 0
        for num2 in range(len(numArr2)):
            if num == num2:
                frequency += 1

        multipliedTotal += (num * frequency)
        # TODO: replace with your solution


if __name__ == "__main__":

    part: int = DEFAULT_PART
    input_file_name: str = DEFAULT_INPUT_FILE_NAME

    # process arguments if any
    if len(sys.argv) > 2:
        input_file_name = sys.argv[2]
    if len(sys.argv) > 1:
        part = int(sys.argv[1])

    if part == 1:
        part1(input_file_name)
    elif part == 2:
        part2(input_file_name)
    else:
        print("Error: part must be 1 or 2.")
