f = open('datos1.txt', 'r')



def extraer(datos):
    fila1 = []
    fila2 = []
    for linea in datos:
        f1, f2 = linea.split('   ')
        fila1.append(int(f1))
        fila2.append(int(f2))
    return sorted(fila1), sorted(fila2)

def distancia(i, j):
    return abs(i - j)

def fase1(fila1, fila2):
    res = 0
    for i in range(len(fila1)):
        res += distancia(fila1[i], fila2[i])
    print(res)

def conteo(valor, fila2):
    return fila2.count(valor)

def fase2(fila1, fila2):
    s_score = 0
    for i in fila1:
        if i in fila2:
            s_score += conteo(i, fila2) * i
    return s_score

if __name__ == '__main__':
    fila1, fila2 = extraer(f)
    print(fase1(fila1, fila2))
    print(fase2(fila1, fila2))
