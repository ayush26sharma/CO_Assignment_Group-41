import sys
import os

dictionary_opcode = {"add": "00000", "sub": "00001", "mov1": "00010", "mov2": "00011", "ld": "00100", "st": "00101",
                     "mul": "00110", "div": "00111", "rs": "01000", "ls": "01001", "xor": "01010", "or": "01011",
                     "and": "01100", "not": "01101", "cmp": "01110", "jmp": "01111", "jlt": "10000", "jgt": "10001",
                     "je": "10010", "hlt": "10011"}
dictionary_reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110",
                  "FLAGS": "111"}


def add_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def sub_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def mul_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def or_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def and_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def xor_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "00"
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def mov_reg_func(l1):
    binary_code = ""
    binary_code += "00011"
    binary_code += ("0" * 5)
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def mov_imm_func(l1):
    binary_code = ""
    binary_code += "00010"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def load_func(l1, variable):
    binarycode = "00100"
    binarycode += dictionary_reg[l1[1]] + variable[l1[2]]
    return binarycode


def store_func(l1, variable):
    binarycode = "00101"
    binarycode += dictionary_reg[l1[1]] + variable[l1[2]]
    return binarycode


def div_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]] + "0" * 5
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def right_shift_func(l1):
    binary_code = ""
    binary_code += "01000"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def left_shift_func(l1):
    binary_code = ""
    binary_code += "01001"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def invert_func(l1):
    binary_code = ""
    binary_code += (dictionary_opcode[l1[0]] + "0" * 5)
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def compare_func(l1):
    binary_code = ""
    binary_code += (dictionary_opcode[l1[0]] + "0" * 5)
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def unconditional_jump_func(l1, labels1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += "0" * 3
    binary_code += labels1[l1[1]]
    return binary_code


def jump_if_less_func(l1, labels1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += "0" * 3
    binary_code += labels1[l1[1]]
    return binary_code


def jump_if_greater_func(l1, labels1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += "0" * 3
    binary_code += labels1[l1[1]]
    return binary_code


def jump_if_equal_func(l1, labels1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += "0" * 3
    binary_code += labels1[l1[1]]
    return binary_code


def halt_func():
    binary_code = ""
    binary_code += "10011"
    binary_code += ("0" * 11)
    return binary_code


def main():
    labels = {}
    variables = {}
    output = []
    labels_check = ["var","add", "sub", "mov", "ld", "st",
                    "mul", "div", "rs", "ls", "xor", "or",
                    "and", "not", "cmp", "jmp", "jlt", "jgt",
                    "je", "hlt"]
    reg_list = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
    reg_list_fl = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS"]
    l = list(map(str, sys.stdin.readlines()))
    # f = open('Readme.txt', mode='r+')
    # l = f.readlines()
    '''var x
    mov R1 $4
    mov R2 $4
    cmp R1 R2
    mov R3 FLAGS
    mov R4 $1
    cmp R3 R4
    jgt label
    label: hlt'''
    # l = f
    for i in range(len(l)):
        if i >= len(l):
            break
        j1 = l[i].strip()
        j1 = j1.strip("/n")
        if j1 == "":
            l.remove(l[i])
            i -= 1

    j = 0
    str1 = l[-1]
    str1 = str1.strip()
    str1 = str1.strip("/n")
    if "hlt" not in str1:
        print("ERROR: Last instruction should be 'hlt', ERROR on line: "+ str(len(l)))
        return
    for j in range(len(l)):
        j1 = l[j].strip()

        j1 = j1.strip("/n")

        list1 = j1.split()
        if "var" in list1:
            if len(list1) != 2 and len(list1) != 3:
                print("ERROR: Invalid variable instruction length on line: " + str(j + 1))
                return
            elif len(list1) == 3:
                pass
            else:
                if list1[0] != "var":
                    print("ERROR: Syntax for defining a variable is not correct, ERROR on line: " + str(j + 1))
                    return
                elif not (list1[1].isalnum() or list1[1].find("_") != -1):

                    print(
                        "ERROR: The name of a variable should contain only alphanumeric characters and underscore, ERROR on line: " + str(
                            j + 1))
                    return
                else:
                    if (list1[1] in labels_check):
                        print(
                            "ERROR: Variable name cannot be same as an instruction name, ERROR on line: " + str(j + 1))
                        return
                    variables[list1[1]] = 0
                    if len(l) == 1:
                        return
        else:
            break

    temp = j
    a1 = 0
    for x in variables.keys():
        converted = bin(len(l) - j + a1)[2:]

        variables[x] = "0" * (8 - len(converted)) + converted
        a1 += 1

    for x in range(len(l) - j):
        a1 = l[temp + x]
        a1 = a1.strip()
        a1 = a1.strip("/n")

        list1 = a1.split()
        if list1[0][-1] == ":" and list1[0][:-1].isalnum():
            if list1[0][:-1] in labels:
                print('ERROR: "' + str(list1[0][:-1]) + '" label already defined, ERROR on line: ' + str(temp + x + 1))
                return
            if len(list1)==1:
                print("ERROR: Label should be followed by an instruction, ERROR on line: "+ str(temp + x + 1))
                return
            labels[list1[0][:-1]] = "0" * (8 - len(bin(x)[2:])) + bin(x)[2:]
        elif a1.find(":") != -1:
            print("ERROR: The name of a label should always be alphanumeric with no spaces, ERROR on line: " + str(
                temp + x + 1))
            return
    for x in labels:
        if x in labels_check:
            print("ERROR: Name of a label can't be same as an instruction name, ERROR on line: "+ str(int(labels[x],2)))
            return
    for x in range(len(l[j:])):
        # print(i)
        i = l[j + x]
        i = i.strip()
        i = i.strip("/n")

        list1 = i.split()

        if "var" in list1:
            print("ERROR: Variables must be defined in the beginning of the code, ERROR on line: " + str(j + x + 1))
            return
        elif "add" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("ERROR:Invalid 'add' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "add":

                            print("ERROR: Syntax for add instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(add_func(list1[1:]))
                else:
                    if list1[0] != "add":
                        print("ERROR: Syntax for add instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(add_func(list1))

        elif "sub" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("ERROR:Invalid 'sub' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "sub":

                            print("ERROR: Syntax for sub instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(sub_func(list1[1:]))
                else:
                    if list1[0] != "sub":
                        print("ERROR: Syntax for sub instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(sub_func(list1))

        elif "mov" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("ERROR:Invalid 'mov' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "mov":
                            print("ERROR: Syntax for mov instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in reg_list:
                                print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                if list1[3] in reg_list_fl:
                                    output.append(mov_reg_func(list1[1:]))
                                else:
                                    if list1[3][0] != "$":
                                        print("ERROR: Immediate value is not defined properly, ERROR on line: " + str(
                                            j + x + 1))
                                        return
                                    elif list1[3][1:].isnumeric() and 255 >= int(list1[3][1:]) >= 0:
                                        output.append(mov_imm_func(list1[1:]))
                                    else:
                                        print(
                                            "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                                j + x + 1))
                                        return
                else:
                    if list1[0] != "mov":
                        print("ERROR: Syntax for mov instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] not in reg_list:
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            if list1[2] in reg_list_fl:
                                output.append(mov_reg_func(list1))
                            else:
                                if list1[2][0] != "$":
                                    print("ERROR: Immediate value is not defined properly, ERROR on line: " + str(
                                        j + x + 1))
                                    return
                                elif list1[2][1:].isnumeric() and 255 >= int(list1[2][1:]) >= 0:
                                    output.append(mov_imm_func(list1))

                                else:
                                    print(
                                        "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                            j + x + 1))
                                    return
        elif "ld" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("ERROR:Invalid 'ld' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "ld":
                            print("ERROR: Syntax for ld instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in reg_list:
                                print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                if list1[3] not in variables:
                                    print("ERROR: Invalid variable used, ERROR on line:" + str(j + x + 1))
                                    return
                                else:
                                    output.append(load_func(list1[1:], variables))
                else:
                    if list1[0] != "ld":
                        print("ERROR: Syntax for ld instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] not in reg_list:
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in variables:
                                print("ERROR: Invalid variable used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                output.append(load_func(list1, variables))

        elif "st" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("ERROR:Invalid 'st' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 4:
                    if list1[0] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "st":
                            print("ERROR: Syntax for st instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in reg_list:
                                print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                if list1[3] not in variables:
                                    print("ERROR: Invalid variable used, ERROR on line:" + str(j + x + 1))
                                    return
                                else:
                                    output.append(store_func(list1[1:], variables))
                else:
                    if list1[0] != "st":
                        print("ERROR: Syntax for st instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] not in reg_list:
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in variables:
                                print("ERROR: Invalid variable used, ERROR on line:" + str(j + x + 1))
                                return
                            else:

                                output.append(store_func(list1, variables))
        elif "mul" in list1:
            if len(list1) != 4 and len(list1) != 5:
                print("ERROR:Invalid 'mul' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "mul":
                            print("ERROR: Syntax for mul instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(mul_func(list1[1:]))
                else:
                    if list1[0] != "mul":

                        print("ERROR: Syntax for mul instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):

                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(mul_func(list1))
        elif "and" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("ERROR:Invalid 'and' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "and":

                            print("ERROR: Syntax for add instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(and_func(list1[1:]))
                else:
                    if list1[0] != "and":

                        print("ERROR: Syntax for add instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(and_func(list1))
        elif "or" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("ERROR:Invalid 'or' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "or":

                            print("ERROR: Syntax for 'or' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(or_func(list1[1:]))
                else:
                    if list1[0] != "or":

                        print("ERROR: Syntax for 'or' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(or_func(list1))
        elif "xor" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("ERROR:Invalid 'xor' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "xor":

                            print("ERROR: Syntax for xor instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(xor_func(list1[1:]))
                else:
                    if list1[0] != "xor":

                        print("ERROR: Syntax for xor instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(xor_func(list1))
        elif "rs" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("ERROR:Invalid 'rs' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "rs":
                            print("ERROR: Syntax for rs instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in reg_list:
                                print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                if list1[3][0] != "$":
                                    print("ERROR: Immediate value is not defined properly, ERROR on line: " + str(
                                        j + x + 1))
                                    return
                                elif list1[3][1:].isnumeric() and 255 >= int(list1[3][1:]) >= 0:
                                    output.append(right_shift_func(list1[1:]))
                                else:
                                    print(
                                        "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                            j + x + 1))
                                    return
                else:
                    if list1[0] != "rs":
                        print("ERROR: Syntax for rs instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] not in reg_list:
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            if list1[2][0] != "$":
                                print(
                                    "ERROR: Immediate value is not defined properly, ERROR on line: " + str(j + x + 1))
                                return
                            elif list1[2][1:].isnumeric() and 255 >= int(list1[2][1:]) >= 0:
                                output.append(right_shift_func(list1))

                            else:
                                print(
                                    "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                        j + x + 1))
                                return
        elif "ls" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("ERROR:Invalid 'ls' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "ls":
                            print("ERROR: Syntax for ls instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        else:
                            if list1[2] not in reg_list:
                                print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                                return
                            else:
                                if list1[3][0] != "$":
                                    print("ERROR: Immediate value is not defined properly, ERROR on line: " + str(
                                        j + x + 1))
                                    return
                                elif list1[3][1:].isnumeric() and 255 >= int(list1[3][1:]) >= 0:
                                    output.append(left_shift_func(list1[1:]))
                                else:
                                    print(
                                        "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                            j + x + 1))
                                    return
                else:
                    if list1[0] != "ls":
                        print("ERROR: Syntax for ls instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] not in reg_list:
                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            if list1[2][0] != "$":
                                print(
                                    "ERROR: Immediate value is not defined properly, ERROR on line: " + str(j + x + 1))
                                return
                            elif list1[2][1:].isnumeric() and 255 >= int(list1[2][1:]) >= 0:
                                output.append(left_shift_func(list1))

                            else:
                                print(
                                    "ERROR: Immediate value should be a number between 0 and 255 (both including), ERROR on line: " + str(
                                        j + x + 1))
                                return
        elif "div" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("ERROR:Invalid 'div' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "div":
                            print("ERROR: Syntax for div instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(div_func(list1[1:]))
                else:
                    if list1[0] != "div":

                        print("ERROR: Syntax for div instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(div_func(list1))

        elif "not" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("ERROR:Invalid 'not' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "not":

                            print(
                                "ERROR: Syntax for 'not' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(invert_func(list1[1:]))
                else:
                    if list1[0] != "not":

                        print("ERROR: Syntax for 'not' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(invert_func(list1))

        elif "cmp" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("ERROR:Invalid 'cmp' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "cmp":

                            print(
                                "ERROR: Syntax for 'cmp' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(compare_func(list1[1:]))
                else:
                    if list1[0] != "cmp":

                        print("ERROR: Syntax for 'cmp' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("ERROR: Invalid register used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(compare_func(list1))

        elif "jmp" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("ERROR:Invalid 'jmp' instruction on line: " + str(j + x + 1))
                return
            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "jmp":

                            print(
                                "ERROR: Syntax for 'jmp' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(unconditional_jump_func(list1[1:], labels))
                else:
                    if list1[0] != "jmp":

                        print("ERROR: Syntax for jmp instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif list1[1] not in labels:
                        print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(unconditional_jump_func(list1, labels))

        elif "jgt" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("ERROR:Invalid 'jgt' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "jgt":

                            print(
                                "ERROR: Syntax for 'jgt' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(jump_if_greater_func(list1[1:], labels))
                else:
                    if list1[0] != "jgt":

                        print("ERROR: Syntax for 'jgt' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif list1[1] not in labels:
                        print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(jump_if_greater_func(list1, labels))

        elif "jlt" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("ERROR:Invalid 'jlt' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "jlt":

                            print(
                                "ERROR: Syntax for 'jlt' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(jump_if_less_func(list1[1:], labels))
                else:
                    if list1[0] != "jlt":

                        print("ERROR: Syntax for 'jlt' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif list1[1] not in labels:
                        print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(jump_if_less_func(list1, labels))

        elif "je" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("ERROR:Invalid 'je' instruction on line: " + str(j + x + 1))
                return

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("ERROR: Label is not defined, ERROR on line: " + str(j + x + 1))
                        return
                    else:
                        if list1[1] != "je":

                            print("ERROR: Syntax for 'je' instruction is not correct, ERROR on line: " + str(j + x + 1))
                            return
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                            return
                        else:
                            output.append(jump_if_equal_func(list1[1:], labels))
                else:
                    if list1[0] != "je":

                        print("ERROR: Syntax for 'je' instruction is not correct, ERROR on line: " + str(j + x + 1))
                        return
                    elif list1[1] not in labels:
                        print("ERROR: Invalid label used, ERROR on line:" + str(j + x + 1))
                        return
                    else:
                        output.append(jump_if_equal_func(list1, labels))

        elif "hlt" in list1:

            if j + x != len(l) - 1:
                print("ERROR: Halt should be in the end, ERROR on line: " + str(j + x + 1))
                return
            if list1.count("hlt")>1:
                print("ERROR: Two halt instructions found, ERROR on line: "+ str(j+x+1))
                return
            output.append(halt_func())
        else:
            print("ERROR: Invalid instruction, ERROR on line: "+str(j + x + 1))
            return
    for s in output:
        print(s)
    # print(labels)
    # print(variables)
    #
    # string = "mov R2 $100"
    # l2 = string.split()
    # print(mov_imm_func(l2))


# 0001000100000100
# 0001001000000100
# 0111000000001010
# 0001100000011111
# 0001010000000001
# 0111000000011100
# 1000100000000111
# 1001100000000000
main()
