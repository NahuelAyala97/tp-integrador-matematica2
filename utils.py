#auxiliar para convertir un dic en un strin de clave, valor para imprimir en pantalla
def clave_valor_string(diccionario):
    clave_valor = ""
    for clave, valor in diccionario.items():
        clave_valor += f"{clave}: {valor}\n"

    return clave_valor

def suma_digitos(conjunto):
    print(conjunto)
    sum_dic = {}
    contador = 1
    for n in conjunto:
        
        contador += 1
    return sum_dic