# Incluimos todos los imports que serán necesario luego

import json
from simhash import Simhash, SimhashIndex
from collections import Counter, OrderedDict
import random
import spacy
import nltk
nltk.download("stopwords")
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import random

# 0. Cargando las noticias en memoria

# Abrimos el archivo especificando que tiene formato utf-8
with open('noticias-cambio-climático-españa-abril-2022-abril-2023-finales-sentencias-disagree-NOT-disagree.ndjson', encoding='utf-8') as archivo:
  lineas = archivo.readlines()

textos = list()
for linea in lineas:
  try:
    data = json.loads(linea)
    if len(data["sentencias_disagree"])<len(data["sentencias_NOT_disagree"]):
      texto = " ".join(data["sentencias"])
      texto = "".join(texto.splitlines())
      textos.append(texto)
  except:
    pass

print("0. Carga en memoria realizada")

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
print("1. Eliminados elementos cuasiduplicados")
print(len(textos_no_duplicados))

# 2.a y 2.b Segmentando la noticia y utilizando TextTiling

sentenciasTotales = list()
nlp = spacy.load("es_core_news_sm")
# No pasamos un texto entero, si no que vamos iterando y luego vamos sumando el resultado a una lista con sentencias
for i in range(len(textos_no_duplicados[0:100])):
  texto = textos_no_duplicados[i]
  doc = nlp(texto)
  sentencias = list(doc.sents)
  for j in range(len(sentencias)):
    sentencias[j] = sentencias[j].text
  sentenciasTotales = sentenciasTotales + sentencias

print("2.a Segmentada la noticia en sentencias usando spaCy")

# Conseguimos un texto único con todas las sentencias, separando con \n\n
texto = "\n\n".join(sentenciasTotales)

print("2.b Unidas esas sentencias en un único texto de tal modo que entre sentencia y sentencia haya un doble salto de línea \n\n")

print(texto[0:1000],"...")

# 2.c Aplicando TextTiling

stopwords_spanish = set(stopwords.words('spanish'))

tt = TextTilingTokenizer(stopwords=stopwords_spanish)

# Segmentamos el texto utilizando el algoritmo TextTiling
segments = tt.tokenize(texto)

# Imprimimos los segmentos

for i in range(len(segments)):
  segment=segments[i]
  print(i, " ".join(segment.splitlines()))

print("Texto segmentado en ",len(segments)," segmentos.")

print(len(segments))

for i in range(len(segments)):
  segment = segments[i]
  segment = segment.replace("\n\n","\n")

  print(i, segment.strip())
  print("---")

# 3. Cluster


# Vectorización
nlp = spacy.load("es_core_news_sm")
stop_words = list(spacy.lang.es.stop_words.STOP_WORDS)

# max_features sirve para indicar cuántos términos formarán nuestro vocabulario,
# a veces menos es más...

# Obsérvese que la tokenización que nos ofrece textacy para topic modeling es
# mucho más sofisticada (extracción de entidades y sintagmas nominales además
# de n-gramas). Por supuesto podríamos hacerlo usando spaCy pero
# `TfidfVectorizer` es taaan cómodo...

vectorizador = TfidfVectorizer(encoding="utf-8", lowercase=True,
                               stop_words=stop_words, ngram_range=(1,3),
                               max_features=10000)

print(segments)
doc_term_matrix = vectorizador.fit_transform(segments)
print(doc_term_matrix)

# Clustering con k-means

from sklearn.cluster import KMeans

# El número de clusters debe fijarse de antemano
#
num_clusters = 50

clustering1 = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=1000, n_init=1, verbose=True)

# Se aplica el algoritmo seleccionado a la matriz que representa el corpus
#
clustering1.fit(doc_term_matrix)


# Visualización

clustered_docs1 = dict()
docs_per_cluster1 = dict()

for i in range(len(clustering1.labels_)):
  try:
    clustered_docs1[clustering1.labels_[i]].append(i)
    docs_per_cluster1[clustering1.labels_[i]] += 1
  except:
    clustered_docs1[clustering1.labels_[i]] = list()
    clustered_docs1[clustering1.labels_[i]].append(i)
    docs_per_cluster1[clustering1.labels_[i]] = 1

ids = list(docs_per_cluster1.keys())
ids.sort()
sorted_docs_per_cluster1 = {i: docs_per_cluster1[i] for i in ids}

# De este modo obtenemos de nuevo el texto asociado a los términos (recordemos
# que con el vectorizador obtenemos una "traducción" totalmente numérica de los
# documentos).

terminos = vectorizador.get_feature_names_out()

# El atributo cluster_centers_ es un array n-dimensional (realmente bidimensional)
# que contiene el centroide de cada cluster en una matriz de clusters x términos
# definido por pesos flotantes obviamente
#
# El método argsort de numpy *no* ordena el array, retorna *otro* array de las
# mismas dimensiones que contiene *índices* en el orden en que deberían estar
# para que los *valores* del array (en este caso cluster_centers_) estuviera
# ordenado
#
# cluster_centers = .toarray()

indice_cluster_terminos1 = clustering1.cluster_centers_.argsort()[:, ::-1]

# Mostramos como mucho los 10 términos más representativos de cada cluster

for cluster_id in sorted_docs_per_cluster1:

  print("Cluster %d (%d documentos): " % (cluster_id, docs_per_cluster1[cluster_id]), end="")

  for term_id in indice_cluster_terminos1[cluster_id, :10]:
    # ¡Atención! El centro son coordenadas y dichas coordenadas son términos ya
    # que trabajamos con texto y, en consecuencia, aparecen todos los términos
    # del vocabulario... Un término solo nos interesará entonces si su valor
    # no es nulo.

    if clustering1.cluster_centers_[cluster_id][term_id] != 0:
      print('"%s"' % terminos[term_id], end=" ")

  print()

  ejemplares = clustered_docs1[cluster_id]
  random.shuffle(ejemplares)
  for ejemplar in ejemplares[0:5]:
    print("\t", textos_no_duplicados[ejemplar][0:140], "...")

  print()