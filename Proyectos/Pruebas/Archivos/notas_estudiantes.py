# 1era Forma
# notas = {
#    "Nora": 87,
#    "Gino": 100,
#    "Loretto": 67,
#    "Talina": 45
#}

# with open("data_estudiantes.txt", "w") as archivo:
#    for nombre, nota in notas.items():
#        archivo.write(nombre + " - " + str(nota) + "\n")

# 2da Forma
nuevas_notas = {
    "Emily": 54,
    "Daniel": 98,
    "Junienne": 78
}

with open("data_estudiantes.txt", "a") as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")        
