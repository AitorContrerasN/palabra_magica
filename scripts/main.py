def cargar_diccionario(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        palabras = [linea.strip() for linea in archivo if len(linea.strip()) == 5]
    return palabras

def filtrar_palabras(palabras, intento, resultados):
    palabras_filtradas = palabras
    for i, (letra, resultado) in enumerate(zip(intento, resultados)):
        if resultado == '2':
            # Verifica que todas las palabras tengan la letra en la posición correcta
            palabras_filtradas = [palabra for palabra in palabras_filtradas if len(palabra) > i and palabra[i] == letra]
        elif resultado == '1':
            # Verifica que la letra esté en la palabra, pero no en la posición i
            palabras_filtradas = [palabra for palabra in palabras_filtradas if len(palabra) > i and letra in palabra and palabra[i] != letra]
        elif resultado == '0':
            # Verifica que la letra no esté en ninguna posición de la palabra
            palabras_filtradas = [palabra for palabra in palabras_filtradas if letra not in palabra]
    return palabras_filtradas


def main():
    ruta_diccionario = 'palabra_secreta/recursos/diccionario.txt'
    palabras = cargar_diccionario(ruta_diccionario)
    for _ in range(6):  # Máximo de intentos
        while True:
            intento = input("Introduce la palabra utilizada: ").lower()
            if len(intento) == 5 and all(char.isalpha() for char in intento):  # Verifica que la palabra tenga 5 letras y solo contenga letras
                break
            else:
                print("Por favor, introduce una palabra de exactamente 5 letras.")
        resultados = []
        for i, letra in enumerate(intento):
            while True:
                resultado = input(f"Resultado para {letra} (2: correcto y posición, 1: correcto pero posición errónea, 0: incorrecto): ")
                if resultado in ['0', '1', '2']:
                    resultados.append(resultado)
                    break
                else:
                    print("Por favor, introduce un valor válido (0, 1, 2).")
        
        palabras = filtrar_palabras(palabras, intento, resultados)
        
        print(f"{len(palabras)} palabras posibles.")
        for palabra in palabras:
            print(palabra)
        print()



if __name__ == "__main__":
    main()
