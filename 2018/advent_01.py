# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    nums = [int(line) for line in lines]
    
    return nums

# solutions
def solve1(nums):
    return sum(nums)

def solve2(nums):
    current = 0
    frequencies = [current]

    while True:
        for n in nums:
            current += n
            
            if current not in frequencies:
                frequencies.append(current)
            else:
                return current

# go
path = 'data/input_01.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
