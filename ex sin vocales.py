def invertirSinVocales():
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O","U")
    texto = (input("ingrese un texto: "))
    while vocales in texto:
        texto2= texto.replace(vocales,"")
        return texto2

print(invertirSinVocales())
