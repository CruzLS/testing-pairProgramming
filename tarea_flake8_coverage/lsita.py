
medidas = list()
metros = -1
metrosCM = metros*100
pulgadas = metrosCM/2.54
pies = metrosCM/30.48
medidas.insert(0,pulgadas)
medidas.insert(0,pies)



for x in medidas:
    print(x)
