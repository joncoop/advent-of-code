# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    return lines

# helper functions
def helper1():
    pass

def helper2():
    pass

# solutions
def solve1(data):
    return None

def solve2(data):
    return None

# go
path = 'data/input_01.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
