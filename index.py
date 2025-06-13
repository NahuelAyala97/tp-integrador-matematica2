import utils
from datetime import datetime

#Solicita al usuario dni
conjuntos_str = input("Ingrese los dni separados por una coma: ").split(',')

conjuntos_unicos = {}

#contador para usar como key en el dictionario conjuntos_unicos
contador = 1
#recorre los dni dados por el usuario
for c in conjuntos_str:
    #adiciona cada conjunto convirtiendolo en un set de enteros
    #los set por definición solo permite digitos únicos, por lo que se realiza el filtro automáticamente.
    conjuntos_unicos[contador] = {int(n) for n in str(c)}
    contador += 1

print(conjuntos_unicos)

# --- PARTE 2 (Facundo): OPERACIONES CON AÑOS DE NACIMIENTO ---
print("\n=== OPERACIONES CON AÑOS DE NACIMIENTO ===")

# Solicitar años de nacimiento
num_integrantes = len(conjuntos_str)
anos_nacimiento = []

print(f"Ingrese los años de nacimiento de los {num_integrantes} integrantes:")
for i in range(num_integrantes):
    while True:
        try:
            ano = int(input(f"Año de nacimiento del integrante {i+1}: "))
            if ano < 1900 or ano > datetime.now().year:
                print("Por favor ingrese un año válido (entre 1900 y el año actual)")
                continue
            if ano in anos_nacimiento:
                print("Este año ya fue ingresado. Ingrese un año diferente o ficticio.")
                continue
            anos_nacimiento.append(ano)
            break
        except ValueError:
            print("Por favor ingrese un número válido")

print(f"\nAños de nacimiento ingresados: {anos_nacimiento}")

# Función para determinar si un año es bisiesto
def es_bisiesto(ano):
    """
    Determina si un año es bisiesto.
    Un año es bisiesto si:
    - Es divisible por 4 Y
    - Si es divisible por 100, también debe ser divisible por 400
    """
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Contar años pares e impares
anos_pares = []
anos_impares = []

for ano in anos_nacimiento:
    if ano % 2 == 0:
        anos_pares.append(ano)
    else:
        anos_impares.append(ano)

print(f"\nAños pares: {anos_pares} (Total: {len(anos_pares)})")
print(f"Años impares: {anos_impares} (Total: {len(anos_impares)})")

# Calcular edades actuales
ano_actual = datetime.now().year
edades_actuales = []
for ano in anos_nacimiento:
    edad = ano_actual - ano
    edades_actuales.append(edad)

print(f"\nEdades actuales: {edades_actuales}")

# Evaluación de condiciones lógicas

# Condición 1: Si todos nacieron después del 2000, mostrar "Grupo Z"
if all(ano > 2000 for ano in anos_nacimiento):
    print("\n✓ Grupo Z - Todos nacieron después del 2000")
else:
    print(f"\n✗ No es Grupo Z - Algunos nacieron en 2000 o antes")

# Condición 2: Si alguno nació en año bisiesto, mostrar "Tenemos un año especial"
anos_bisiestos = []
for ano in anos_nacimiento:
    if es_bisiesto(ano):
        anos_bisiestos.append(ano)

if anos_bisiestos:
    print(f"✓ Tenemos un año especial - Años bisiestos: {anos_bisiestos}")
else:
    print("✗ No hay años bisiestos en el grupo")

# Condición 3: Si hay más años pares que impares
if len(anos_pares) > len(anos_impares):
    print("✓ Mayoría de años pares en el grupo")
elif len(anos_impares) > len(anos_pares):
    print("✓ Mayoría de años impares en el grupo")
else:
    print("✓ Cantidad igual de años pares e impares")

# Producto cartesiano entre conjunto de años y conjunto de edades
print(f"\n=== PRODUCTO CARTESIANO ===")
print("Años de nacimiento × Edades actuales:")
producto_cartesiano = []
for ano in anos_nacimiento:
    for edad in edades_actuales:
        producto_cartesiano.append((ano, edad))

# Mostrar producto cartesiano de forma organizada
print("Pares (Año, Edad):")
for i, par in enumerate(producto_cartesiano):
    print(f"{i+1:2d}. {par}")

print(f"\nTotal de pares en el producto cartesiano: {len(producto_cartesiano)}")

#Solicitud al usuario la elección de operación entre conjuntos
mensaje_operacion = f'''Ingrese la operación a realizar con los conjuntos: 
                  1: Unión
                  2: Intersección
                  3: Diferencias
                  4: Diferencia simétrica
                  5: Frecuencia de dígitos en los DNI
                  6: Suma total de los dígitos de los DNI
                  7: Evaluación de condiciones lógicas
                  8: Mostrar resumen de años de nacimiento
                  0: Finalizar\n'''

operacion = input(f'{mensaje_operacion}')

#Inicio del menú interactivo para realizar las operaciones
while operacion != 0:
    if operacion == "1":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #al operar con conjuntos es posible utilizar el metodo "union" de set para calcular o el operador + 
        union = conjuntos_unicos[int(conjunto1)].union(conjuntos_unicos[int(conjunto2)])
        print(f"\nUnión: {union}\n")
    
    elif operacion == "2":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #set tiene el metodo intersección para operar entre conjuntos o con el operador &
        interseccion = conjuntos_unicos[int(conjunto1)].intersection(conjuntos_unicos[int(conjunto2)])
        print(f"\nInterseccion: {interseccion}\n")

    elif operacion == "3":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #se utiliza el motodo de set difference para obtener la diferencia entre conjuntos, o usando el operador -
        diferencia = conjuntos_unicos[int(conjunto1)].difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia: {diferencia}\n")

    elif operacion == "4":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #set tambien cuenta con el metodo symmetric_difference tambien posible con el operador ^
        diferencia_simetrica = conjuntos_unicos[int(conjunto1)].symmetric_difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia simetrica: {diferencia_simetrica}\n")

    elif operacion == "5":
        #se recorre los dnis ingresados para crear un string con todos los digitos
        digitos = ""
        for dni in conjuntos_str:
            digitos += dni
        #al string con los digitos se pasa como argumento a la funcion auxiliar para que entre la frecuencia
        print(f'La frecuencia de digitos en los DNI son:\n{utils.frecuencia_digitos(digitos)}')
    
    elif operacion == "6":
        #se pasa como argumento los dnis ingresados a la funcion auxiliar para luego imprimir
        #cada dni con su suma de digitos correspondiente.
        suma_dnis = utils.suma_digitos(conjuntos_str)
        print(f'Sumatoria de los digitos de los DNI: \n{utils.clave_valor_string(suma_dnis)}')
    
    elif operacion == "7":
        #se utilizan dos funciones auxiliares para determinar el digito compartido entre los conjuntos creados
        # y la diversidad numerica de cada uno. 
        digito_compartido = utils.digito_compartido(conjuntos_unicos)
        diversidad = utils.diversidad_numerica(conjuntos_unicos)
    
    elif operacion == "8":
        # Nueva opción para mostrar el resumen de años de nacimiento
        print(f"\n=== RESUMEN AÑOS DE NACIMIENTO ===")
        print(f"Años ingresados: {anos_nacimiento}")
        print(f"Edades actuales: {edades_actuales}")
        print(f"Años pares: {anos_pares} ({len(anos_pares)} años)")
        print(f"Años impares: {anos_impares} ({len(anos_impares)} años)")
        if anos_bisiestos:
            print(f"Años bisiestos: {anos_bisiestos}")
        else:
            print("No hay años bisiestos")
    #Si el usuario ingresa la opción 0 el programa finalizar.
    elif operacion == "0":
        print("\nGracias por usar la calculadora de conjuntos.")
        break
    else:
    #si el usuario no ingresa una opcion correcta, da aviso y vuelve a preguntar
        print("Ingrese una opción correcta, por favor.")
    #se pregunta nuevamente al usuario una opción para que vuelva a correr el bucle
    operacion = input(f'{mensaje_operacion}')