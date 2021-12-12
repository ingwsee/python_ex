
'''Validar email
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no,
 valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
'''

# busca en cada caracter del email @
def validar (email):
    caracterrequerido="@"
    
    for c in email:
        if c == caracterrequerido:
            return True
        return False

direccion=input("Por favor ingrese email:")
if validar(direccion):
    print("Dirección Valida")
else:
    print("Dirección Invalida") 