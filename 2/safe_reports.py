
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
        if 1 <= (second - first) <= 3:
            safe = check_asc(levels)
        elif (first - second) > 0:
            safe = check_desc(levels)    

        if safe:
            safe_count += 1
        else:
            if check_problem_dampener(levels):
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

def check_problem_dampener(levels) -> bool:
    safe = False
    for idx in range(len(levels)):
        temp_levels = levels.copy()
        temp_levels.pop(idx)

        first = int(temp_levels[0])
        second = int(temp_levels[1])
        if 1 <= (second - first) <= 3:
            safe = check_asc(temp_levels)
        elif 1 <= (first - second) <= 3:
            safe = check_desc(temp_levels)
        
        if safe:
            break

    return safe
            
    
reports = get_reports()
print(get_safe_rep_count(reports))