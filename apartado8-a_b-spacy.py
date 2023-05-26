# Incluimos todos los imports que serán necesario luego

import spacy
import nltk
nltk.download("stopwords")
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
import pickle

print("- 8.a Segmentando las noticias - ")
print()

# 8.a y 8.b Segmentando la noticia en sentencias

with open('datos_adicionales/pickle/apartado7/textos.pickle', 'rb') as archivo:
    textos = pickle.load(archivo)

sentenciasTotales = list()
nlp = spacy.load("es_core_news_sm")
# No pasamos un texto entero, si no que vamos iterando y luego vamos sumando el resultado a una lista con sentencias
for i in range(len(textos)):
  print(" Progreso segmentando: " + str(i) + " de un total de " + str(len(textos)))
  texto = textos[i]
  doc = nlp(texto)
  sentencias = list(doc.sents)
  for j in range(len(sentencias)):
    sentencias[j] = sentencias[j].text
  sentencias = "\n\n".join(sentencias)
  sentenciasTotales.append(sentencias)

print("- 8. Segmentadas las noticias en sentencias usando spaCy - ")

print(texto[0:1000],"...")

with open('datos_adicionales/pickle/apartado8-sp/texto-spacy.pickle', 'wb') as archivo:
  pickle.dump(sentenciasTotales, archivo)
