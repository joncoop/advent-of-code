# read data
def read_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()

    return lines

def get_formatted_data(lines):
    formatted = []
    
    for line in lines:
        date = line[6:11]
        minute = int(line[15:17])
        status = line[19:]
        formatted.append([date, minute, status])
    
    return formatted

# helper functions
def sort_by_time(data):
    return sorted(data, key = lambda x: (x[0], x[1]))

def get_guard_num(status):
    chunks = status.split(' ')
    num_str = chunks[1][1:]
    return int(num_str)

def get_sleep_times(data):
    sleep_times = {}
    current_guard = -1
    asleep = False
    
    for record in data:
        minute = record[1]
        status = record[2]
        
        if "#" in status:
            if asleep:
                for i in range(sleep_start, minute):
                    sleep_times[current_guard][i] += 1

            current_guard = get_guard_num(status)
            asleep = True
            sleep_start = minute
            
            if current_guard not in sleep_times.keys():
                sleep_times[current_guard] = [0] * 60


        elif status == "falls asleep":
            asleep = True
            sleep_start = minute
        elif status == "wakes up":
            asleep = False
            for i in range(sleep_start, minute):
                sleep_times[current_guard][i] += 1
        
    return sleep_times

def get_sleepiest_guard(sleep_times):
    sleepiest = -1
    max_sleep = 0
    
    for guard_num, minute_list in sleep_times.items():
        total_sleep = sum(minute_list)

        if total_sleep > max_sleep:
            max_sleep = total_sleep
            sleepiest = guard_num

    return sleepiest

def get_time_most_asleep(minute_list):
    max_minute = 0
    max_sleep = 0

    for i, sleep_time in enumerate(minute_list):
        if sleep_time > max_sleep:
            max_minute = i
            max_sleep = sleep_time

    return max_minute

# solutions
def solve1(data):
    data = sort_by_time(data)        
    sleep_times = get_sleep_times(data)        
    guard_num = get_sleepiest_guard(sleep_times)
    minutes_asleep = sleep_times[guard_num]
    time = get_time_most_asleep(minutes_asleep)

    return guard_num * time

def solve2(data):
    data = sort_by_time(data)        
    sleep_times = get_sleep_times(data)

    max_minute = -1
    max_slept_at_minute = -1
    guard_num = -1
    
    for k, v in sleep_times.items():
        for i, minutes in enumerate(v):
            if minutes >= max_slept_at_minute:
                max_slept_at_minute = minutes
                max_minute = i
                guard_num = k

    return guard_num * max_minute

# go
path = 'data/input_04.txt'
lines = read_data(path)
formatted_data = get_formatted_data(lines)

answer1 = solve1(formatted_data)
print("1. " + str(answer1))

answer2 = solve2(formatted_data)
print("2. " + str(answer2))
