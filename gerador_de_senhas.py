import random


min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sysbs = '[]{}()!@¢&*#:?°º§¬¢£|\;/:;-_%'

#introdução
print ('Olá Seja muito bem vindo, estamos felizes em ter optado por escolher.' )
print ('O nosso modo de selecionar a sua senha, recomendamos que sua senha tenha pelo menos 8 caracters 😁.')
print ('---------------------------------------------------------------------')

#Recebendo dados
nome = input ('Qual seu nome? ༼ つ ◕_◕ ༽つ:  ')
print ("Hello There!"+ nome +"não se esqueça dessa tabela quando for colocar o tamanho da senha ok?")
print ('---------------------------------------------------------------------')
print ('''          Tamanho da senha  | Tempo para quebrar    |
            4 Digitos       |   0,45 s              |
            5 Digitos       |   15 s                |
            6 Digitos       |   4 min               |
            7 Digitos       |   6 Horas             |
            8 Digitos       |   24 Dias             |
            9 Digitos       |   6 Anos              |
            10 Digitos      |   600 Anos            |''')
print ('---------------------------------------------------------------------')
qnt = input ('Olá '+ nome + ' digite qual tamanho da senha:  ')
qntInt = int(qnt)
length = qntInt

#fazendo senha com todos
all = min + max + num + sysbs
passwordALL = "" .join(random.sample(all,length))

#só maiúsculas e números
MAXnum = max + num
passwordMAXnum = "" .join(random.sample(MAXnum,length))

#só minusculas e maiúsculas
MAXmin = max + min
passwordMAXmin = "" .join(random.sample(MAXmin,length))

#só números
Num = num
passwordNum = "" .join(random.sample(Num,length))

#só caracter
Sys = sysbs
passwordSys = "".join(random.sample(Sys,length))

#imprimir as senhas
print ('---------------------------------------------------------------------')
print ('------------------------AQUI ESTÁ SUA SENHA--------------------------')
print ('Senha com todos = ' + passwordALL)
print ('Senha com números e letras maiúsculas = ' + passwordMAXnum)
print ('Senha com números e letras maiúscuas e minusculas = ' + passwordMAXmin)
print ('Senha com números = ' + passwordNum)
print ('Senha com caracters = ' + passwordSys)
print ('---------------------------------------------------------------------')
print ('---------------------------------------------------------------------')