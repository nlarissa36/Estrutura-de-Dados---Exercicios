#Escreva as funções recursivas listadas a seguir, 
#todas recebem um inteiro e devolvem um inteiro.


#zeraPares
#retorna um inteiro com os dígitos pares em zero
def zeraPares(n):
    if n < 10:
        return n if n % 2 else 0
    elif n % 2:
        return zeraPares(n // 10) * 10 + n % 10
    return zeraPares(n // 10) * 10

print(zeraPares(123456789))


#zeraImpares
#retorna um inteiro com os dígitos ímpares em zero


#removePares
#remove os dígitos pares do inteiro


#removeImpares
#remove os dígitos ímpares do inteiro
