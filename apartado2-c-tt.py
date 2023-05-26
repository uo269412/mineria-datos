# Incluimos todos los imports que serán necesario luego

import spacy
import nltk

nltk.download("stopwords")
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
import pickle

print("- 2.c Aplicando TT - ")
print()

with open('datos_adicionales/pickle/apartado2-sp/texto-spacy.pickle', 'rb') as archivo:
    texto = pickle.load(archivo)

# 2.c Aplicando TextTiling

stopwords_spanish = set(stopwords.words('spanish'))

tt = TextTilingTokenizer(stopwords=stopwords_spanish)
segmentosTotales = list()

# Segmentamos el texto utilizando el algoritmo TextTiling
for i in range(len(texto)):
    try:
        segments = tt.tokenize(texto[i])
    except:
        print("Esta noticia no se pudo procesar: " + texto[i])
    print("[TT] Procesando " + str(i) + " de un total de " + str(len(texto) - 1) + " - Texto segmentado en ",
          str(len(segments)), " segmentos.")

    for j in range(len(segments)):
        segment = segments[j]
        elements = segment.split("\n\n")
        for element in elements:
            if element not in segmentosTotales:
                segmentosTotales.append(element)

with open('datos_adicionales/pickle/apartado2-tt/segments.pickle', 'wb') as archivo:
    pickle.dump(segmentosTotales, archivo)
