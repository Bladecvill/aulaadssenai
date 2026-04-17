ml = [17, 8, 10, 6, 2, 4]

def ordena_lista(ml):

    for i in range(len(ml)):

        for j in range(i+1, len(ml)):
            if ml[i] > ml[j]:
                ml[i], ml[j] = \
                ml[j], ml[i]

ol = [ordena_lista(ml)]
print("Lista ordenada: ", ol)