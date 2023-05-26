# Incluimos todos los imports que serán necesario luego

import json
from simhash import Simhash, SimhashIndex
from collections import Counter, OrderedDict
import random
import pickle

# 0. Cargando las noticias en memoria

print("- 0. Cargando las noticias en memoria -")
print()

# Abrimos el archivo especificando que tiene formato utf-8
with open('noticias-cambio-climático-españa-abril-2022-abril-2023-finales-sentencias-disagree-NOT-disagree.ndjson',
          encoding='utf-8') as archivo:
    lineas = archivo.readlines()

textos = list()
for linea in lineas:
    try:
        data = json.loads(linea)
        if len(data["sentencias_disagree"]) < len(data["sentencias_NOT_disagree"]):
            texto = " ".join(data["sentencias"])
            texto = "".join(texto.splitlines())
            textos.append(texto)
    except:
        pass

print("- 0. Carga en memoria realizada -")
print()
print("- 1. Eliminando elementos cuasi-duplicados -")

# 1. Eliminamos elementos cuasi-duplicados
firmas = []

# El valor de f por defecto en Simhash es de 64 bits y para este caso concreto
# resulta demasiado bajo y produce excesivas colisiones.

valor_f = 128

observaciones = []

# Creamos las firma de cada documento
for i in range(len(textos)):
    texto = textos[i]

    firma = Simhash(texto, f=valor_f)
    firmas.append((i, firma))  # Lo ideal sería almacenar una tupla (id_str, firma)

# Se crea un índice con las firmas

indice = SimhashIndex(firmas, k=10, f=valor_f)

# Determinamos cuántos duplicados hay en la colección

for i in range(len(textos)):
    firma = firmas[i][1]
    duplicados = indice.get_near_dups(firma)

    observaciones.append(len(duplicados))

print()

print(Counter(observaciones).most_common(50))

# Los textox únicos se almacenarán aquí

textos_no_duplicados = list()

# Anotaremos los identificadores (realmente índices en la lista original) de los
# textos que hay que ignorar porque son duplicados de un texto que ha sido
# añadido a la lista de textos únicos

ignorar = list()

for i in range(len(textos)):
    if i not in ignorar:
        texto = textos[i]

        # firma = Simhash(texto, f=valor_f)
        firma = firmas[i][1]

        duplicados = indice.get_near_dups(firma)

        # Si el texto no tiene duplicados se añade a la lista
        # y se apunta a ignorar (sí, sé que es innecesario...)

        if len(duplicados) == 1:
            textos_no_duplicados.append(texto)
            ignorar.append(i)
        else:
            # Barajamos la lista de duplicados

            random.shuffle(duplicados)

            # Cogemos el primero de la lista barajada

            ident = int(duplicados[0])

            # Se añade y se ignoran *todos* los documentos duplicados

            textos_no_duplicados.append(textos[ident])
            for ident in duplicados:
                ignorar.append(int(ident))

print()
print("- 1. Eliminados elementos cuasiduplicados - ")
print()
print("Total de noticias a analizar:" + len(textos_no_duplicados))
print()

with open('datos_adicionales/pickle/apartado1/textos_no_duplicados.pickle', 'wb') as archivo:
    pickle.dump(textos_no_duplicados, archivo)
