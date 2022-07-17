import colorgram

#extrai as 3 cores mais comuns da imagem
cores = colorgram.extract('teste.jpg',3)

coresRgb = []

for i in range(3):
    coresRgb.append(cores[i].rgb)

print(coresRgb)