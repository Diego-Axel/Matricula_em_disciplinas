''' Imports '''

import os

'''
Essas displinas são as que estão presentes no Excel que está disponivel para ser vizualizado/baixado na pasta 'arquivo_base' (coloquei apenas algumas matérias). Essas serão às matérias que o usuário podera se matricular.

'''

disciplinas = {
    "AAS0050":["Análise e Expressão Textual", "35N34"],
    "AAS0178":["Sociologia", "24N34"],
    "AAS0700":["Libras", "24N12"],
    "AEX0064":["Teoria da Computação", "2N1234"],
    "AEX0102":["Calculo II", "24N12"],
    "AEX0106":["Engenharia de Requisitos", "6T2345"],
    "AEX0149":["Introdução a computação e Sistemas de Informação", "35N12"],
    "AEX0152":["Princípios de Engenharia de Software", "4N1234"],
    "AEX0153":["Logica e Matemática Discreta", "2N1234"],
    "AEX0157":["Fundamentos de Banco de Dados", "4N34", "5N12"],
    "AEX0158":["Algoritmos e Programação III", "6N1234"],
    "AEX0159":["Analise e Projeto de Sistemas", "3N12", "5N34"],
    "AEX0162":["Gerencia de Projetos", "6N1234"],
    "AEX0163":["Sistemas Operacionais", "4N12", "5N34"],
    "AEX0171":["Tecnologia e Sociedade", "3N12", "5N34"],
    "AEX0172":["Aspectos Filosóficos e Sociológicos de Informática", "35N34"],
    "AEX0184":["Infraestrutura de Hardware", "3N34", "5N12"],
    "AEX0185":["Paradigmas de Programação", "4T2345"],
    "AEX0187":["Aprendizado de Máquina", "5T2345"]
}


'''
Dicionário que guadará as disciplinas que o úsuario escolher, junto com os seus turnos e código
'''
escolhas = {}


def menu_principal():
    os.system('clear || cls')
    print("-----------------------------------------------------")
    print("| SISTEMA DE MÁTRICULAS EM DISCIPLINAS CURRICULARES |")
    print("|                 SEJA BEM VINDO(A)                 |")
    print("|                                                   |")
    print("|                 1 - MATRICULAR-SE                 |")
    print("|                 2 - EXIBIR DISCIPLINAS            |")
    print("|                 3 - ALTERAR DISCIPLINA            |")
    print("|                 4 - EXCLUIR DISCIPLINA            |")
    print("|                 0 - SAIR                          |")
    print("-----------------------------------------------------")
    print()
    op_principal = input("| Escolha uma opção: ")
    return op_principal



def matricula():
    os.system('clear || cls')
    print("-------------------------------------------------------------------------------------------")
    print("|     CÓDIGO    |                        DISCIPLINA                       |   TURNO/DIA   |")
    print("-------------------------------------------------------------------------------------------")
    print("|    AAS0050    |                Análise e Expressão Textual              |     35N34     |")
    print("|    AAS0178    |                         Sociologia                      |     24N34     |")
    print("|    AAS0700    |                           Libras                        |     24N34     |")
    print("|    AEX0064    |                    Teoria da Computação                 |     2N1234    |")
    print("|    AEX0102    |                         Calculo II                      |     24N12     |")
    print("|    AEX0106    |                  Engenharia de Requisitos               |     24N12     |")
    print("|    AEX0149    |     Introdução a computação e Sistemas de Informação    |     35N12     |")
    print("|    AEX0152    |             Princípios de Engenharia de Software        |     4N1234    |")
    print("|    AEX0153    |                Logica e Matemática Discreta             |     24N34     |")
    print("|               |                                                         |               |")
    print("|    AEX0157    |               Fundamentos de Banco de Dados             |     24N34     |")
    print("|               |                                                         |     5N12      |")
    print("|               |                                                         |               |")
    print("|    AEX0158    |                Algoritmos e Programação III             |     24N34     |")
    print("|               |                                                         |               |")
    print("|    AEX0159    |                Analise e Projeto de Sistemas            |     3N12      |")
    print("|               |                                                         |     5N34      |")
    print("|               |                                                         |               |")
    print("|    AEX0162    |                    Gerencia de Projetos                 |     6N1234    |")
    print("|    AEX0163    |                    Sistemas Operacionais                |     24N34     |")
    print("|    AEX0171    |                    Tecnologia e Sociedade               |     3N12      |")
    print("|    AEX0172    |    Aspectos Filosóficos e Sociológicos de Informática   |     24N34     |")
    print("|    AEX0184    |                  Infraestrutura de Hardware             |     3N34      |")
    print("|    AEX0185    |                  Paradigmas de Programação              |     4T2345    |")
    print("|    AEX0187    |                   Aprendizado de Máquina                |     5T2345    |")
    print("-------------------------------------------------------------------------------------------")


















# Programa Principal:

op_principal = ""

while op_principal != "0":
    op_principal = menu_principal()
    print()
    if op_principal == "1":
        matricula()