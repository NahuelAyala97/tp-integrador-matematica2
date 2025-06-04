#auxiliar para convertir un dic en un strin de clave, valor para imprimir en pantalla
def clave_valor_string(diccionario):
    clave_valor = ""
    for clave, valor in diccionario.items():
        clave_valor += f"{clave}: {valor}\n"

    return clave_valor

def suma_digitos(list_dni):
    sum_dic = {}
    contador = 1
    for dni in list_dni:
        suma = 0
        for n in dni:
            suma += int(n)
        sum_dic[contador] = suma
        contador += 1
    return sum_dic