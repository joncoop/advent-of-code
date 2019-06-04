# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    result = []
    for line in lines:
        step = line[5]
        before = line[36]
        result.append([step, before])
        print(step, before)
    return result

# helper functions
def is_before(string, letter, before):
    return string.find(letter) < string.find(before)

def insert_before(string, letter, before):
    result = string.replace(letter, '')

    i = string.find(before)

    while letter < result[i]:
        i -= 1

    return result[:i] + letter + result[i:]

# solutions
def solve1(data):
    result =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for line in data:
        step = line[0]
        before = line[1]

        if not is_before(result, step, before):
            result = insert_before(result, step, before)
        print([step, before], result)
    return result

def solve2(data):
    return None

# go
path = 'data/input_07.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
