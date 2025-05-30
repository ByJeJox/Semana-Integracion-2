# DNI alumnos
# Ingreso de los DNIs (reales o ficticios).
dni_Molina = "31476619"
dni_Mele = "36552513"
dni_Martinez = "39964587"
dni_Meshler = "34433376"
dni_Masseroni = "39600348"

# Conjuntos de dígitos de los DNIs
conjunto_molina = []
conjunto_mele = []
conjunto_martinez = []
conjunto_meshler = []
conjunto_masseroni = []

# Función para formar un conjunto a partir de un DNI
def formar_conjunto_unico(dni):
    return set(dni)

# Formamos los conjuntos a partir de los DNIs y los asignamos a las variables correspondientes
# Generación automática de los conjuntos de dígitos únicos usando la funcion formar_conjunto_unico.
conjunto_molina = formar_conjunto_unico(dni_Molina)
conjunto_mele = formar_conjunto_unico(dni_Mele)
conjunto_martinez = formar_conjunto_unico(dni_Martinez)
conjunto_meshler = formar_conjunto_unico(dni_Meshler)
conjunto_masseroni = formar_conjunto_unico(dni_Masseroni)

# Imprimimos los conjuntos
print("Conjunto de dígitos unicos del DNI de Molina: ", conjunto_molina)
print("Conjunto de dígitos unicos del DNI de Mele: ", conjunto_mele)
print("Conjunto de dígitos unicos del DNI de Martinez: ", conjunto_martinez)
print("Conjunto de dígitos unicos del DNI de Meshler: ", conjunto_meshler)
print("Conjunto de dígitos unicos del DNI de Masseroni: ", conjunto_masseroni)

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


# # Función para sumar los dígitos de un DNI
# NO PEDIDA
# def suma_digitos(conjunto_dni):
#     return sum(int(digit) for digit in conjunto_dni)

# print("Suma de los dígitos del DNI de Molina: ", suma_digitos(conjunto_molina))
# print("Suma de los dígitos del DNI de Mele: ", suma_digitos(conjunto_mele))
# print("Suma de los dígitos del DNI de Martinez: ", suma_digitos(conjunto_martinez))
# print("Suma de los dígitos del DNI de Meshler: ", suma_digitos(conjunto_meshler))
# print("Suma de los dígitos del DNI de Masseroni: ", suma_digitos(conjunto_masseroni))

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
print("Unión de Molina y Mele: ", union_conjuntos(conjunto_molina, conjunto_mele))
print("Unión de Molina y Martinez: ", union_conjuntos(conjunto_molina, conjunto_martinez))
print("Unión de Molina y Meshler: ", union_conjuntos(conjunto_molina, conjunto_meshler))
print("Unión de Molina y Masseroni: ", union_conjuntos(conjunto_molina, conjunto_masseroni))


# Función para encontrar la intersección de dos conjuntos
def interseccion_conjuntos(conjunto1, conjunto2):
    conjunto_interseccion = []
    for i in conjunto1:
        if i in conjunto2 and i not in conjunto_interseccion:
            conjunto_interseccion.append(i)
    return conjunto_interseccion

print("Intersección de Molina y Mele: ", interseccion_conjuntos(conjunto_molina, conjunto_mele))

# Expresión lógica 1: "Los dígitos que están en conjunto1 y no están en conjunto2"
def diferencia_entre_pares(conjunto1, conjunto2):
    conjunto_diferencia = []
    for i in conjunto1:
        if i not in conjunto2 and i not in conjunto_diferencia:
            conjunto_diferencia.append(i)
    return conjunto_diferencia
 
print("Diferencia entre Molina y Mele: ", diferencia_entre_pares(conjunto_molina, conjunto_mele))

def diferencia_simetrica(conjunto1, conjunto2):
    conjunto_diferencia_simetrica = []
    for i in conjunto1:
        if i not in conjunto2 and i not in conjunto_diferencia_simetrica:
            conjunto_diferencia_simetrica.append(i)
    
    for i in conjunto2:
        if i not in conjunto1 and i not in conjunto_diferencia_simetrica:
            conjunto_diferencia_simetrica.append(i)
    
    return conjunto_diferencia_simetrica


print("Diferencia simétrica entre Molina y Mele: ", diferencia_simetrica(conjunto_molina, conjunto_mele))
print("Diferencia simétrica entre Molina y Martinez: ", diferencia_simetrica(conjunto_mele, conjunto_molina))

print("------------Logica------------")


set_molina = set(conjunto_molina)
set_mele = set(conjunto_mele)
set_martinez = set(conjunto_martinez)

# Expresión lógica 1: "Los dígitos que están en A y no en B"
def diferencia_expresion(A, B):
    return A - B

# Expresión lógica 2: "Los dígitos que están en A o en B, pero no en ambos"
def diferencia_simetrica_expresion(A, B):
    return A ^ B

# Expresión lógica 3: "Los dígitos que aparecen en los tres DNIs a la vez"
def interseccion_tres_conjuntos(A, B, C):
    return A & B & C

expresion_1 = diferencia_expresion(set_molina, set_mele)
expresion_2 = diferencia_simetrica_expresion(set_molina, set_mele)
expresion_3 = interseccion_tres_conjuntos(set_molina, set_mele, set_martinez)

print("Expresión 1 (A y no en B):", expresion_1)
print("Expresión 2 (A o B, pero no en ambos):", expresion_2)
print("Expresión 3 (En los tres DNIs):", expresion_3)
