n=5
#execute n times
for i in range(0,n):
    print("Hello %d"%i)

#laço externo executa n vezes
for i in range(0,n):
    for j in range(0,n):
        print("Valor de i:%d, valor de j: %d"%(i,j))
