def cifrado_cesar(texto, desplazamiento, modo):
    """
    Aplica el cifrado César a un texto.

    Args:
        texto (str): El texto a encriptar o desencriptar.
        desplazamiento (int): La cantidad de posiciones a desplazar las letras.
        modo (str): 'encriptar' para encriptar, 'desencriptar' para desencriptar.

    Returns:
        str: El texto procesado (encriptado o desencriptado).
    """
    resultado = ""
    # Aseguramos que el desplazamiento esté en el rango 0-25 para letras del alfabeto
    desplazamiento = desplazamiento % 26

    if modo == 'desencriptar':
        desplazamiento = -desplazamiento # Para desencriptar, movemos en la dirección opuesta

    for caracter in texto:
        if 'a' <= caracter <= 'z':
            # Procesa letras minúsculas
            inicio_alfabeto = ord('a')
            posicion_original = ord(caracter) - inicio_alfabeto
            nueva_posicion = (posicion_original + desplazamiento) % 26
            nuevo_caracter = chr(inicio_alfabeto + nueva_posicion)
            resultado += nuevo_caracter
        elif 'A' <= caracter <= 'Z':
            # Procesa letras mayúsculas
            inicio_alfabeto = ord('A')
            posicion_original = ord(caracter) - inicio_alfabeto
            nueva_posicion = (posicion_original + desplazamiento) % 26
            nuevo_caracter = chr(inicio_alfabeto + nueva_posicion)
            resultado += nuevo_caracter
        else:
            # Deja los caracteres que no son letras sin cambios (números, espacios, símbolos)
            resultado += caracter

    return resultado

# --- Ejemplo de Uso ---

# Solicitar entrada al usuario
mensaje = input("Introduce el mensaje: ")
try:
    clave = int(input("Introduce la clave de desplazamiento (un número entero): "))
except ValueError:
    print("Entrada inválida para la clave. Usando clave 0.")
    clave = 0

opcion = input("¿Quieres (e)ncriptar o (d)esencriptar? ").lower()

if opcion == 'e':
    texto_procesado = cifrado_cesar(mensaje, clave, 'encriptar')
    print(f"Mensaje encriptado: {texto_procesado}")
elif opcion == 'd':
     # Al desencriptar, usamos la misma clave positiva, la función maneja el negativo
    texto_procesado = cifrado_cesar(mensaje, clave, 'desencriptar')
    print(f"Mensaje desencriptado: {texto_procesado}")
else:
    print("Opción no válida. Por favor, elige 'e' o 'd'.")