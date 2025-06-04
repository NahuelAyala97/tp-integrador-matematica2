import utils

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

#Solicitud al usuario la elección de operación entre conjuntos
mensaje_operacion = f'''Ingrese la operación a realizar con los conjuntos: 
                  1: Unión
                  2: Intersección
                  3: Diferencias
                  4: Diferencia simétrica
                  5: Suma total de los dígitos de los DNI
                  0: Finalizar\n'''

operación = input(f'{mensaje_operacion}')

#Inicio del menú interactivo para realizar las operaciones
while operación != 0:
    if operación == "1":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        
        union = conjuntos_unicos[int(conjunto1)].union(conjuntos_unicos[int(conjunto2)])
        print(f"\nUnión: {union}\n")
    
    elif operación == "2":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        
        interseccion = conjuntos_unicos[int(conjunto1)].intersection(conjuntos_unicos[int(conjunto2)])
        print(f"\nInterseccion: {interseccion}\n")

    elif operación == "3":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        
        diferencia = conjuntos_unicos[int(conjunto1)].difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia: {diferencia}\n")

    elif operación == "4":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        
        diferencia_simetrica = conjuntos_unicos[int(conjunto1)].symmetric_difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia simetrica: {diferencia_simetrica}\n")

    elif operación == "5":
        suma_dnis = utils.suma_digitos(conjuntos_str)
        print(f'Sumatoria de los digitos de los DNI: \n{utils.clave_valor_string(suma_dnis)}')

    elif operación == "0":
        print("\nGracias por usar la calculadora de conjuntos.")
        break
    else:
        print("Ingrese una opción correcta, por favor.")

    operación = input(f'{mensaje_operacion}')