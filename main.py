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