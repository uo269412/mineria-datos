import subprocess

# Lista de programas a ejecutar
programas = [
    './apartado1.py',
    './apartado2-sp.py',
    './apartado2-tt.py',
    './apartado3.py',
    './apartado4-5.py'
]

for programa in programas:
    subprocess.run(['python', programa])