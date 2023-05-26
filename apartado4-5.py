import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle

with open('datos_adicionales/pickle/apartado1/textos_no_duplicados.pickle', 'rb') as archivo:
    textos_no_duplicados = pickle.load(archivo)

with open('datos_adicionales/pickle/apartado3/clustered_docs1.pickle', 'rb') as archivo:
    clustered_docs1 = pickle.load(archivo)

with open('datos_adicionales/pickle/apartado2-tt/segments.pickle', 'rb') as archivo:
    segments = pickle.load(archivo)

global entrenamiento
entrenamiento = open("datos_adicionales/apartado4/conjunto-entrenamiento.txt", "w", encoding='utf-8')

global testeo
testeo = open("datos_adicionales/apartado4/conjunto-testeo.txt", "w", encoding='utf-8')

lista = list()


def escribeLinea(escritor, texto=""):
    escritor.write(texto + "\n")


def obtenerFormatoNoticia(label, ejemplares):
    for ejemplar in ejemplares:
        texto = segments[ejemplar].replace("\n", "")
        lista.append("__label__" + label + " " + texto)


# 4. y 5. Ponemos el label a los clústeres según se ha considerado. Escogiendo diez clústeres y poniéndole un label
# acorde a la información proporcionada

obtenerFormatoNoticia("temperatura_media", clustered_docs1[1])
obtenerFormatoNoticia("crisis_climática", clustered_docs1[1])
obtenerFormatoNoticia("hidrógeno_verde", clustered_docs1[7])
obtenerFormatoNoticia("dióxido_carbono", clustered_docs1[8])
obtenerFormatoNoticia("transición_energética", clustered_docs1[12])
obtenerFormatoNoticia("energía_renovable", clustered_docs1[14])
obtenerFormatoNoticia("emisiones_co2", clustered_docs1[15])
obtenerFormatoNoticia("olas_calor", clustered_docs1[17])
obtenerFormatoNoticia("sequía_agua", clustered_docs1[21])
obtenerFormatoNoticia("efecto_invernadero", clustered_docs1[22])

# 80% para el entrenamiento

porcentajeEntrenamiento = 0.8
numero_elementos_entrenamiento = int(len(lista) * porcentajeEntrenamiento)
conjuntoEntrenamiento = random.sample(lista, numero_elementos_entrenamiento)

for elemento in conjuntoEntrenamiento:
    escribeLinea(entrenamiento, elemento)

# 20% (restante) para el testeo

conjuntoTesteo = list(set(lista) - set(conjuntoEntrenamiento))

for elemento in conjuntoTesteo:
    escribeLinea(testeo, elemento)

print("Se han generado los dos archivos, tanto de entrenamiento como de testeo, en datos_adicionales/apartado4")