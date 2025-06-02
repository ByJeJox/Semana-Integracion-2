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

# # Conjuntos de dígitos de los DNIs
# conjunto_unico_molina = []
# conjunto_unico_mele = []
# conjunto_unico_martinez = []
# conjunto_unico_meshler = []
# conjunto_unico_masseroni = []

# Función para formar un conjunto a partir de un DNI
def formar_conjunto_unico(dni):
    return set(dni)

# Formamos los conjuntos a partir de los DNIs y los asignamos a las variables correspondientes
# Generación automática de los conjuntos de dígitos únicos usando la funcion formar_conjunto_unico.
conjunto_unico_molina = formar_conjunto_unico(dni_molina)
conjunto_unico_mele = formar_conjunto_unico(dni_mele)
conjunto_unico_martinez = formar_conjunto_unico(dni_martinez)
conjunto_unico_meshler = formar_conjunto_unico(dni_meshler)
conjunto_unico_masseroni = formar_conjunto_unico(dni_masseroni)
conjunto_unico_martilotta = formar_conjunto_unico(dni_martilotta)

# Imprimimos los conjuntos
print("Conjunto de dígitos unicos del DNI de Molina: ", conjunto_unico_molina)
print("Conjunto de dígitos unicos del DNI de Mele: ", conjunto_unico_mele)
print("Conjunto de dígitos unicos del DNI de Martinez: ", conjunto_unico_martinez)
print("Conjunto de dígitos unicos del DNI de Meshler: ", conjunto_unico_meshler)
print("Conjunto de dígitos unicos del DNI de Masseroni: ", conjunto_unico_masseroni)
print("Conjunto de dígitos unicos del DNI de Martilotta: ", conjunto_unico_martilotta)

# print("Opcion 2 de Generación automática de los conjuntos de dígitos únicos")

# # Conjuntos de dígitos únicos de los DNIs generados automaticamente
# conjunto_unico_molina = set(dni_Molina)
# conjunto_unico_mele = set(dni_Mele)
# conjunto_unico_martinez = set(dni_Martinez)
# conjunto_unico_meshler = set(dni_Meshler)
# conjunto_unico_masseroni = set(dni_Masseroni)

# print("Conjunto único de Molina:", conjunto_unico_molina)
# print("Conjunto único de Mele:", conjunto_unico_mele)
# print("Conjunto único de Martinez:", conjunto_unico_martinez)
# print("Conjunto único de Meshler:", conjunto_unico_meshler)
# print("Conjunto único de Masseroni:", conjunto_unico_masseroni)

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
 
print("Diferencia entre Molina y Mele: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_mele))
print("Diferencia entre Molina y Martinez: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_martinez))
print("Diferencia entre Molina y Meshler: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_meshler))
print("Diferencia entre Molina y Masseroni: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_masseroni))
print("Diferencia entre Molina y Martilotta: ", diferencia_entre_pares(conjunto_unico_molina, conjunto_unico_martilotta))

# def diferencia_expresion(A, B):
#      return A - B

# print("Diferencia entre Molina y Mele (expresión): ", diferencia_expresion(conjunto_unico_molina, conjunto_unico_mele))


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


# Vista de las diferencias simétricas entre los conjuntos de molina con los demás
print("Diferencia simétrica entre Molina y Mele: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_mele))
print("Diferencia simétrica entre Molina y Martinez: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_martinez))
print("Diferencia simétrica entre Molina y Meshler: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_meshler))
print("Diferencia simétrica entre Molina y Masseroni: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_masseroni))
print("Diferencia simétrica entre Molina y Martilotta: ", diferencia_simetrica(conjunto_unico_molina, conjunto_unico_martilotta))

# def diferencia_simetrica_expresion(A, B):
#      return A ^ B

# print("Diferencia simétrica entre Molina y Mele (expresion): ", diferencia_simetrica_expresion(conjunto_unico_molina, conjunto_unico_mele))

# Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas
def contar_frecuencia_dni(dni):
    frecuencia = {}  # Diccionario aux para almacenar la frecuencia de cada dígito
    for digito in dni:  # Recorremos cada carácter del DNI
        if digito in frecuencia: # Si el dígito ya está en el diccionario
            frecuencia[digito] += 1  # Incrementamos la cuenta si ya existe
        else:
            frecuencia[digito] = 1  # Si no existe, lo inicializamos en 1
    return frecuencia


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

print("Suma de los dígitos del DNI de Molina: ", suma_digitos_dni(dni_molina))
print("Suma de los dígitos del DNI de Mele: ", suma_digitos_dni(dni_mele))
print("Suma de los dígitos del DNI de Martinez: ", suma_digitos_dni(dni_martinez))
print("Suma de los dígitos del DNI de Meshler: ", suma_digitos_dni(dni_meshler))
print("Suma de los dígitos del DNI de Masseroni: ", suma_digitos_dni(dni_masseroni))
print("Suma de los dígitos del DNI de Martilotta: ", suma_digitos_dni(dni_martilotta))


# Dígito compartido entre todos los conjuntos
def digitos_compartidos(conjunto1, conjunto2, conjunto3, conjunto4, conjunto5):
    conjunto_digitos_compartidos = []  # Usamos un conjunto para almacenar los dígitos compartidos

    for digito in "0123456789":  # Recorremos los dígitos del 0 al 9
        if digito in conjunto1 and digito in conjunto2 and digito in conjunto3 and digito in conjunto4 and digito in conjunto5:
            conjunto_digitos_compartidos.append(digito)  # Si el dígito está en todos los conjuntos, lo añadimos
    return conjunto_digitos_compartidos  # Devolvemos el conjunto de dígitos compartidos

print("Dígitos compartidos entre todos los conjuntos:",digitos_compartidos(conjunto_unico_molina, conjunto_unico_mele, conjunto_unico_martinez, conjunto_unico_meshler, conjunto_unico_masseroni, conjunto_unico_martilotta))

# Diversidad numérica alta si tiene mas de 6 digitos únicos

def diversidad_numerica_alta(conjunto):
    if len(conjunto) > 6:  # Si el conjunto tiene más de 6 dígitos únicos
        return "Diversidad Numerica Alta"
    else:
        return "Diversidad Numerica Baja"
    
print("Diversidad numérica del DNI de Molina:", diversidad_numerica_alta(conjunto_unico_molina))
print("Diversidad numérica del DNI de Mele:", diversidad_numerica_alta(conjunto_unico_mele))
print("Diversidad numérica del DNI de Martinez:", diversidad_numerica_alta(conjunto_unico_martinez))
print("Diversidad numérica del DNI de Meshler:", diversidad_numerica_alta(conjunto_unico_meshler))
print("Diversidad numérica del DNI de Masseroni:", diversidad_numerica_alta(conjunto_unico_masseroni))
print("Diversidad numérica del DNI de Martilotta:", diversidad_numerica_alta(conjunto_unico_martilotta))


# print("------------Logica------------")


# # Expresión lógica 1: "Los dígitos que están en A y no en B"
# def diferencia_expresion(A, B):
#     return A - B

#------------------------------------------

# # Expresión lógica 2: "Los dígitos que están en A o en B, pero no en ambos"
# def diferencia_simetrica_expresion(A, B):
#     return A ^ B

#------------------------------------------
# # Expresión lógica 3: "Los dígitos que aparecen en los tres DNIs a la vez"
# def interseccion_tres_conjuntos(A, B, C):
#     return A & B & C

# def interseccion_varios_conjuntos(*conjuntos):
#     interseccion = conjuntos[0]  # Empezamos con el primer conjunto
#     for conjunto in conjuntos[1:]:  # Iteramos sobre los restantes
#         interseccion &= conjunto  # Aplicamos la intersección
#     return interseccion

# # Ejemplo de uso
# conjunto_unico_molina = {'3', '9', '8', '2', '4', '5'}
# conjunto_unico_mele = {'4', '5', '1', '2', '7', '6', '3', '9'}
# conjunto_unico_martinez = {'5', '6', '7', '8', '9', '0'}

# resultado = interseccion_varios_conjuntos(conjunto_unico_molina, conjunto_unico_mele, conjunto_unico_martinez)
# print("Dígitos que aparecen en los tres DNIs:", resultado)

# B. Operaciones con años de nacimiento
print("-----B. Operaciones con años de nacimiento-----")
from itertools import product

#Creamos un diccionario con los años de nacimiento de los alumnos
anios_nacimiento = {
    "Molina": 1985,
    "Mele": 1991,
    "Martinez": 1997,
    "Meshler": 1990,
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

print(f"Cantidad de alumnos nacidos en años pares: {pares}")
print(f"Cantidad de alumnos nacidos en años impares: {impares}")

# Si todos nacieron después del 2000, mostrar "Grupo Z".
es_grupo_z = True

for anio in lista_anios:
    if anio <= 2000:
        es_grupo_z = False
        break

if es_grupo_z:
    print("Grupo Z")
else:
    print("Old School")

# Implementar una función para determinar si un año es bisiesto.
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

# Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
if any(es_bisiesto(anio) for anio in lista_anios):
    print("Tenemos un año especial")

# Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.

# Calculamos las edades 
anio_actual = 2025
edades = {nombre: anio_actual - anio for nombre, anio in anios_nacimiento.items()}

# Producto cartesiano: cada persona con su año de nacimiento y edad
print("\nRelación entre años de nacimiento y edades:") # Usamos \n para que se imprima en una nueva línea
for nombre in anios_nacimiento:
    print(f"({nombre}, {anios_nacimiento[nombre]}) x ({nombre}, {edades[nombre]})")