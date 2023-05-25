# Incluimos todos los imports que serán necesario luego

import spacy
import nltk
nltk.download("stopwords")
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
import pickle

print("- 2.a Segmentando las noticias - ")
print()

# 2.a y 2.b Segmentando la noticia y utilizando TextTiling

with open('pickle/apartado1/textos_no_duplicados.pickle', 'rb') as archivo:
    textos_no_duplicados = pickle.load(archivo)

sentenciasTotales = list()
nlp = spacy.load("es_core_news_sm")
# No pasamos un texto entero, si no que vamos iterando y luego vamos sumando el resultado a una lista con sentencias
for i in range(len(textos_no_duplicados)):
  print(" Progreso segmentando: " + str(i) + " de un total de " + str(len(textos_no_duplicados)))
  texto = textos_no_duplicados[i]
  doc = nlp(texto)
  sentencias = list(doc.sents)
  for j in range(len(sentencias)):
    sentencias[j] = sentencias[j].text
  sentencias = "\n\n".join(sentencias)
  sentenciasTotales.append(sentencias)

print("- 2. Segmentada las noticias en sentencias usando spaCy - ")

print(texto[0:1000],"...")

with open('pickle/apartado2-sp/texto-spacy.pickle', 'wb') as archivo:
  pickle.dump(sentenciasTotales, archivo)
