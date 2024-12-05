with open("input.txt") as f:
    input = f.read()

rules, updates = input.split("\n\n")

# Parse rules into a sorted list
rule_dict_before = {}

for rule in rules.splitlines():
    before, after = rule.split("|")
    if before not in rule_dict_before.keys():
        rule_dict_before[before] = [after]
    else:
        rule_dict_before[before].append(after)


valid_count = 0 
valid_middle_total = 0
total_part_2 = 0
for update in updates.splitlines():
    vals = update.split(",")
    # For each predecessor is there a rule that says they should be greater than me 
    is_true = True
    ordered_vals = vals.copy()
    for i in range(1, len(vals)):
        for j in range(i):
            if vals[i] in rule_dict_before and vals[j] in rule_dict_before[vals[i]]:
                
                is_true = False
        for k in range(i+1, len(vals)):
            if (vals[k] in rule_dict_before and vals[i] in rule_dict_before[vals[k]]):
                is_true = False

    is_true_first = is_true
    while not is_true:
        is_true = True
        vals = ordered_vals.copy()
        print("start loop")
        print(ordered_vals)
        for i in range(1, len(vals)):
            for j in range(i):
                if ordered_vals[i] in rule_dict_before and ordered_vals[j] in rule_dict_before[ordered_vals[i]]:
                    ordered_vals.insert(i+1, ordered_vals[j])
                    del ordered_vals[j]
                    is_true = False
           
            for k in range(i+1, len(vals)):
                if (vals[k] in rule_dict_before and vals[i] in rule_dict_before[vals[k]]):
                    ordered_vals.insert(i-1, ordered_vals[k])
                    del ordered_vals[k+1]
                    is_true = False
           

    print("end")                   
    print(ordered_vals)
    if is_true_first:
        valid_middle_total += int(vals[len(vals)//2])
    
    else:
        print(ordered_vals)
        total_part_2 += int(ordered_vals[len(ordered_vals)//2])
    valid_count += int(is_true) 
            




print(valid_count)
print(valid_middle_total)
print(total_part_2)