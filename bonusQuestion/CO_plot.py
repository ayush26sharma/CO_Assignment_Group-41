import sys
import os
import matplotlib.pyplot as plt

dictionary_opcode = {"add": "00000", "sub": "00001", "mov1": "00010", "mov2": "00011", "ld": "00100", "st": "00101",
                     "mul": "00110", "div": "00111", "rs": "01000", "ls": "01001", "xor": "01010", "or": "01011",
                     "and": "01100", "not": "01101", "cmp": "01110", "jmp": "01111", "jlt": "10000", "jgt": "10001",
                     "je": "10010", "hlt": "10011"}


def funcToPrint(dict_reg_l):
    str1 = ""
    for i in dict_reg_l:
        str1 += "0" *(16 - len(str(bin(dict_reg_l[i]))[2:])) + str(bin(dict_reg_l[i]))[2:] +" "
    # str1.strip()
    return str1

def main():
    # labels = {}
    # variables = {}
    # output = []
    # labels_check = ["add", "sub", "mov", "ld", "st",
    #                 "mul", "div", "rs", "ls", "xor", "or",
    #                 "and", "not", "cmp", "jmp", "jlt", "jgt",
    #                 "je", "hlt"]
    # reg_list = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
    # reg_list_fl = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS"]
    l = list(map(str, sys.stdin.readlines()))
    #f = open('Readme.txt', mode='r+')
    #l = f.readlines()
    # print(l)
    variables = {}
    dict_flags = {"V": "0", "L": "0", "G": "0", "E": "0"}
    dict_reg = {"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}
    regValues = {"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}
    i = 0
    arr = [[0,0]]
    ct = 0
    while i < len(l):
        l[i] = l[i].strip()

        l[i] = l[i].strip("/n")

        if l[i][:5]=="00000":
            sum1 = regValues[dict_reg[l[i][10:13]]] + regValues[dict_reg[l[i][13:]]]
            if (sum1) > (2 ** 16 - 1):
                dict_flags["V"] = "1"
                sum1 = sum1 - (2 ** 16)
            elif (sum1) < 0:
                dict_flags["V"] = "1"
                sum1 = 0
            else:
                dict_flags["V"] = "0"
            regValues[dict_reg[l[i][7:10]]] = sum1
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])

        elif l[i][:5]=="00001":
            diff1 = regValues[dict_reg[l[i][10:13]]] - regValues[dict_reg[l[i][13:]]]
            if (diff1) > (2 ** 16 - 1):
                dict_flags["V"] = "1"
                diff1 = diff1 - (2 ** 16)
            elif (diff1) < 0:
                dict_flags["V"] = "1"
                diff1 = 0
            else:
                dict_flags["V"] = "0"
            regValues[dict_reg[l[i][7:10]]] = diff1
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])

        elif l[i][:5] == "00010":
            regValues[dict_reg[l[i][5:8]]] = int(l[i][8:],2)
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "00011":
            if l[i][13:]=="111":
                flagSum = 0
                for x in dict_flags:
                    if x=="V" and dict_flags[x] == "1":
                        flagSum+= 8
                    if x=="L" and dict_flags[x] == "1":
                        flagSum+= 4
                    if x=="G" and dict_flags[x] == "1":
                        flagSum+= 2
                    if x=="E" and dict_flags[x] == "1":
                        flagSum+= 1

                regValues[dict_reg[l[i][10:13]]] = flagSum
            else:
                regValues[dict_reg[l[i][10:13]]] = regValues[dict_reg[l[i][13:]]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5]=="00100":
            if l[i][8:] not in variables:
                variables[l[i][8:]] = 0
                regValues[dict_reg[l[i][5:8]]] = 0
            else:
                regValues[dict_reg[l[i][5:8]]] = variables[l[i][8:]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
            arr.append([ct,int(l[i][8:],2)])
        elif l[i][:5] =="00101":
            variables[l[i][8:]] = regValues[dict_reg[l[i][5:8]]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])
            arr.append([ct,int(l[i][8:],2)])
        elif l[i][:5] == "00110":
            sum1 = regValues[dict_reg[l[i][10:13]]] * regValues[dict_reg[l[i][13:]]]
            if (sum1) > (2 ** 16 - 1):
                dict_flags["V"] = "1"
                sum1 = sum1 - (2 ** 16)
            elif (sum1) < 0:
                dict_flags["V"] = "1"
                sum1 = 0
            else:
                dict_flags["V"] = "0"
            regValues[dict_reg[l[i][7:10]]] = sum1
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "00111":
            quotient = regValues[dict_reg[l[i][10:13]]] // regValues[dict_reg[l[i][13:]]]
            rem = regValues[dict_reg[l[i][10:13]]] % regValues[dict_reg[l[i][13:]]]
            if (quotient) > (2 ** 16 - 1):
                dict_flags["V"] = "1"
                quotient = quotient - (2 ** 16)
            elif (quotient) < 0:
                dict_flags["V"] = "1"
                quotient = 0
            else:
                dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            regValues["R0"] = quotient
            regValues["R1"] = rem
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01000":
            regValues[dict_reg[l[i][5:8]]] //= 2** int(l[i][8:],2)
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01001":
            temp = regValues[dict_reg[l[i][5:8]]]
            temp = 2 * int(l[i][8:],2)
            if temp > (2**16-1):
                temp1 = bin(temp)[2:]
                temp = int(temp1[len(temp1)-16:], 2)
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            regValues[dict_reg[l[i][5:8]]] = temp
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01010":
            regValues[dict_reg[l[i][7:10]]] = regValues[dict_reg[l[i][10:13]]] ^ regValues[dict_reg[l[i][13:]]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01100":
            regValues[dict_reg[l[i][7:10]]] = regValues[dict_reg[l[i][10:13]]] & regValues[dict_reg[l[i][13:]]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01100":
            regValues[dict_reg[l[i][7:10]]] = regValues[dict_reg[l[i][10:13]]] | regValues[dict_reg[l[i][13:]]]
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01101":
            for j in regValues[dict_reg[l[i][13:]]]:
                if j=='1':
                    j='0'
                else:
                    j='1'
            regValues[dict_reg[l[i][10:13]]] = int(regValues[dict_reg[l[i][13:]]],2)            
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01110":
            x = regValues[dict_reg[l[i][10:13]]]
            y = regValues[dict_reg[l[i][13:]]]
            dict_flags["V"] = "0"
            if x<y:
                dict_flags["L"] = "1"
            elif x>y:
                dict_flags["G"] = "1"
            elif x==y:
                dict_flags["E"] = "1"
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i += 1
            ct+=1
            arr.append([ct,i])
        elif l[i][:5] == "01111":
            pc = str(bin(i))[2:]
            i = int(l[i][8:],2)
            ct+=1
            arr.append([ct,i])
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"

            conv2 = "0" * (8 - len(pc)) + pc
        elif l[i][:5] == "10000":
            pc = str(bin(i))[2:]
            if dict_flags["L"]=='1':
                i = int(l[i][8:],2)
                ct+=1
                arr.append([ct,i])
            else:
                i+=1
                ct+=1
                arr.append([ct,i])
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"

            conv2 = "0" * (8 - len(pc)) + pc
        elif l[i][:5] == "10001":
            pc = str(bin(i))[2:]
            if dict_flags["G"]=='1':
                i = int(l[i][8:],2)
                ct+=1
                arr.append([ct,i])
            else:
                i+=1
                ct+=1
                arr.append([ct,i])
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"

            conv2 = "0" * (8 - len(pc)) + pc
        elif l[i][:5] == "10010":
            pc = str(bin(i))[2:]
            if dict_flags["E"]=='1':
                i = int(l[i][8:],2)
                ct+=1
                arr.append([ct,i])
            else:
                i+=1
                ct+=1
                arr.append([ct,i])
            dict_flags["V"] = "0"
            dict_flags["L"] = "0"
            dict_flags["G"] = "0"
            dict_flags["E"] = "0"

            conv2 = "0" * (8 - len(pc)) + pc

        elif l[i][:5] == "10011":
            pc = str(bin(i))[2:]
            conv2 = "0" * (8 - len(pc)) + pc
            i+=1
            ct+=1
            arr.append([ct,i])
    totalNum = 256 - (len(l) + len(variables))
    print(arr)
    x_axis =[]
    y_axis =[]
    for i in arr:
        x_axis.append(i[0])
        y_axis.append(i[1])
    plt.scatter(x_axis,y_axis,c= "blue")
    plt.xlabel("Cycle(s)")
    plt.ylabel("Memory Address")
    plt.title("Bonus Question: Scatter Plot")
    plt.show()
main()
