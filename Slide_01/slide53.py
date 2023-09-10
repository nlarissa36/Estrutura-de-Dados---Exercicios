#Escreva as funções recursivas listadas a seguir, 
#todas recebem um inteiro e devolvem um inteiro.

# Maior Digito
# retorna o maior dígito do inteiro 


def maiorDigito(n):
    if (n<10):
        return n
    else:
        if n%10 > maiorDigito(n//10):
            return n%10
        else:
            return maiorDigito(n//10)
        
print("O Maior digito é ")     
print(maiorDigito(238)) 



# MenorDigito
# retorna o menor dígito do inteiro

def menorDigito(n):
    if (n<10):
        return n
    else:
        if n%10 < menorDigito(n//10):
            return n%10
        else:
            return menorDigito(n//10)
        
print("O Menor digito é ")     
print(menorDigito(238)) 


# ContaDigito
# retorna a quantidade de dígitos do inteiro

def qtdDigitos(n):
    cont = 1
    if (n<10):
        print("O número tem 1 digito")
    else:
        while(n>10):
            n = n/10
            cont = cont + 1
        print("O número tem %d digitos "%cont)



print(qtdDigitos(9999))


# SomaDigito
# retorna a soma dos dígitos do inteiro

#print("A soma dos números é ") 