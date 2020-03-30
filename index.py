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
