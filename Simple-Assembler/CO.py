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
    binary_code += "01000000"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def left_shift_func(l1):
    binary_code = ""
    binary_code += "01001000"
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


if __name__ == '__main__':
    labels = {}
    variables = {}
    flags = {}
    reg_list = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
    reg_list_fl = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS"]
    f = list(map(str, sys.stdin.readlines()))
    '''var x
    mov R1 $4
    mov R2 $4
    cmp R1 R2
    mov R3 FLAGS
    mov R4 $1
    cmp R3 R4
    jgt label
    label: hlt'''
    l = f
    j = 0
    for j in range(len(l)):
        j1 = l[j].strip()

        j1 = j1.strip("/n")

        list1 = j1.split()
        if "var" in list1:
            if len(list1) != 2 and len(list1) != 3:
                print("Error in statement.")
            elif len(list1) == 3:
                pass
            else:
                if list1[0] != "var":
                    print("Error in statement.")
                elif not list1[1].isalnum():
                    print("Error in statement.")
                else:

                    variables[list1[1]] = 0
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
            labels[list1[0][:-1]] = "0" * (8 - len(bin(x)[2:])) + bin(x)[2:]
        elif list1[0][-1] == ":":
            print("Error in statement.")
    for i in l[j:]:
        # print(i)
        i = i.strip()
        i = i.strip("/n")

        list1 = i.split()
        if "var" in list1:
            print("Error in statement.")
        elif "add" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "add":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(add_func(list1[1:]))
                else:
                    if list1[0] != "add":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):

                        print("Error in statement.")
                    else:
                        print(add_func(list1))

        elif "sub" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "sub":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(sub_func(list1[1:]))
                else:
                    if list1[0] != "sub":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(sub_func(list1))
        elif "mov" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("Error in statement.")
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "mov":
                            print("Error in statement.")
                        else:
                            if list1[2] not in reg_list:
                                print("Error in statement.")
                            else:
                                if list1[3] in reg_list_fl:
                                    print(mov_reg_func(list1[1:]))
                                else:
                                    if list1[3][0] != "$":
                                        print("Error in statement.")
                                    elif list1[2][1:].isnumeric() and 255 >= int(list1[2][1:]) >= 0:
                                        print(mov_imm_func(list1[1:]))
                                    else:
                                        print("Error in statement.")
                else:
                    if list1[0] != "mov":
                        print("Error in statement.")
                    else:
                        if list1[1] not in reg_list:
                            print("Error in statement.")
                        else:
                            if list1[2] in reg_list_fl:
                                print(mov_reg_func(list1))
                            else:
                                if list1[2][0] != "$":
                                    print("Error in statement.")
                                elif list1[2][1:].isnumeric() and 255 >= int(list1[2][1:]) >= 0:
                                    print(mov_imm_func(list1))

                                else:
                                    print("Error in statement.")
        elif "ld" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("Error in statement.")
            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "ld":
                            print("Error in statement.")
                        else:
                            if list1[2] not in reg_list:
                                print("Error in statement.")
                            else:
                                if list1[3] not in variables:
                                    print("Error in statement.")
                                else:
                                    print(load_func(list1[1:], variables))
                else:
                    if list1[0] != "ld":
                        print("Error in statement.")
                    else:
                        if list1[1] not in reg_list:
                            print("Error in statement.")
                        else:
                            if list1[2] not in variables:
                                print("Error in statement.")
                            else:
                                print(load_func(list1, variables))

        elif "st" in list1:
            if len(list1) != 3 and len(list1) != 4:
                print("Error in statement.")
            else:
                if len(list1) == 4:
                    if list1[0] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "st":
                            print("Error in statement.")
                        else:
                            if list1[2] not in reg_list:
                                print("Error in statement.")
                            else:
                                if list1[3] not in variables:
                                    print("Error in statement.")
                                else:
                                    print(store_func(list1[1:], variables))
                else:
                    if list1[0] != "st":
                        print("Error in statement.")
                    else:
                        if list1[1] not in reg_list:
                            print("Error in statement.")
                        else:
                            if list1[2] not in variables:
                                print("Error in statement.")
                            else:

                                print(store_func(list1, variables))
        elif "mul" in list1:
            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "mul":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(mul_func(list1[1:]))
                else:
                    if list1[0] != "mul":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):

                        print("Error in statement.")
                    else:
                        print(mul_func(list1))
        elif "and" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "and":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(sub_func(list1[1:]))
                else:
                    if list1[0] != "and":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(and_func(list1))
        elif "or" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "or":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(sub_func(list1[1:]))
                else:
                    if list1[0] != "or":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(or_func(list1))
        elif "xor" in list1:

            if len(list1) != 4 and len(list1) != 5:

                print("Error in statement.")

            else:
                if len(list1) == 5:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "xor":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list) or (list1[4] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(sub_func(list1[1:]))
                else:
                    if list1[0] != "xor":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list) or (list1[3] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(xor_func(list1))

        elif "div" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("Error in statement.")

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "div":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(div_func(list1[1:]))
                else:
                    if list1[0] != "div":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(div_func(list1))

        elif "not" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("Error in statement.")

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "not":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(invert_func(list1[1:]))
                else:
                    if list1[0] != "not":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(invert_func(list1))

        elif "cmp" in list1:

            if len(list1) != 3 and len(list1) != 4:

                print("Error in statement.")

            else:
                if len(list1) == 4:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "cmp":

                            print("Error in statement.")
                        elif (list1[2] not in reg_list) or (list1[3] not in reg_list):

                            print("Error in statement.")
                        else:
                            print(compare_func(list1[1:]))
                else:
                    if list1[0] != "cmp":

                        print("Error in statement.")
                    elif (list1[1] not in reg_list) or (list1[2] not in reg_list):
                        print("Error in statement.")
                    else:
                        print(compare_func(list1))

        elif "jmp" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("Error in statement.")

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "jmp":

                            print("Error in statement.")
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("Error in statement.")
                        else:
                            print(unconditional_jump_func(list1[1:], labels))
                else:
                    if list1[0] != "jmp":

                        print("Error in statement.")
                    elif list1[1] not in labels:
                        print("Error in statement.")
                    else:
                        print(unconditional_jump_func(list1, labels))

        elif "jgt" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("Error in statement.")

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "jgt":

                            print("Error in statement.")
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("Error in statement.")
                        else:
                            print(jump_if_greater_func(list1[1:], labels))
                else:
                    if list1[0] != "jgt":

                        print("Error in statement.")
                    elif (list1[1] not in labels):
                        print("Error in statement.")
                    else:
                        print(jump_if_greater_func(list1, labels))

        elif "jlt" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("Error in statement.")

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "jlt":

                            print("Error in statement.")
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("Error in statement.")
                        else:
                            print(jump_if_less_func(list1[1:], labels))
                else:
                    if list1[0] != "jlt":

                        print("Error in statement.")
                    elif (list1[1] not in labels):
                        print("Error in statement.")
                    else:
                        print(jump_if_less_func(list1, labels))

        elif "je" in list1:

            if len(list1) != 2 and len(list1) != 3:

                print("Error in statement.")

            else:
                if len(list1) == 3:
                    if list1[0][:-1] not in labels:
                        print("Error in statement.")
                    else:
                        if list1[1] != "je":

                            print("Error in statement.")
                        elif (list1[2] not in labels) or (list1[0][:-1] == list1[2]):

                            print("Error in statement.")
                        else:
                            print(jump_if_equal_func(list1[1:], labels))
                else:
                    if list1[0] != "je":

                        print("Error in statement.")
                    elif (list1[1] not in labels):
                        print("Error in statement.")
                    else:
                        print(jump_if_equal_func(list1, lables))

        # string = "mov R2 $100"
        # l2 = string.split()
        # print(mov_imm_func(l2))
        # elif "div" in list1:
        elif "hlt" in list1:
            print(halt_func())
    # print(labels)
    # print(variables)
    # string = "mov R2 $100"
    # l2 = string.split()
    # print(mov_imm_func(l2))

# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 0000100000001010
# 1001100000000000
