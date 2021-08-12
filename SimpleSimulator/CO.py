# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:18:59 2021

@author: HP
"""

dictionary_opcode = {"add": "00000", "sub": "00001", "mov1": "00010", "mov2": "00011", "ld": "00100", "st": "00101",
                     "mul": "00110", "div": "00111", "rs": "01000", "ls": "01001", "xor": "01010", "or": "01011",
                     "and": "01100", "not": "01101", "cmp": "01110", "jmp": "01111", "jlt": "10000", "jgt": "10001",
                     "je": "10010", "hlt": "10011"}
dictionary_reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110",
                  "FLAGS": "111"}


def add_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def sub_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def mul_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def or_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def and_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]] + dictionary_reg[l1[3]])
    return binary_code


def xor_code(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
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


def div_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def right_shift_func(l1):
    binary_code = ""
    binary_code += "00010"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def left_shift_func(l1):
    binary_code = ""
    binary_code += "00010"
    binary_code += (dictionary_reg[l1[1]])
    imm = int(l1[2][1:])
    converted = bin(imm)[2:]
    conv2 = "0" * (8 - len(converted)) + converted
    binary_code += conv2
    return binary_code


def invert_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def compare_func(l1):
    binary_code = ""
    binary_code += dictionary_opcode[l1[0]]
    binary_code += (dictionary_reg[l1[1]] + dictionary_reg[l1[2]])
    return binary_code


def halt_func(l1):
    binary_code = ""
    binary_code += (dictionary_opcode[l1[0]])
    binary_code += ("0" * 11)
    return binary_code


def main():
    string = "mov R2 $100"
    l2 = string.split()
    print(mov_imm_func(l2))


main()
