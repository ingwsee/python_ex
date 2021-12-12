# Indicar al usuario que ingrese una palabra y asignarlo a la variable userWord.

userWord = str (input ("Ingrese una palabra: ")).upper()
vocales = ("A","E","I","O","U")
texto = ''
for letra in userWord:
    if letra in vocales:
         texto = userWord.replace(letra,"")
         continue
    print(texto) 
else:
     print ()
     
    # Completa el cuerpo del ciclo for.
#texto = (input("ingrese un texto: "))
 #   while vocales in texto:
#        userWord = userWord.replace(vocales,"")
        #return userWord
#        print (userWord)
"""
userWord = str (input ("Ingrese una palabra: "))
userWord.upper()
vocales = ['A','E','I','O','U']
res = ''
for vocales in userWord:
    continue
    if userWord not in vocales:
        res += userWord
return res
print (userWord)


word = input('Input your word: ').upper()

new_word = ''
for char in word:
    if char in 'AEIOU':
        continue
    new_word += char

print(new_word)
"""
