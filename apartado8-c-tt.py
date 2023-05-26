# Incluimos todos los imports que serán necesario luego

import spacy
import nltk

nltk.download("stopwords")
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
import pickle

print("- 8.c Aplicando TT - ")
print()

with open('datos_adicionales/pickle/apartado8-sp/texto-spacy.pickle', 'rb') as archivo:
    texto = pickle.load(archivo)

# 8.c Aplicando TextTiling

stopwords_spanish = set(stopwords.words('spanish'))

tt = TextTilingTokenizer(stopwords=stopwords_spanish)
segmentosTotales = list()

# Vamos a guardar una referencia que nos permita vincular el segmento con la noticia. Por lo tanto, la clave del
# diccionario será la posición del segmento en cuanto a la lista de segmentos, mientras que su valor se corresponderá
# con el índice que tiene la noticia en la lista de noticias

referenciasNoticias = {}

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
                referenciasNoticias[len(segmentosTotales) - 1] = i

with open('datos_adicionales/pickle/apartado8-tt/segments.pickle', 'wb') as archivo:
    pickle.dump(segmentosTotales, archivo)

with open('datos_adicionales/pickle/apartado8-tt/segments-noticias.pickle', 'wb') as archivo:
    pickle.dump(referenciasNoticias, archivo)
