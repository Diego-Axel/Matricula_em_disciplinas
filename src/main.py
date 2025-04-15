import os

# Dicionário de disciplinas disponíveis
disciplinas = {
    "AAS0050": ["Análise e Expressão Textual", "35N34"],
    "AAS0178": ["Sociologia", "24N34"],
    "AAS0700": ["Libras", "24N12"],
    "AEX0064": ["Teoria da Computação", "2N1234"],
    "AEX0102": ["Cálculo II", "24N12"],
    "AEX0106": ["Engenharia de Requisitos", "6T2345"],
    "AEX0149": ["Introdução a Computação e Sistemas de Informação", "35N12"],
    "AEX0152": ["Princípios de Engenharia de Software", "4N1234"],
    "AEX0153": ["Lógica e Matemática Discreta", "2N1234"],
    "AEX0157": ["Fundamentos de Banco de Dados", "4N34", "5N12"],
    "AEX0158": ["Algoritmos e Programação III", "6N1234"],
    "AEX0159": ["Análise e Projeto de Sistemas", "3N12", "5N34"],
    "AEX0162": ["Gerência de Projetos", "6N1234"],
    "AEX0163": ["Sistemas Operacionais", "4N12", "5N34"],
    "AEX0171": ["Tecnologia e Sociedade", "3N12", "5N34"],
    "AEX0172": ["Aspectos Filosóficos e Sociológicos de Informática", "35N34"],
    "AEX0184": ["Infraestrutura de Hardware", "3N34", "5N12"],
    "AEX0185": ["Paradigmas de Programação", "4T2345"],
    "AEX0187": ["Aprendizado de Máquina", "5T2345"]
}

# Lista de disciplinas matriculadas pelo aluno
disciplinas_matriculadas = []


def exibir_menu():
    os.system('clear || cls')
    print("-----------------------------------------------------")
    print("| SISTEMA DE MATRÍCULAS EM DISCIPLINAS CURRICULARES |")
    print("|                 SEJA BEM-VINDO(A)                 |")
    print("|                                                   |")
    print("|  1 - MATRICULAR-SE                                |")
    print("|  2 - EXIBIR TODAS AS DISCIPLINAS DISPONÍVEIS      |")
    print("|  3 - ALTERAR DISCIPLINA MATRICULADA               |")
    print("|  4 - EXCLUIR DISCIPLINA MATRICULADA               |")
    print("|  5 - MINHAS DISCIPLINAS MATRICULADAS              |")
    print("|  0 - SAIR                                         |")
    print("-----------------------------------------------------")
    return input("Escolha uma opção: ")


def exibir_disciplinas(dados):
    os.system('clear || cls')
    print("\nLISTA DE DISCIPLINAS:")
    for codigo, detalhes in dados.items():
        print(f"{codigo} - {detalhes[0]} ({', '.join(detalhes[1:])})")
    print()


def matricular():
    exibir_disciplinas(disciplinas)
    codigo = input("Digite o código da disciplina que deseja se matricular: ").strip().upper()

    if codigo not in disciplinas:
        print("❌ Código inválido.")
    elif codigo in disciplinas_matriculadas:
        print("⚠️ Você já está matriculado(a) nessa disciplina.")
    else:
        disciplinas_matriculadas.append(codigo)
        print("✅ Matrícula realizada com sucesso!")


def alterar_disciplina():
    os.system('clear || cls')
    if not disciplinas_matriculadas:
        print("⚠️ Você ainda não está matriculado em nenhuma disciplina.")
        return

    print("\nDISCIPLINAS MATRICULADAS:")
    for i, codigo in enumerate(disciplinas_matriculadas, 1):
        print(f"{i}. {codigo} - {disciplinas[codigo][0]}")

    try:
        indice = int(input("Digite o número da disciplina que deseja substituir: ")) - 1
        if 0 <= indice < len(disciplinas_matriculadas):
            exibir_disciplinas(disciplinas)
            novo_codigo = input("Digite o novo código da disciplina: ").strip().upper()

            if novo_codigo not in disciplinas:
                print("❌ Código inválido.")
            elif novo_codigo in disciplinas_matriculadas:
                print("⚠️ Você já está matriculado nessa disciplina.")
            else:
                disciplinas_matriculadas[indice] = novo_codigo
                print("✅ Disciplina alterada com sucesso.")
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("❌ Entrada inválida.")


def excluir_disciplina():
    os.system('clear || cls')
    if not disciplinas_matriculadas:
        print("⚠️ Nenhuma disciplina matriculada.")
        return

    print("\nDISCIPLINAS MATRICULADAS:")
    for i, codigo in enumerate(disciplinas_matriculadas, 1):
        print(f"{i}. {codigo} - {disciplinas[codigo][0]}")

    try:
        indice = int(input("Digite o número da disciplina que deseja excluir: ")) - 1
        if 0 <= indice < len(disciplinas_matriculadas):
            removida = disciplinas_matriculadas.pop(indice)
            print(f"✅ Disciplina {removida} removida com sucesso.")
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("❌ Entrada inválida.")


def minhas_disciplinas():
    os.system('clear || cls')
    if not disciplinas_matriculadas:
        print("⚠️ Você não está matriculado em nenhuma disciplina.")
    else:
        print("\nMINHAS DISCIPLINAS:")
        for codigo in disciplinas_matriculadas:
            print(f"{codigo} - {disciplinas[codigo][0]} ({', '.join(disciplinas[codigo][1:])})")
        print()


verificador = True
while verificador:
    opcao = exibir_menu()
    if opcao == '1':
        matricular()
    elif opcao == '2':
        exibir_disciplinas(disciplinas)
    elif opcao == '3':
        alterar_disciplina()
    elif opcao == '4':
        excluir_disciplina()
    elif opcao == '5':
        minhas_disciplinas()
    elif opcao == '0':
        print("👋 Saindo... Até logo!")
        verificador = False
    else:
        print("❌ Opção inválida. Tente novamente.")
        print()
    input("Pressione Enter para continuar...")