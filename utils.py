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

#####
#funciones auxiliares para calculos de fechas(Facundo)

def es_bisiesto(ano):
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si:
    - Es divisible por 4 Y no por 100, O
    - Es divisible por 400
    """
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def contar_pares_impares(anos):
    """
    Cuenta cuántos años son pares e impares.
    Retorna dos listas: [años_pares], [años_impares]
    """
    anos_pares = []
    anos_impares = []
    
    for ano in anos:
        if ano % 2 == 0:
            anos_pares.append(ano)
        else:
            anos_impares.append(ano)
    
    return anos_pares, anos_impares

def calcular_edades(anos_nacimiento, ano_actual=2025):
    """
    Calcula las edades actuales basándose en los años de nacimiento.
    """
    edades = []
    for ano in anos_nacimiento:
        edad = ano_actual - ano
        edades.append(edad)
    return edades

def evaluar_grupo_z(anos_nacimiento):
    """
    Evalúa si todos los integrantes nacieron después del 2000 (Grupo Z).
    """
    return all(ano > 2000 for ano in anos_nacimiento)

def encontrar_anos_bisiestos(anos_nacimiento):
    """
    Encuentra qué años de nacimiento son bisiestos.
    """
    anos_bisiestos = []
    for ano in anos_nacimiento:
        if es_bisiesto(ano):
            anos_bisiestos.append(ano)
    return anos_bisiestos

def producto_cartesiano(conjunto1, conjunto2):
    """
    Calcula el producto cartesiano entre dos conjuntos.
    Retorna una lista de tuplas (elemento1, elemento2).
    """
    producto = []
    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            producto.append((elemento1, elemento2))
    return producto

def mostrar_condiciones_logicas_anos(anos_nacimiento):
    """
    Evalúa y muestra todas las condiciones lógicas relacionadas con años.
    """
    print("=== EVALUACIÓN DE CONDICIONES LÓGICAS - AÑOS ===")
    
    # Condición 1: Grupo Z
    if evaluar_grupo_z(anos_nacimiento):
        print("✓ Grupo Z - Todos nacieron después del 2000")
    else:
        print("✗ No es Grupo Z - Algunos nacieron en 2000 o antes")
    
    # Condición 2: Años bisiestos
    anos_bisiestos = encontrar_anos_bisiestos(anos_nacimiento)
    if anos_bisiestos:
        print(f"✓ Tenemos un año especial - Años bisiestos: {anos_bisiestos}")
    else:
        print("✗ No hay años bisiestos en el grupo")
    
    # Condición 3: Mayoría pares vs impares
    anos_pares, anos_impares = contar_pares_impares(anos_nacimiento)
    if len(anos_pares) > len(anos_impares):
        print("✓ Mayoría de años pares en el grupo")
    elif len(anos_impares) > len(anos_pares):
        print("✓ Mayoría de años impares en el grupo")
    else:
        print("✓ Cantidad igual de años pares e impares")

def mostrar_resumen_anos(anos_nacimiento):
    """
    Muestra un resumen completo de la información de años de nacimiento.
    """
    print(f"\n=== RESUMEN AÑOS DE NACIMIENTO ===")
    print(f"Años ingresados: {anos_nacimiento}")
    
    # Calcular edades
    edades = calcular_edades(anos_nacimiento)
    print(f"Edades actuales: {edades}")
    
    # Contar pares e impares
    anos_pares, anos_impares = contar_pares_impares(anos_nacimiento)
    print(f"Años pares: {anos_pares} (Total: {len(anos_pares)})")
    print(f"Años impares: {anos_impares} (Total: {len(anos_impares)})")
    
    # Años bisiestos
    anos_bisiestos = encontrar_anos_bisiestos(anos_nacimiento)
    if anos_bisiestos:
        print(f"Años bisiestos: {anos_bisiestos}")
    else:
        print("No hay años bisiestos")
    
    # Producto cartesiano
    producto = producto_cartesiano(anos_nacimiento, edades)
    print(f"Producto cartesiano (Años × Edades): {len(producto)} pares")
    
    # Mostrar algunos ejemplos del producto cartesiano
    print("Primeros 5 pares del producto cartesiano:")
    for i, par in enumerate(producto[:5]):
        print(f"  {i+1}. {par}")
    
    if len(producto) > 5:
        print(f" ... y {len(producto) - 5}")