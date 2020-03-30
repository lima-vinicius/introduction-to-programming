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

