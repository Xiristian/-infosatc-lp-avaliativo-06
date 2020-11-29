parametro = input("Digite: ")
separar = []
caracteresValidos = ["{", "}", "[", "]", "(", ")"]
erro = False

def funcao():
    global erro
    
    for i in separarAntes:
        if i in "{":
            try:
                separar.remove("{")
                separar.remove("}")
            except:
                erro = True

        if i in "(":
            try:
                separar.remove("(")
                separar.remove(")")
            except:
                erro = True

        if i in "[":
            try:
                separar.remove("[")
                separar.remove("]")
            except:
                erro = True

    for i in separar:
        if i in caracteresValidos:
            erro = True







for i in parametro:
    separar.append(i)
separarAntes = separar.copy()

for i in separar:
    if i not in caracteresValidos:
        print("Os caracteres não sçao válidos")
    else:
        funcao()

print("O que foi digitado:", parametro)
print("Está errado:", erro)