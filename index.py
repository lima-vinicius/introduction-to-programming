"""
Federal University of Pernambuco - Brazil.
Computer Center(CIn) (http://www.cin.ufpe.br)
Information System Undergraduate
IF968 - Programação 01 \n
Author: Vinicius Rafael Pereira Lima 
Email: vrpl@cin.ufpe.br
Copyright(c) 2019 Vinícius Rafael Pereira de Lima\n
"""

# Date and time function
def datetime ():
    '''Function to return the current date and time'''
    from datetime import datetime
    data = datetime.now()   
    datahora = data.strftime("%d/%m/%Y %H:%M")
    return datahora

#RECEPTION PROGRAM

# All functions to read file
def lerArquivoUsuario():
    '''Function to return patients registered in a dictionary'''
    arquivo = open("users.txt", "r")
    elementos = arquivo.readlines()
    arquivo.close()
    tupla = elementosTupla(elementos)
    dic = lerDicionarioUsuario(tupla)
    return dic

def elementosTupla(elementos):
    '''Function to return patients registered in a tuple'''
    tupla = ()
    for palavras in elementos:
        tupla += (palavras, )
    tuplaNova = ()
    stringNova = ""
    for elemento in tupla:
        for caractere in elemento:
            if caractere != "\n":
                stringNova += caractere
            else:
                tuplaNova += (stringNova, )
                stringNova = ""
    return tuplaNova

def lerDicionarioUsuario(tupla):
    '''Function to return a dictionary of registered patients'''
    dic = {}
    cont = 0
    while(cont < len(tupla)):
        dic[tupla[cont]] = tupla[cont+1 : cont+11]
        cont += 11
    return dic

#All the functions to writing
def criacaoCadastro():
    '''Function to create a patient record'''
    print("<-------------------------------------------->")
    cpf = int(input("CPF: "))
    nome = input("Nome completo: ")
    rg = input("RG: ")
    idade = input("Idade: ")
    estado = input("UF: ")
    cidade = input("Cidade: ")
    rua = input("Rua: ")
    numero = input("Numero: ")
    data = datetime()
    dataAtualizacao = datetime()
    dataConsulta = datetime()
    print("Cadastro Realizado")
    print("<-------------------------------------------->")
    adicionarDicionario(nome, cpf, rg, idade, estado, cidade, rua, numero, data, dataAtualizacao, dataConsulta)

def adicionarDicionario(nome, cpf, rg, idade, estado, cidade, rua, numero, data, dataAtualizacao, dataConsulta):
    '''Function to add the patient record to a dictionary'''
    dic = lerArquivoUsuario()
    dic[cpf] = ((nome), (rg), (idade), (estado), (cidade), (rua), (numero), (data), (dataAtualizacao), (dataConsulta))
    escreverArquivo(dic)

def escreverArquivo(dic):
    '''Function to write the patient's record in a txt file'''
    arquivo = open("users.txt", "w")
    for chave in dic:
        arquivo.write(str(chave))
        arquivo.write("\n")
        for elementos in dic[chave]:
            arquivo.write(str(elementos))
            arquivo.write("\n")
    arquivo.close()

#Check Registration
def checarCadastro():
    '''Function to check if there is a patient record'''
    dic = lerArquivoUsuario()
    chaves = dic.keys()
    cpf = input("Paciente(CPF): ")
    cont = 0
    for chave in chaves:
        if(chave == cpf):
            cont+=1
    if(cont == 0):
        print("Paciente não cadastrado")
    return (cpf, cont)

#View registration
def lerCadastro():
    '''Function to view patient record'''
    dic = lerArquivoUsuario()
    chave = checarCadastro()
    if(chave[1] == 1):
        print("<-------------------------------------------->")
        print("\nNome: {}".format(dic[chave[0]][0]))
        print("RG: {}".format(dic[chave[0]][1]))
        print("Idade: {}".format(dic[chave[0]][2]))
        print("UF: {}".format(dic[chave[0]][3]))
        print("Cidade: {}".format(dic[chave[0]][4]))
        print("Rua: {}".format(dic[chave[0]][5]))
        print("Número: {}".format(dic[chave[0]][6]))
        print("Data do cadastro: {}".format(dic[chave[0]][7]))
        print("Data da última autalização: {}\n".format(dic[chave[0]][8]))
        print("Data da última Consulta: {}\n".format(dic[chave[0]][9]))
        print("<-------------------------------------------->")

#Updating Patient Registration
def atualizar ():
    '''Function to update patient record information'''
    dic = lerArquivoUsuario()
    chave = checarCadastro()
    if(chave[1] == 1):
        print("<-------------------------------------------->")
        print("1- Idade 2- Estado 3- Cidade 4- Rua 5- Número")
        resp = int(input("Digite o número correspondente a informação que deseja atualizar: "))
        informacao = input("Digite a nova informação: ")
        if(resp == 1):
            dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], informacao, dic[chave[0]][3], dic[chave[0]][4], dic[chave[0]][5], dic[chave[0]][6], dic[chave[0]][7], dic[chave[0]][8], dic[chave[0]][9])
        if(resp == 2):
            dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], dic[chave[0]][2], informacao, dic[chave[0]][4], dic[chave[0]][5], dic[chave[0]][6], dic[chave[0]][7], dic[chave[0]][8], dic[chave[0]][9])
        if(resp == 3):
            dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], dic[chave[0]][2], dic[chave[0]][3], informacao, dic[chave[0]][5], dic[chave[0]][6], dic[chave[0]][7], dic[chave[0]][8], dic[chave[0]][9])
        if(resp == 4):
            dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], dic[chave[0]][2], dic[chave[0]][3], dic[chave[0]][4], informacao, dic[chave[0]][6], dic[chave[0]][7], dic[chave[0]][8], dic[chave[0]][9])
        if(resp == 5):
            dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], dic[chave[0]][2], dic[chave[0]][3], dic[chave[0]][4], dic[chave[0]][5], informacao, dic[chave[0]][7], dic[chave[0]][8], dic[chave[0]][9])
        dic[chave[0]] = (dic[chave[0]][0], dic[chave[0]][1], dic[chave[0]][2], dic[chave[0]][3], dic[chave[0]][4], dic[chave[0]][5], dic[chave[0]][6], dic[chave[0]][7], datetime(), dic[chave[0]][9])
        print("Informação Atualizada")
        print("<-------------------------------------------->")
        escreverArquivo(dic)

#Deleting Patient registration
def excluirCadastro():
    '''Function to delete patient registration'''
    dic = lerArquivoUsuario()
    print("<-------------------------------------------->")
    chave = input("Usuario(CPF):")
    del(dic[chave])
    print("Cadastro do paciente excluido")
    print("<-------------------------------------------->")
    escreverArquivo(dic)

# Waiting List (Reception)
def lerArquivoEspera():
    '''Function to read patients on the waiting list'''
    arquivo = open("listadeespera.txt", "r")
    elementos = arquivo.readlines()
    arquivo.close()
    tupla = elementosTupla(elementos)
    return tupla

def listaEspera():
    '''Function to add a patient to the waiting list'''
    tupla = lerArquivoEspera()
    print("<-------------------------------------------->")
    chave = checarCadastro()
    if (chave[1] == 1):
        dic = lerArquivoUsuario()
        usuario = dic[chave[0]]
        sintoma1 = input("Qual sintoma 1: ")
        sintoma2 = input("Qual sintoma 2: ")
        print("<-------------------------------------------->")
        tupla += (usuario[0], usuario[2], sintoma1, sintoma2, usuario[9],)
        user = chave[0]
        atualizarConsulta(user)
    escreverEspera(tupla)
    if (chave[1] == 0):
        print("<-------------------------------------------->")
        print("Para realizar uma consulta, o paciente precisa estar cadastrado!")
        resp = int(input("Fazer Cadastro(1- SIM 2-NÃO): "))
        print("<-------------------------------------------->")
        if(resp == 1):
            criacaoCadastro()
            listaEspera()

#Update last registration
def atualizarConsulta(chave):
    '''Function to modify the date and time of the patient's last appointment'''
    dic = lerArquivoUsuario()
    dic[chave] = (dic[chave][0], dic[chave][1], dic[chave][2], dic[chave][3], dic[chave][4], dic[chave][5], dic[chave][6], dic[chave][7], dic[chave][8], datetime())
    escreverArquivo(dic)

#Write to wait list
def escreverEspera(tupla):
    '''Function to write the patient on the waiting list'''
    arquivo = open("waitinglist.txt", "w")
    for elemento in tupla:
        arquivo.write(str(elemento))
        arquivo.write("\n")
    arquivo.close()

#DOCTOR PROGRAM

def quantidadePessoa():
    '''Function to return the number of patients on the waiting list'''
    from math import floor
    tupla = lerArquivoEspera()
    qntPessoa = floor(len(tupla) / 5)
    print("<-------------------------------------------->")
    print("No momento existem {} Pessoas na lista de espera".format(qntPessoa))
    print("<-------------------------------------------->")

def exibirEspera():
    '''Function to read patient data on the waiting list and end consultation'''
    tupla = lerArquivoEspera()
    cont = 0
    while(cont < len(tupla)):
        print("<-------------------------------------------->")
        print("Nome: {}\nIdade: {}\nSintoma1: {}\nSintoma2: {}".format(tupla[cont], tupla[cont+1],tupla[cont+2],tupla[cont+3]))
        resp = int(input("Terminar Consulta?(1- SIM):"))
        print("<-------------------------------------------->")
        if(resp == 1):
            cont += 5
    arquivo = open("listadeespera.txt", "w")
    arquivo.close()
    print("<-------------------------------------------->")
    print("Não tem pacientes na lista de espera")
    print("<-------------------------------------------->")

#DIRECTOR PROGRAM

#File Information
def informacaoChaves ():
    '''Function to return patient and employee registration keys'''
    dic1 = lerArquivoUsuario()
    dic2 = lerArquivoLogin()
    print("<-------------------------------------------->")
    resp = int(input("1- Cadastro dos Pacientes 2- Cadastro dos Funcionarios: "))
    if (resp == 1):
        for chave in dic1:
            print("\nChave de Acesso: {}\nNome: {}\n".format(chave, dic1[chave][0]))
            print("<-------------------------------------------->")
        resp1 = int(input("Deseja acessar informações?(1- SIM 2- NÃO):"))
        
        if(resp1 == 1):
            lerCadastro()
            print("<-------------------------------------------->")
    if (resp == 2):
        print("\nNiveis de Acesso: 1- Recepção 2- Médico 3- Direção\n")
        for chave in dic2:
            print("Chave de Acesso: {}\nSenha: {}\nNome: {}\nNível Acesso: {}\n".format(chave, dic2[chave][1], dic2[chave][2], dic2[chave][0]))
        print("<-------------------------------------------->")

def totalCadastro():
    '''Function to return the amount of registration of Patients and Staff'''
    dic1 = lerArquivoUsuario()
    dic2 = lerArquivoLogin()
    qntPaciente = len(dic1)
    qntLogin = len(dic2)
    print("<-------------------------------------------->")
    resp = int(input("1- Quantidade de Funcionários 2- Quantidade de Pacientes: "))
    if(resp == 1):
        print("\nAtualmente o Hospistal possui {} funcionários\n".format(qntLogin))
        print("<-------------------------------------------->")
    elif(resp == 2):
        print("\nAtualmente o Hospital possui {} Pacientes\n".format(qntPaciente))
        print("<-------------------------------------------->")

#Promote employee
def promover ():
    '''Function to modify the employee's access level'''
    dic = lerArquivoLogin()
    print("<-------------------------------------------->")
    print("1- Recepcao 2- Médico 3- Diretor")
    for chave in dic:
        print("\nNome: {}\nChave: {}\nNivel De Acesso: {}\n".format(dic[chave][2], chave, dic[chave][0]))
    chave = input("Digite a chave do funcionário: ")
    nivel = input("1- Recepcao 2- Médico 3- Diretor: ")
    dic[chave] = (nivel, dic[chave][1], dic[chave][2])
    print("Funcionario Promovido")
    print("<-------------------------------------------->")
    escreverArquivoLogin(dic)

#Delete employee registration
def excluirFuncionario():
    '''Function to delete employee registration'''
    dic = lerArquivoLogin()
    informacaoChaves()
    print("<-------------------------------------------->")
    chave = input("Digite a chave:")
    del(dic[chave])
    print("Cadastro do funcionario excluido")
    print("<-------------------------------------------->")
    escreverArquivoLogin(dic)

#Login
def lerArquivoLogin():
    '''Function to return a dictionary of registered logins'''
    arquivo = open("login.txt", "r")
    elementos = arquivo.readlines()
    arquivo.close()
    tupla = elementosTupla(elementos)
    dic = criarDicionarioLogin(tupla)
    chaves = dic.keys()
    if(("") in chaves):
        del(dic[""])
    return dic

def criarDicionarioLogin(tupla):
    '''Function for placing login data in a dictionary'''
    dic = {}
    cont = 0
    while(cont < len(tupla)):
        dic[tupla[cont]] = tupla[cont+1 : cont+4]
        cont += 4
    return dic

def criarLogin():
    '''Function to create a login'''
    print("<-------------------------------------------->")
    acesso = input("1- Recepção 2- Médico: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")
    print("Funcionario cadastrado")
    print("<-------------------------------------------->")
    adicionarDicionarioLogin(cpf, acesso, senha, nome)

def adicionarDicionarioLogin(cpf, acesso, senha, nome):
    '''Function to put the registered login data in a dictionary'''
    dic = lerArquivoLogin() 
    dic[cpf] = ((acesso), (senha), (nome))
    escreverArquivoLogin(dic)

def escreverArquivoLogin(dic):
    '''Function to write registered logins'''
    arquivo = open("login.txt", "w")
    for chave in dic:
        arquivo.write(str(chave))
        arquivo.write("\n")
        for elementos in dic[chave]:
            arquivo.write(str(elementos))
            arquivo.write("\n")
    arquivo.close()

def checarLogin():
    '''Function to check if the login is registered'''
    dic = lerArquivoLogin()
    chaves = dic.keys()
    cpf = input("Usuario(CPF): ")
    senha = input("Senha: ")
    print("<-------------------------------------------->")
    flag = False
    for chave in chaves:
        if(chave == cpf) and (dic[chave][1] == senha):
            flag = True
            return dic[chave]
    if(flag == False):
        
        print("Usuario não cadastrado")
        print("<-------------------------------------------->\n")

#Log Function

def log(cpf, funcao):
    '''Function to generate a list with the navigation history in the program'''
    log = []
    nivel = ""
    if (cpf[0] == "1"):
        nivel = "Recepção"
    if (cpf[0] == "2"):
        nivel = "Médico"
    if (cpf[0] == "3"):
        nivel = "Diretor"
    log.append(datetime())
    log.append(cpf[2])
    log.append(nivel)
    log.append(funcao)
    escreverLog(log)

def escreverLog(lista):
    '''Function to write the navigation history in a csv file'''
    import csv
    arquivo = open("log.csv", "a", newline="")
    writer = csv.writer(arquivo)
    writer.writerow(lista)
    arquivo.close()


 #ALL PROGRAM

#Reception Program
def programaRecepcao():
    '''Function of the complete reception program; Create Registration, Read Registration, Update Registration, Delete Registration, Add patient on the waiting list and Logout.'''
    flag = True
    login = checarLogin()
    if (login != None) and (login[0] == "1"):
        print("Seja Bem Vindo Recepcionista {}".format(login[2]))
        log(login, "Realizou Login")
        while(flag == True):
            resp = int(input("""\n1- Cadastrar
2- Ler Cadastro
3- Atualizar
4- Excluir(Paciente)
5- Consulta
6- Logout
Resposta: """))
            if (resp == 1):    
                criacaoCadastro()
                arquivo = log(login, "Criou Cadastro")
                print(arquivo)
            elif (resp == 2):
                lerCadastro()
                log(login, "Leu Cadastro")
            elif (resp == 3):
                atualizar()
                log(login, "Atualizou Cadastro")
            elif (resp == 4):
                excluirCadastro()
                log(login, "Excluiu Cadastro")
            elif(resp == 5):
                listaEspera()
                log(login, "Adicionou paciente na lista de Espera")
            elif(resp == 6):    
                flag = False
                log(login, "Realizou Logout")

#Doctor Program
def programaMedico():
    '''Function of the complete doctor program; Check how many patients on the waiting list, Perform pending consultations on the waiting list and Logout.'''
    flag = True
    login = checarLogin()
    if (login != None) and (login[0] == "2"):
        log(login, "Realizou Login")
        print("Seja Bem Vindo Medico {}".format(login[2]))
        while(flag == True):
            resp = int(input("""\n1- Lista de Espera
2- Realizar Consulta
3- Logout
Resposta: """))
    
            if(resp == 1):
                quantidadePessoa()
                log(login, "Checou a quantiadade paciente na lista de Espera")
            elif(resp == 2):
                exibirEspera()
                log(login, "Realizou consultas na lista de Espera")
            elif(resp == 3):
                flag = False
                log(login, "Realizou Logout")

#Principal Program
def programaDirecao():
    '''Function of the complete principal program; Check the Hospital's registration total, Check the Hospital's registration keys, Create employee login, Modify employee access level,
Delete employee registration and Logout.'''
    flag = True
    login = checarLogin() 
    if (login != None) and (login[0] == "3"):
        log(login, "Realizou Login")
        print("Seja Bem Vindo Diretor {}\n".format(login[2]))
        while(flag == True):
            resp = int(input("""\n1- Quantidade Cadastros (Pacientes e Funcionarios)
2- Ler Informações(Pacientes e Funcionarios)
3- Criar Cadastro Para Funcionarios
4- Promover Funcionário(Atualizar nível de acesso)
5- Excluir (Funcioanarios)
6- Logout
Resposta: """))
            if(resp == 1):
                totalCadastro()
                log(login, "Checou o total de cadastro do Hospital")
            elif(resp == 2):
                informacaoChaves()
                log(login, "Checou as chaves de cadastro do Hospital")
            elif(resp == 3):
                criarLogin()
                log(login, "Criou Login de acesso")
            elif(resp == 4):
                promover()
                log(login, "Modificou o nível de acesso de um funcionário")
            elif(resp == 5):
                excluirFuncionario()
                log(login, "Excluiu o cadastro de um funcionário")
            elif(resp == 6):
                flag = False
                log(login, "Realizou Logout")

#Program Menu
def menuPrograma():
    '''Full program menu function; Reception, Doctor and Principal'''
    flag = True
    while (flag == True):
        resp = input("""<---------------Seja Bem vindo--------------->
\nDigite seu nivel de acesso\n
1- Recepção
2- Medico
3- Diretor
4- Logout
Resposta: """)
        if(resp == "1"):
            programaRecepcao()
        if(resp == "2"):
            programaMedico()
        if(resp == "3"):
            programaDirecao()
        if(resp == "4"):
            flag = False
menuPrograma()