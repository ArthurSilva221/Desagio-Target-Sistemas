xml =   [22174.1664,24537.6698,26139.6134,0,0,26742.6612,0,42889.2258,46251.174,
        11191.4722, 0,0,3847.4823,373.7838,2659.7563,48924.2448,18419.2614,0,0,
        35240.1826,43829.1667,18235.6852,4355.0662,13327.1025,0,0,25681.8318,
        1718.1221,13220.495,8414.61]

valor =[]
dias = []
faturamento=([],[])

cont = 0
for i in xml:
    cont = cont + 1
    if i > 0:
        valor.append(i)
        dias.append(cont)

        faturamento=(dias,valor)

def maior_fat(faturamento):
    anterior = 0
    cont=0
    for x in faturamento[1]:
        cont= cont + 1
        if x > anterior:
            anterior = x
            dia = faturamento[0][cont-1]

    return print("Dia",dia, "possui o maior valor, sendo dê ", anterior,"R$.")

def menor_fat(faturamento):
    antes = faturamento[1][0]
    cont = -1
    for x in faturamento[0]:
        cont = cont +1

        if antes > faturamento[1][cont]:
            antes = faturamento[1][cont]
            day = x

    return print("Dia",day, "possui o maior valor, sendo dê ", antes,"R$.")

def media_fat(faturamento):
    numdig = 0
    cont = 0

    for i in faturamento[1]:
        cont=cont+1
        numdig=numdig+i

    media = numdig/cont
    aux = 0

    print("Media atual do faturamento:",media)
    print("Sequência de dias que foram maiores que a media:")

    for x in faturamento[1]:
        aux = aux + 1
        if x > media:
            valor = x
            dia = faturamento[0][aux - 1]

            print(dia,valor)

maior_fat(faturamento)
menor_fat(faturamento)
media_fat(faturamento)







