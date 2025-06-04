#auxiliar para convertir un dic en un strin de clave, valor para imprimir en pantalla
def clave_valor_string(diccionario):
    clave_valor = ""
    #se recorre el diccionario tomando todos los items para obtener cada key, value
    #para poder imprimirlo
    for clave, valor in diccionario.items():
        clave_valor += f"{clave}: {valor}\n"

    return clave_valor

#funcion auxiliar para encontrar la frecuencia de digitos 
def frecuencia_digitos(digitos): 
    frecuencia_dic = {}
    #recorre los digitos del argumento, se utiliza el metodo get() de diccionarios
    # y se pasa como argumento un value por defecto para que no de error si no esta el indice buscado
    #si lo encuentra le suma uno al valor del indice
    for d in digitos:
        frecuencia_dic[d] = frecuencia_dic.get(d, 0) + 1
    
    return frecuencia_dic

#funcion auxiliar para sumar los digitos de una lista 
def suma_digitos(list_dni):
    sum_dic = {}
    #contador para usarlo como indice del diccionario
    contador = 1
    #recorre la lista
    for dni in list_dni:
        suma = 0
        #recorre cada digito para luego sumarlo en la variable suma
        for n in dni:
            suma += int(n)
        #se utilizar el indice del contador para agregar al diccionario la suma de los digitos
        sum_dic[contador] = suma
        contador += 1
    #retorna un diccionario con indice y suma de cada dni en la lista
    return sum_dic

#auxiliar para encontrar los digitos compartidos en el diccionario de conjuntos
def digito_compartido(conjuntos): 
    #se utiliar el metodo intersection de set para encontrar los digitos compartidos
    #se pasa como argumento todos los valores dentro del diccionario conjuntos con el operador * 
    interseccion = set.intersection(*conjuntos.values())
    
    if interseccion:
        print(f"Digitos compartidos: {interseccion}")
    else:
        print("No comparten ningun digito.")       

#funcion auxiliar para determinar si el conjunto es de divesidad numerica alta o baja
def diversidad_numerica(conjuntos):
    #se recorrer todos los valores del dictionario pasado como argumento
    for c in conjuntos.values():
        #se determina la diversidad numerica dependiendo de la longitud del elementos del conjunto
        if len(c) > 6:
            print(f"El conjunto {c} tiene diversidad númerica alta.")
        else: 
            print(f"El conjunto {c} tiene una diversidad númerica baja.")