import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import pickle
import fasttext

with open('datos_adicionales/pickle/apartado8-tt/segments.pickle', 'rb') as archivo:
    segments = pickle.load(archivo)

with open('datos_adicionales/pickle/apartado8-tt/segments-noticias.pickle', 'rb') as archivo:
    referenciasNoticias = pickle.load(archivo)

with open('datos_adicionales/pickle/apartado7/textos.pickle', 'rb') as archivo:
    noticias = pickle.load(archivo)

global escritor
escritor = open("datos_adicionales/apartado8/lista-labels.noticias.ndjson", "w", encoding='utf-8')

lista = list()


def escribeLinea(texto=""):
    escritor.write(texto + "\n")


def estructuraLabel(label="", porcentaje=0.0):
    return '"' + label + '": ' + str(porcentaje) + ","


def calcular_porcentaje(lista, valor):
    repeticiones = lista.count(valor)
    porcentaje = round((repeticiones / len(lista)), 2)
    return porcentaje


labels = ["temperatura_media", "crisis_climática", "hidrógeno_verde", "dióxido_carbono", "transición_energética",
          "energía_renovable", "emisiones_co2", "olas_calor", "sequía_agua", "efecto_invernadero"]

# Parece que la configuración de epoch = 28 es la que otorga mejores resultados
params = {
    'epoch': 28,
    'lr': 0.1,
    'dim': 100
}

ruta_entrenamiento = "datos_adicionales/apartado4/conjunto-entrenamiento.txt"
modelo = fasttext.train_supervised(ruta_entrenamiento, **params)
ruta_testeo = "datos_adicionales/apartado4/conjunto-testeo.txt"
result = modelo.test(ruta_testeo)

print("Precisión: " + str(result[1]))

# Comenzamos con la noticia 0, es decir, la primera
previousValue = 0
lista_noticia = list()

# Aquí iteramos por cada segmento, sabiendo a que noticia le corresponde, y calculamos el porcentaje de segmentos que
# pertenecen a dicha label


for i in range(len(segments)):
    if referenciasNoticias[i] != previousValue:
        string = '{"noticia": ' + '"' + noticias[previousValue] + '"' + ","
        # Obtenemos el índice de la noticia al que pertenece el segmento, es decir, al entrar en el if hemos cambiado
        # de noticia
        previousValue = referenciasNoticias[i]

        string += '"etiquetas" : {'
        for i in range(len(labels)):
            repeticiones = calcular_porcentaje(lista_noticia, labels[i])
            # No queremos incluir todas las etiquetas en el ndjson, solo aquellas que pertenecen a los segmentos d
            # elas noticias
            if (repeticiones != 0):
                string += estructuraLabel(labels[i], repeticiones)
        # Quitamos la última coma que se añade
        string = string[:-1]
        string += "}}"
        escribeLinea(string)
        # Comenzamos una nueva noticia
        lista_noticia = list()
    # Quitamos el fragmento que tiene label, ya que queremos dejar solamente las etiquetas
    lista_noticia.append(modelo.predict(segments[i])[0][0].replace("__label__", ""))


print("Se ha generado el archivo njdson en datos_adicionales/apartado8")
