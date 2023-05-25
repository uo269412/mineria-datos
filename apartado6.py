import fasttext

ruta_entrenamiento = "apartado4/conjunto-entrenamiento.txt"
modelo = fasttext.train_supervised(ruta_entrenamiento)
ruta_testeo = "apartado4/conjunto-testeo.txt"
result = modelo.test(ruta_testeo)

print()
