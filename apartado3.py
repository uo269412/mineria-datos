import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle

# 3. Cluster

with open('pickle/apartado2-tt/segments.pickle', 'rb') as archivo:
  segments = pickle.load(archivo)

with open('pickle/apartado2-tt/segments-noticias.pickle', 'rb') as archivo:
  referenciasNoticias = pickle.load(archivo)

with open('pickle/apartado1/textos_no_duplicados.pickle', 'rb') as archivo:
  textos_no_duplicados = pickle.load(archivo)

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

doc_term_matrix = vectorizador.fit_transform(segments)
print(doc_term_matrix)

# Clustering con k-means

from sklearn.cluster import KMeans

# El número de clusters debe fijarse de antemano
#
num_clusters = 15

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
    print("\t",textos_no_duplicados[referenciasNoticias[ejemplar]][0:140], "...")
  print()

# Guardamos los resultados del clustering (Aunque no vayamos a utilizar todos)

with open('pickle/apartado3/sorted_docs_per_cluster1.pickle', 'wb') as archivo:
  pickle.dump(sorted_docs_per_cluster1, archivo)

with open('pickle/apartado3/docs_per_cluster1.pickle', 'wb') as archivo:
  pickle.dump(docs_per_cluster1, archivo)

with open('pickle/indice_cluster_terminos1.pickle.pickle', 'wb') as archivo:
  pickle.dump(indice_cluster_terminos1, archivo)

with open('pickle/clustering1.pickle.pickle', 'wb') as archivo:
  pickle.dump(clustering1, archivo)

with open('pickle/apartado3/clustered_docs1.pickle', 'wb') as archivo:
  pickle.dump(clustered_docs1, archivo)

with open('pickle/terminos.pickle.pickle', 'wb') as archivo:
  pickle.dump(terminos, archivo)