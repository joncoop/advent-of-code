def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def solve(nums):
    current = 0
    frequencies = [current]

    while True:
        for n in nums:
            current += n
            
            if current not in frequencies:
                frequencies.append(current)
            else:
                return current

# Go
lines = read_data('input_01.txt')
nums = [int(line) for line in lines]

answer = solve(nums)
print(answer)
