lista = [0,1,2,3,4]
listaAntes = [0,1,2,3,4]
parametro = 1

while parametro != 0:

    parametro = int(input("Digite um número:(0-Sair) "))

    def rotacionaEsquerda():
        for i in listaAntes:
            lista[i-1] = listaAntes[i]

    def rotacionaDireita():
        for i in listaAntes:
            lista[i] = listaAntes[i-1]

    if parametro > 0:
        rotacionaDireita()
    elif parametro < 0:
        rotacionaEsquerda()

    print("Lista antes:       ", listaAntes)
    listaAntes = lista.copy()
    print("Lista rotacionada: ", lista)