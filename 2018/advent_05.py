# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    return lines[0]

# helper functions
def get_first_match_loc(data):
    for i in range(0, len(data) - 1):
        a = data[i]
        b = data[i+1]

        if a.lower() == b.lower() and not a == b:
            return i

    return -1

def react(data):
    loc = get_first_match_loc(data)
    result = data[:loc]
    
    while loc > -1:
        data = data[:loc] + data[loc+2:]
        loc = get_first_match_loc(result)

    return result
        
def remove_unit(data, letter):
    big = letter.upper()
    little = letter.lower()

    data = data.replace(big, '')
    data = data.replace(little, '')

    return data

# solutions
def solve1(data):
    reacted = react(data)

    return len(reacted)

def solve2(data):
    smallest = len(data)
    units = "abcdefghijklmnopqrstuvwxyz"

    for u in units:
        copy = remove_unit(data, u)
        reacted = react(copy)
        size = len(reacted)
        smallest = min(smallest, size)

    return smallest
        

    

# go
path = 'data/input_05.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
