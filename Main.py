import os
class ficha:
    def __init__(self,nome,cpf,setor):
        self.nome = nome
        self.cpf = cpf
        self.setor = setor
f = ficha
f.nome = []
f.cpf = []
f.setor = []
nomevar = ""
cpfvar = ""
setorvar = ""
menu = teste = max = safe = listarsetor = 0
while(menu != 4):
    print("Bem-vindo ao sistema de atendimento\n1 - Solicitar atendimento\n2 - Listar Atendimentos Registrados\n3 - Listar Atendimentos por Setor")
    menu = int(input("4 - Sair\n"))
    if menu == 1:
        nomevar = input("Digite seu nome:")
        f.nome.append(nomevar)
        cpfvar = ""
        while(len(cpfvar) != 11):
            cpfvar = input("Digite seu CPF:")
            if (len(cpfvar)!= 11):
                print("CPF Inválido")
                os.system("Pause")
        f.cpf.append(cpfvar)
        setorvar = ""
        safe = 0
        while(safe != 1):
            setorvar = (
                int(input("Setor Desejado:\n1 - Abertura de Conta\n2 - Caixa\n3 - Gerente Pessoa Física\n4 - Gerente Pessoa Jurídica\n")))
            if setorvar >= 1 and setorvar <= 4:
                safe = 1
            else:
                print("Setor Inválido")
                os.system("Pause")
        f.setor.append(setorvar)
        max = max + 1
    elif menu == 2:
        print("Atendimentos Registrados:\n===============================")
        for i in range(0,max):
            print(f.nome[i])
            print(f.cpf[i])
            if f.setor[i] == 1:
                print("Abertura de Conta")
            elif f.setor[i] == 2:
                print("Caixa")
            elif f.setor[i] == 3:
                print("Gerente Pessoa Física")
            elif f.setor[i] == 4:
                print("Gerente Pessoa Jurídica")
            print("===============================")
        print("Fim Dos Atendimentos Registrados")
    elif menu == 3:
        i = 0
        listarsetor = int(input("Escolha o setor desejado:\n1 - Abertura de Conta\n2 - Caixa\n3 - Gerente Pessoa Física\n4 - Gerente Pessoa Jurídica"))
        if listarsetor == 1:
            print("\n===============================")
            for i in range(0, max):
                if f.setor[i] == 1:
                    print(f.nome[i])
                    print(f.cpf[i])
                    print("Abertura de Conta")
            print("===============================\nFim dos Atendimentos Nesse Setor\n")
        elif listarsetor == 2:
            print("\n===============================")
            for i in range(0, max):
                if f.setor[i] == 2:
                    print(f.nome[i])
                    print(f.cpf[i])
                    print("Caixa")
            print("===============================\nFim dos Atendimentos Nesse Setor\n")
        elif listarsetor == 3:
            print("\n===============================")
            for i in range(0, max):
                if f.setor[i] == 3:
                    print(f.nome[i])
                    print(f.cpf[i])
                    print("Gerente Pessoa Física")
            print("===============================\nFim dos Atendimentos Nesse Setor\n")
        elif listarsetor == 4:
            print("\n===============================")
            for i in range(0, max):
                if f.setor[i] == 4:
                    print(f.nome[i])
                    print(f.cpf[i])
                    print("Gerente Pessoa Jurídica")
            print("===============================\nFim dos Atendimentos Nesse Setor\n")
    elif menu == 4:
        print("Tenha um bom dia")
    else:
        print("Opção Inexistente")
        os.system("Pause")