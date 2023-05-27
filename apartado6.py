import fasttext
import pickle

# Parece que la configuración de epoch = 28 es la que otorga mejores resultados
params = {
    'epoch': 28,
    'lr': 0.1,
    'dim': 100
}

# Ya que no podemos meter el modelo en pickle, y según las ejecuciones difieren, este programa solo aparece para ver
# unos resultados de como funciona el clasificador de manera general con el entrenamiento frente al testeo,
# más tarde en el fichero apartado8-d_e-clasificador.py, se creará otro modelo con la misma configuración para
# ponerlo a prueba contra las noticias negacionistas

modelo = fasttext.train_supervised("datos_adicionales/apartado4/conjunto-entrenamiento.txt", **params)
result = modelo.test("datos_adicionales/apartado4/conjunto-testeo.txt")

modelo.save_model("datos_adicionales/apartado6/modelo.bin")

print("Resultados de precisión: " + str(result[1]))
