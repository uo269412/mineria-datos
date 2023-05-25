import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle


with open('pickle/apartado1/textos_no_duplicados.pickle', 'rb') as archivo:
    textos_no_duplicados = pickle.load(archivo)

with open('pickle/apartado3/clustered_docs1.pickle', 'rb') as archivo:
    clustered_docs1 = pickle.load(archivo)

with open('pickle/apartado2-tt/segments-noticias.pickle', 'rb') as archivo:
    referenciasNoticias = pickle.load(archivo)

global entrenamiento
entrenamiento = open("apartado4/conjunto-entrenamiento.txt", "w", encoding='utf-8')

global testeo
testeo = open("apartado4/conjunto-testeo.txt", "w", encoding='utf-8')

lista = list()

def escribeLinea(escritor, texto=""):
    escritor.write(texto + "\n")


def obtenerFormatoNoticia(label, ejemplares):
    for ejemplar in ejemplares:
        texto = textos_no_duplicados[referenciasNoticias[ejemplar]].replace("\n", "")
        lista.append("__label__" + label + " " + texto)


# 4. y 5. Ponemos el label a los clústeres según se ha considerado. Escogiendo seis clústeres y poniéndole un label acorde a
# la información proporcionada

obtenerFormatoNoticia("calentamientoglobal", clustered_docs1[0])
obtenerFormatoNoticia("desarrollosostenible", clustered_docs1[1])
obtenerFormatoNoticia("energiarenovablesolar", clustered_docs1[5])
obtenerFormatoNoticia("emisionescarbono", clustered_docs1[7])
obtenerFormatoNoticia("combustiblesfosiles", clustered_docs1[10])
obtenerFormatoNoticia("consumoagua", clustered_docs1[14])

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
