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
    return 1 if n < 10 else 1 + qtdDigitos(n // 10)


print("A quantidade de digitos é: ")
print(qtdDigitos(9999))


# SomaDigito
# retorna a soma dos dígitos do inteiro
def somaDigitos(number):
    return number if number < 10 else number % 10 + somaDigitos(number // 10)

   
print("A soma dos números é ") 
print(somaDigitos(442))


        
    