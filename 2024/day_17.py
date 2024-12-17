with open("input.txt") as f:
    input = f.read()

def get_operand(operand_point):
    if int(operand_point) < 4:
        return int(operand_point)
    elif operand_point == "4":
        return register["A"]
    elif operand_point == "5":
        return register["B"]
    elif operand_point == "6":
        return register["C"]
    elif operand_point == "7":
        return None

def instruction(opcode, combo_operand, literal_operand, pointer):
    # ADV
    if opcode == "0":
        num = register["A"]
        denom = 2 ** int(combo_operand) 
        register["A"] = int(num / denom)
        return pointer + 2
    # BXL
    if opcode == "1":
        register["B"] = register["B"] ^ literal_operand
        return pointer + 2
    # BST
    if opcode == "2":
        register["B"] = combo_operand % 8
        return pointer + 2
    # JNZ
    if opcode == "3":
        if register["A"] == 0:
            return pointer + 2
        else:
            return literal_operand
    # BXC
    if opcode == "4":
        register["B"] = register["B"] ^ register["C"]
        return pointer + 2
    # OUT
    if opcode == "5":
        to_out.append(str(combo_operand % 8))
        return pointer + 2
    # BDV
    if opcode == "6":
        num = register["A"]
        denom = 2 ** int(combo_operand) 
        register["B"] = int(num / denom)
        return pointer + 2   
    if opcode == "7":
        num = register["A"]
        denom = 2 ** int(combo_operand) 
        register["C"] = int(num / denom)
        return pointer + 2        


register ={"A":44348299, "B":0, "C":0}
program = input.split(",")

pointer = 0
to_out = []
while pointer < len(program)-1:
    print(pointer)
    opcode = program[pointer]
    operand = int(program[pointer +1])
    combo_operand = get_operand(program[pointer+1])
    print("opcode", opcode, "operand", operand)
    pointer = instruction(opcode, combo_operand, operand, pointer)

print(register)
print(",".join(to_out))