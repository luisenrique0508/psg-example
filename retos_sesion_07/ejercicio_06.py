# removeprefix y removesuffix (Python 3.9+)
texto = "Pythonista"
print(texto.removeprefix("Py"))  # 'thonista'
print(texto.removesuffix("ista"))  # 'Python'
# isascii (Python 3.7+)
cadena = "abc123"
print(cadena.isascii())  # True

# zfill (rellena con ceros a la izquierda)
numero = "42"
print(numero.zfill(5))  # '00042'

# partition (divide en 3 partes usando un separador)
frase = "user:password"
print(frase.partition(":"))  # ('user', ':', 'password')

# rjust (alinear a la derecha rellenando con un carácter)
texto = "42"
print(texto.rjust(6, "*"))  # '****42'

# expandtabs (convierte tabulaciones en espacios)
linea = "a\tb\tc"
print(linea.expandtabs(4))  # 'a   b   c'