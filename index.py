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
                  5: Frecuencia de dígitos en los DNI
                  6: Suma total de los dígitos de los DNI
                  7: Evaluación de condiciones lógicas
                  0: Finalizar\n'''

operación = input(f'{mensaje_operacion}')

#Inicio del menú interactivo para realizar las operaciones
while operación != 0:
    if operación == "1":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #al operar con conjuntos es posible utilizar el metodo "union" de set para calcular o el operador + 
        union = conjuntos_unicos[int(conjunto1)].union(conjuntos_unicos[int(conjunto2)])
        print(f"\nUnión: {union}\n")
    
    elif operación == "2":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #set tiene el metodo intersección para operar entre conjuntos o con el operador &
        interseccion = conjuntos_unicos[int(conjunto1)].intersection(conjuntos_unicos[int(conjunto2)])
        print(f"\nInterseccion: {interseccion}\n")

    elif operación == "3":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #se utiliza el motodo de set difference para obtener la diferencia entre conjuntos, o usando el operador -
        diferencia = conjuntos_unicos[int(conjunto1)].difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia: {diferencia}\n")

    elif operación == "4":
        conjunto1 = input((f'\nIngrese el primer conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        conjunto2 = input((f'\nIngrese el segundo conjunto:\n{utils.clave_valor_string(conjuntos_unicos)}\b'))
        #set tambien cuenta con el metodo symmetric_difference tambien posible con el operador ^
        diferencia_simetrica = conjuntos_unicos[int(conjunto1)].symmetric_difference(conjuntos_unicos[int(conjunto2)])
        print(f"\nDiferencia simetrica: {diferencia_simetrica}\n")

    elif operación == "5":
        #se recorre los dnis ingresados para crear un string con todos los digitos
        digitos = ""
        for dni in conjuntos_str:
            digitos += dni
        #al string con los digitos se pasa como argumento a la funcion auxiliar para que entre la frecuencia
        print(f'La frecuencia de digitos en los DNI son:\n{utils.frecuencia_digitos(digitos)}')
    
    elif operación == "6":
        #se pasa como argumento los dnis ingresados a la funcion auxiliar para luego imprimir
        #cada dni con su suma de digitos correspondiente.
        suma_dnis = utils.suma_digitos(conjuntos_str)
        print(f'Sumatoria de los digitos de los DNI: \n{utils.clave_valor_string(suma_dnis)}')
    
    elif operación == "7":
        #se utilizan dos funciones auxiliares para determinar el digito compartido entre los conjuntos creados
        # y la diversidad numerica de cada uno. 
        digito_compartido = utils.digito_compartido(conjuntos_unicos)
        diversidad = utils.diversidad_numerica(conjuntos_unicos)
    #Si el usuario ingresa la opción 0 el programa finaliza.
    elif operación == "0":
        print("\nGracias por usar la calculadora de conjuntos.")
        break
    else:
    #si el usuario no ingresa una opcion correcta, da aviso y vuelve a preguntar
        print("Ingrese una opción correcta, por favor.")
    #se pregunta nuevamente al usuario una opción para que vuelva a correr el bucle
    operación = input(f'{mensaje_operacion}')