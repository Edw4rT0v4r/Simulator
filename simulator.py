#!/usr/bin/python3

from sys import argv

from src.afd.program import *
from src.mt.program import *


def simulator(data):
    p = open(data)
    aux_p = p.readlines()
    c_p = 0
    if len(aux_p):
        for line in aux_p:
            line = line.split()
            c_p = len(line)
            if c_p == 3:
                dictionary_afd(line)
            elif c_p == 5:
                dictionary_mt(line)
    p.close()
    return c_p


def readText(data, c_p):
    rt = open(data)
    aux_rt = rt.readlines()
    if len(aux_rt):
        for line in aux_rt:
            line = line.strip()
            if c_p == 3:
                print('La entrada', line, " es ", message[afd('0', line)])
            elif c_p == 5:
                data_line = {}
                v = '_'
                for ind, i in enumerate(line):
                    data_line[ind] = i

                position = 0
                print_result(data_line, ' Linea original')
                for ind, val in data_line.items():
                    if val == '*':
                        position = ind
                        data_line[ind] = '_'
                    if val == ' ':
                        data_line[ind] = '_'
                    v = data_line[position]

                print_result(data_line, ' Inicio')
                mt('0', v, position, data_line)
                break
            else:
                print("No se identifica el texto")
    else:
        if c_p == 3:
            afd()
        if c_p == 5:
            mt()
        else:
            print("No se identifica el texto")
    rt.close()


count_p = 0
for index, value in enumerate(argv):
    if index == 1:
        count_p = simulator(value)
        if len(argv) == 2:
            if count_p == 5:
                mt()
            else:
                print('Error Hace falta la cinta a leer')
    if index == 2:
        readText(value, count_p)
