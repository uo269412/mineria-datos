import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle

# 3. Cluster

with open('pickle/apartado3/clusteres.pickle', 'rb') as archivo:
  sorted_docs_per_cluster1 = pickle.load(archivo)

with open('pickle/apartado1/textos_no_duplicados.pickle', 'rb') as archivo:
  textos_no_duplicados = pickle.load(archivo)

with open('pickle/apartado3/docs_per_cluster1.pickle', 'rb') as archivo:
  docs_per_cluster1 = pickle.load(archivo)

with open('pickle/apartado3/indice_cluster_terminos1.pickle', 'rb') as archivo:
  indice_cluster_terminos1 =  pickle.load(archivo)

with open('pickle/apartado3/clustering1.pickle', 'rb') as archivo:
  clustering1 =  pickle.load(archivo)

with open('pickle/apartado2-tt/segments.pickle', 'rb') as archivo:
  segments = pickle.load(archivo)

with open('pickle/apartado3/clustered_docs1.pickle', 'rb') as archivo:
  clustered_docs1 = pickle.load(archivo)

with open('pickle/apartado3/terminos.pickle', 'rb') as archivo:
  terminos = pickle.load(archivo)

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
    print("\t", segments[ejemplar], "...")

  print()

with open('pickle/apartado3/clusteres.pickle', 'wb') as archivo:
  pickle.dump(sorted_docs_per_cluster1, archivo)

