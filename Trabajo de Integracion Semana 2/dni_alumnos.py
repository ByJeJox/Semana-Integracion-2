# A. Operaciones con DNIs
print("-----A. Operaciones con DNIs-----")
# DNI alumnos
# Ingreso de los DNIs (reales o ficticios).
dni_molina = "31476619"
dni_mele = "36552513"
dni_martinez = "39964587"
dni_meshler = "34433376"
dni_masseroni = "39600348"
dni_martilotta = "42095856"

print("Generación automática de los conjuntos de dígitos únicos")
# Conjuntos de dígitos únicos de los DNIs generados automaticamente
conjunto_unico_molina = set(dni_molina)
conjunto_unico_mele = set(dni_mele)
conjunto_unico_martinez = set(dni_martinez)
conjunto_unico_meshler = set(dni_meshler)
conjunto_unico_masseroni = set(dni_masseroni)
conjunto_unico_martilotta = set(dni_martilotta)

print("Conjunto único de Molina:", conjunto_unico_molina)
print("Conjunto único de Mele:", conjunto_unico_mele)
print("Conjunto único de Martinez:", conjunto_unico_martinez)
print("Conjunto único de Meshler:", conjunto_unico_meshler)
print("Conjunto único de Masseroni:", conjunto_unico_masseroni)

# Funcion para unir dos conjuntos
def union_conjuntos(conjunto1, conjunto2):
    conjunto_union = []
    for i in conjunto1:
        if i not in conjunto_union:
            conjunto_union.append(i)

    for i in conjunto2:
        if i not in conjunto_union:
            conjunto_union.append(i)
    return conjunto_union

print("\n-----Uniones de Molina con los demás conjuntos-----")
# Vista de las uniones de los conjuntos de molina con los demás
print("Unión de Molina y Mele: ", union_conjuntos(conjunto_unico_molina, conjunto_unico_mele))
print("Unión de Molina y Martinez: ", union_conjuntos(conjunto_unico_molina, conjunto_unico_martinez))
print("Unión de Molina y Meshler: ", union_conjuntos(conjunto_unico_molina, conjunto_unico_meshler))
print("Unión de Molina y Masseroni: ", union_conjuntos(conjunto_unico_molina, conjunto_unico_masseroni))
print("Unión de Molina y Martilotta: ", union_conjuntos(conjunto_unico_molina, conjunto_unico_martilotta))


# Función para encontrar la intersección de dos conjuntos
def interseccion_conjuntos(conjunto1, conjunto2):
    conjunto_interseccion = []
    for i in conjunto1:
        if i in conjunto2 and i not in conjunto_interseccion:
            conjunto_interseccion.append(i)
    return conjunto_interseccion

print("\n-----Intersecciones de Molina con los demás conjuntos-----")
print("Intersección de Molina y Mele: ", interseccion_conjuntos(conjunto_unico_molina, conjunto_unico_mele))
print("Intersección de Molina y Martinez: ", interseccion_conjuntos(conjunto_unico_molina, conjunto_unico_martinez))
print("Intersección de Molina y Meshler: ", interseccion_conjuntos(conjunto_unico_molina, conjunto_unico_meshler))
print("Intersección de Molina y Masseroni: ", interseccion_conjuntos(conjunto_unico_molina, conjunto_unico_masseroni))
print("Intersección de Molina y Martilotta: ", interseccion_conjuntos(conjunto_unico_molina, conjunto_unico_martilotta))


# Función para encontrar la diferencia entre dos conjuntos
def diferencia_entre_pares(conjunto1, conjunto2):
    conjunto_diferencia = []
    for i in conjunto1:
        if i not in conjunto2 and i not in conjunto_diferencia:
            conjunto_diferencia.append(i)
    return conjunto_diferencia
 
print("\n-----Diferencias de Molina con los demás conjuntos-----")
# Vista de las diferencias entre los conjuntos de molina con los demás
print("Diferencia entre Molina y Mele: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_mele))
print("Diferencia entre Molina y Martinez: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_martinez))
print("Diferencia entre Molina y Meshler: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_meshler))
print("Diferencia entre Molina y Masseroni: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_masseroni))
print("Diferencia entre Molina y Martilotta: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_martilotta))


# Función para encontrar la diferencia simétrica entre dos conjuntos
def diferencia_simetrica(conjunto1, conjunto2):
    conjunto_diferencia_simetrica = []
    for i in conjunto1:
        if i not in conjunto2 and i not in conjunto_diferencia_simetrica:
            conjunto_diferencia_simetrica.append(i)
    
    for i in conjunto2:
        if i not in conjunto1 and i not in conjunto_diferencia_simetrica:
            conjunto_diferencia_simetrica.append(i)
    
    return conjunto_diferencia_simetrica

print("\n-----Diferencias simétricas de Molina con los demás conjuntos-----")
# Vista de las diferencias simétricas entre los conjuntos de molina con los demás
print("Diferencia simétrica entre Molina y Mele: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_mele))
print("Diferencia simétrica entre Molina y Martinez: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_martinez))
print("Diferencia simétrica entre Molina y Meshler: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_meshler))
print("Diferencia simétrica entre Molina y Masseroni: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_masseroni))
print("Diferencia simétrica entre Molina y Martilotta: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_martilotta))

# Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas
def contar_frecuencia_dni(dni):
    frecuencia = {}  # Diccionario aux para almacenar la frecuencia de cada dígito
    for digito in dni:  # Recorremos cada carácter del DNI
        if digito in frecuencia: # Si el dígito ya está en el diccionario
            frecuencia[digito] += 1  # Incrementamos la cuenta si ya existe
        else:
            frecuencia[digito] = 1  # Si no existe, lo inicializamos en 1
    return frecuencia

print("\n-----Frecuencia de dígitos en los DNIs-----")
# Imprimimos la frecuencia de cada dígito en los DNIs
print("Frecuencia de Molina:", contar_frecuencia_dni(dni_molina))
print("Frecuencia de Mele:", contar_frecuencia_dni(dni_mele))
print("Frecuencia de Martinez:", contar_frecuencia_dni(dni_martinez))
print("Frecuencia de Meshler:", contar_frecuencia_dni(dni_meshler))
print("Frecuencia de Masseroni:", contar_frecuencia_dni(dni_masseroni))
print("Frecuencia de Martilotta:", contar_frecuencia_dni(dni_martilotta))

# Función para sumar los dígitos de un DNI
def suma_digitos_dni(dni):
    suma = 0  # Inicializamos la suma en 0
    for digito in dni:  # Recorremos cada carácter del DNI
        suma += int(digito)  # Convertimos el carácter en número y lo sumamos
    return suma

print("\n-----Suma de los dígitos de los DNIs-----")
# Imprimimos la suma de los dígitos de cada DNI
print("Suma de los dígitos del DNI de Molina: ", suma_digitos_dni(dni_molina))
print("Suma de los dígitos del DNI de Mele: ", suma_digitos_dni(dni_mele))
print("Suma de los dígitos del DNI de Martinez: ", suma_digitos_dni(dni_martinez))
print("Suma de los dígitos del DNI de Meshler: ", suma_digitos_dni(dni_meshler))
print("Suma de los dígitos del DNI de Masseroni: ", suma_digitos_dni(dni_masseroni))
print("Suma de los dígitos del DNI de Martilotta: ", suma_digitos_dni(dni_martilotta))


# Dígito compartido entre todos los conjuntos
def digitos_compartidos(conjunto1, conjunto2, conjunto3, conjunto4, conjunto5, conjunto6):
    conjunto_digitos_compartidos = []  # Usamos un conjunto para almacenar los dígitos compartidos

    for digito in "0123456789":  # Recorremos los dígitos del 0 al 9
        if digito in conjunto1 and digito in conjunto2 and digito in conjunto3 and digito in conjunto4 and digito in conjunto5 and digito in conjunto6:
            conjunto_digitos_compartidos.append(digito)  # Si el dígito está en todos los conjuntos, lo añadimos
    return conjunto_digitos_compartidos  # Devolvemos el conjunto de dígitos compartidos

print("\n-----Dígito compartido entre todos los conjunto-----")
print("Dígito compartido entre todos los conjuntos:",digitos_compartidos(conjunto_unico_molina, conjunto_unico_mele, conjunto_unico_martinez, conjunto_unico_meshler, conjunto_unico_masseroni, conjunto_unico_martilotta))

# Diversidad numérica alta si tiene mas de 6 digitos únicos
def diversidad_numerica_alta(conjunto):
    if len(conjunto) > 6:  # Si el conjunto tiene más de 6 dígitos únicos
        return "Diversidad Numerica Alta"
    else:
        return "Diversidad Numerica Baja"

print("\n-----Diversidad numérica de los DNIs-----")
# Imprimimos la diversidad numérica de cada conjunto único  
print("Diversidad numérica del DNI de Molina:", diversidad_numerica_alta(conjunto_unico_molina))
print("Diversidad numérica del DNI de Mele:", diversidad_numerica_alta(conjunto_unico_mele))
print("Diversidad numérica del DNI de Martinez:", diversidad_numerica_alta(conjunto_unico_martinez))
print("Diversidad numérica del DNI de Meshler:", diversidad_numerica_alta(conjunto_unico_meshler))
print("Diversidad numérica del DNI de Masseroni:", diversidad_numerica_alta(conjunto_unico_masseroni))
print("Diversidad numérica del DNI de Martilotta:", diversidad_numerica_alta(conjunto_unico_martilotta))


# Existe al menos un par de DNIs cuyo total de la suma de los dígitos es igual.
def buscar_pares_dni(dnis):  # Definimos una función que recibe una lista de DNIs
    suma_dict = {}  # Creamos un diccionario vacío para almacenar las sumas de los dígitos

    for dni in dnis:  # Recorremos cada DNI en la lista
        total = suma_digitos_dni(dni)  # Calculamos la suma de los dígitos del DNI actual con la función suma_digitos_dni
        if total in suma_dict:  # Si ya existe una suma igual en el diccionario...
            suma_dict[total].append(dni)  # Agregamos el DNI a la lista de DNIs con la misma suma
        else:  # Si es la primera vez que encontramos esta suma...
            suma_dict[total] = [dni]  # Creamos una nueva entrada en el diccionario con la suma como clave

    for total, dni_lista in suma_dict.items():  # Recorremos el diccionario para buscar coincidencias
        if len(dni_lista) > 1:  # Si hay más de un DNI con la misma suma...
            print(f"DNI con suma {total}: {', '.join(dni_lista)}")  # Imprimimos los DNIs que tienen la misma suma de dígitos

# Lista de DNIs
dnis = [dni_molina, dni_mele, dni_martinez, dni_meshler, dni_masseroni, dni_martilotta]

print("\n-----Búsqueda de pares de DNIs con sumas iguales-----")
buscar_pares_dni(dnis)  # Llamamos a la función para buscar pares de DNIs con sumas iguales

# El conjunto A y el conjunto B se consideran altamente compatibles si tienen tres o más dígitos en común.
def alta_compatibilidad(nombre1, conjunto1, nombre2, conjunto2):
    interseccion = interseccion_conjuntos(conjunto1, conjunto2)  # Usamos la función de intersección definida anteriormente
    if len(interseccion) >= 3:  # Si la intersección tiene 3 o más dígitos...
        return f"El {nombre1} tiene alta compatibilidad con el {nombre2}"
    else:  # Si hay menos de 3 elementos en común...
        return f"El {nombre1} tiene baja compatibilidad con el {nombre2}"

print("\n-----Compatibilidad entre conjuntos de DNIs-----")
# Comprobamos la compatibilidad entre el conjunto de Molina y los demás conjuntos
print("Compatibilidad:", alta_compatibilidad("conjunto Molina", conjunto_unico_molina, "conjunto Mele", conjunto_unico_mele))

# B. Operaciones con años de nacimiento
print("\n-----B. Operaciones con años de nacimiento-----")

# Creamos un diccionario con los años de nacimiento de los alumnos
anios_nacimiento = {
    "Molina": 1985,
    "Mele": 1991,
    "Martinez": 1997,
    "Meshler": 1989,
    "Masseroni": 1996,
    "Martilotta": 1999
}

# Obtenemos los años de nacimiento en una lista
lista_anios = list(anios_nacimiento.values())

# Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
pares = 0
for anio in lista_anios:
    if anio % 2 == 0:
        pares += 1

impares = len(lista_anios) - pares

print("\n-----Conteo de años pares e impares-----")
print(f"Cantidad de alumnos nacidos en años pares: {pares}")
print(f"Cantidad de alumnos nacidos en años impares: {impares}")

print("\n-----Grupo Z o Old School-----")
# Si todos nacieron después del 2000, mostrar "Grupo Z".
es_grupo_z = True

for anio in lista_anios:
    if anio <= 2000:
        es_grupo_z = False
        break

if es_grupo_z:
    print("Tenemos un Grupo Z")
else:
    print("Tenemos un Old School")

print("\n-----Años bisiestos-----")
# Implementar una función para determinar si un año es bisiesto.
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

# Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
for anio in lista_anios:
    if es_bisiesto(anio):
        print("Tenemos un año especial")
        break  # Detiene el ciclo en cuanto encuentra un año bisiesto


print("\n-----Años de nacimiento y edades-----")
# Calculamos las edades 
anio_actual = 2025
edades = {nombre: anio_actual - anio for nombre, anio in anios_nacimiento.items()} #for no anidado

# Producto cartesiano: cada persona con su año de nacimiento y edad
print("Relación entre años de nacimiento y edades:")
for nombre in anios_nacimiento:
    print(f"{nombre} nacio en {anios_nacimiento[nombre]} y tiene {edades[nombre]} años.")