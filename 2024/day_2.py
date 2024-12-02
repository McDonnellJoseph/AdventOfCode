with open("full_input.txt") as f:
    ipt = f.read()

reports = []
for line in ipt.splitlines():
    reports.append([int(l) for l in line.split(" ")])

def is_safe(report):
    increasing = report[1] > report[0]
    is_safe = True
    errors = []
    for i in range(1, len(report)):
        if increasing and report[i] <= report[i-1]:
            errors.append(i-1)
            errors.append(i)
            is_safe = False

        if not increasing and report[i] >= report[i-1]:
            errors.append(i-1)
            errors.append(i)
            is_safe = False
            
            
        if abs(report[i] - report[i-1]) > 3:
            errors.append(i)
            errors.append(i-1)
            is_safe = False
    errors.append(0)
            
    return is_safe, errors

safety_count = []
for report in reports:
    SAFE, ERRORS = is_safe(report) 
    
    for error in ERRORS:
        test_report = report.copy()
        del test_report[error]
        test_safe, errors = is_safe(test_report)
        if test_safe:
            SAFE = True
            break

    safety_count.append(SAFE) 

print(reports)
print(safety_count)

print(sum(safety_count))