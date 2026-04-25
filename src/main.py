# Sim, eu sei que poderia utilizar strings que obteria o mesmo resultado, optei por listas por causa de clareza de pensamento! 

import random

letras_minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras_maiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = [',','.','-','=','+','@','#','$','%','*','/','!','?']

senha = ""

while len(senha) < 12:

        item = random.randint(1,4)

        match item:
            case 1: 
                caracter = random.choice(letras_minusculas)
                senha += caracter
            case 2: 
                caracter = random.choice(letras_maiusculas)
                senha += caracter
            case 3: 
                caracter = random.choice(numeros)
                senha += caracter
            case 4: 
                caracter = random.choice(simbolos)
                senha += caracter
    

