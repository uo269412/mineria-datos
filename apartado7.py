# Incluimos todos los imports que serán necesario luego

import json
from simhash import Simhash, SimhashIndex
from collections import Counter, OrderedDict
import random
import pickle

global escritor
escritor = open("datos_adicionales/apartado7/noticias-negacionista.txt", "w", encoding='utf-8')

lista = list()


def escribeLinea(texto=""):
    escritor.write(texto + "\n")


# 7. Cargando las noticias en memoria

print("- 7. Cargando las noticias negacionistas en memoria -")
print()

# Abrimos el archivo especificando que tiene formato utf-8
with open('noticias-cambio-climático-españa-abril-2022-abril-2023-finales-sentencias-disagree-NOT-disagree.ndjson',
          encoding='utf-8') as archivo:
    lineas = archivo.readlines()

textos = list()
for linea in lineas:
    try:
        data = json.loads(linea)
        if len(data["sentencias_disagree"]) > len(data["sentencias_NOT_disagree"]):
            texto = " ".join(data["sentencias"])
            texto = "".join(texto.splitlines())
            textos.append(texto)
    except:
        pass

print("- 7. Carga en memoria realizada -")
print("Total de noticias negacionistas a analizar:" + str(len(textos)))
print()

with open('datos_adicionales/pickle/apartado7/textos.pickle', 'wb') as archivo:
    pickle.dump(textos, archivo)
