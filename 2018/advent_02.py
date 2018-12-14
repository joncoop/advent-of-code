# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    return lines

#helper functions
def has_matches(line, amount):
    for letter in line:
        count = 0
        for letter2 in line:
            if letter == letter2:
                count += 1

        if count == amount:
            return True

    return False

def remove_matches(line1, line2):
    result = ""
    
    for c1, c2 in zip(line1, line2):
        if c1 == c2:
            result += c1
    return result

#solutions
def solve1(lines):
    twos = 0
    threes = 0

    for line in lines:
        if has_matches(line, 2):
            twos += 1
        if has_matches(line, 3):
            threes += 1

    return twos * threes

def solve2(lines):
    for line1 in lines:
        for line2 in lines:
            removed = remove_matches(line1, line2)

            if len(removed) == len(line1) - 1:
                return removed

    return None

# Go
path = 'data/input_02.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
