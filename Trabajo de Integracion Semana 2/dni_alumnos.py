# DNI alumnos
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
def formar_conjunto_dni(dni):
    list_dni = []
    for i in range(0, len(dni)):
         list_dni.append (dni[i])
    return list_dni

# Formamos los conjuntos a partir de los DNIs
conjunto_molina = formar_conjunto_dni(dni_Molina)
conjunto_mele = formar_conjunto_dni(dni_Mele)
conjunto_martinez = formar_conjunto_dni(dni_Martinez)

# Función para sumar los dígitos de un DNI
def suma_digitos(dni):
    return sum(int(digit) for digit in dni)

print("Suma de los dígitos del DNI de Molina: ", suma_digitos(dni_Molina))
print("Suma de los dígitos del DNI de Mele: ", suma_digitos(dni_Mele))
print("Suma de los dígitos del DNI de Martinez: ", suma_digitos(dni_Martinez))

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

print("DNI de Molina: ", conjunto_molina)
print("DNI de Mele: ", conjunto_mele)
print("Unión de Molina y Mele: ", union_conjuntos(conjunto_molina, conjunto_mele))


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
