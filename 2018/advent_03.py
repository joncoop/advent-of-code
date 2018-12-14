# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    formatted = []

    for line in lines:
        line = line.split(' ')
        n = int(line[0][1:])

        loc = line[2][:-1].split(',')
        x = int(loc[0])
        y = int(loc[1])
        
        dim = line[3].split('x')
        w = int(dim[0])
        h = int(dim[1])

        formatted.append([n, x, y, w, h])

    return formatted

# helper functions
def get_dimensions(data):
    width = 0
    height = 0

    for record in data:
        x = record[1]
        y = record[2]
        w = record[3]
        h = record[4]

        width = max(width, x + w)
        height = max(height, y + h)
        
    return width, height

def get_matrix(width, height):
    matrix = []
    
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)
        matrix.append(row)
        
    return matrix

def mark_overlaps(data):
    width, height = get_dimensions(data)

    matrix = get_matrix(width, height)
    overlaps = []
    for _ in range(len(lines) + 1):
        overlaps.append(False)

    for record in data:
        n = record[0]
        x = record[1]
        y = record[2]
        w = record[3]
        h = record[4]

        for row in range(y, y + h):
            for col in range(x, x + w):
                if matrix[row][col] != 0:
                    overlaps[n] = True
                    overlaps[matrix[row][col]] = True
                matrix[row][col] = n
                
    return overlaps

# solutions
def solve1(data):
    width, height = get_dimensions(data)
    matrix = get_matrix(width, height)
    count = 0

    for record in data:
        x = record[1]
        y = record[2]
        w = record[3]
        h = record[4]
        
        for row in range(y, y + h):
            for col in range(x, x + w):
                matrix[row][col] += 1

                if matrix[row][col] == 2:
                    count += 1
                
    return count

def solve2(data):
    overlaps = mark_overlaps(data)

    non_overlaps = []
    
    for i, shared in enumerate(overlaps):
        if not shared:
            non_overlaps.append(i)
        
    return non_overlaps[1:]

# go
path = 'data/input_03.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
