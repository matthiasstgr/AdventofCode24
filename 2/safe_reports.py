
def get_reports() -> list[str]:
    input = open('/Users/matthiassteger/Documents/projects/AoC/AdventofCode24/2/input.txt', 'r')
    
    report_list = input.readlines()
    for i in range(len(report_list)):
        report_list[i] = report_list[i][:-1]

    return report_list

def get_safe_rep_count(lines) -> int:
    safe_count = 0
    for line in lines:
        safe_bool = False
        levels = str(line).split(' ')
        first = int(levels[0])
        second = int(levels[1])
        if (second - first) >= 1 and (second - first) <= 3:
            safe = check_asc(levels)
        elif (first - second) > 0:
            safe = check_desc(levels)    

        if safe:
            safe_count += 1
    return safe_count;

def check_asc(levels) -> bool:
    for i in range(len(levels)-1):
        first = int(levels[i])
        second = int(levels[i+1])
        diff = second - first
        if 1 <= diff <= 3:
            continue
        else:
            return False
    return True

def check_desc(levels) -> bool:
    for i in range(len(levels)-1):
        first = int(levels[i])
        second = int(levels[i+1])
        diff = first - second
        if 1 <= diff <= 3:
            continue
        else:
            return False
    return True

reports = get_reports()
print(get_safe_rep_count(reports))