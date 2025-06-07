# Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas

texto = input("Ingresa una cadena: ")
cadena = texto.replace(" ", "").lower()
palindromo = cadena == cadena[::-1]
print(palindromo)
