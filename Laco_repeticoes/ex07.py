import random
ns = random.randint(1,100)
tent = 1

while tent <= 3:
    pal = int(input("Adivinhe o numero:"))
    if pal == ns:
        print("Você sabe muito")
        
        break
    else:
        if pal > ns:
            print("dica: é menos")
        else:
            print("dica: é mais")
    tent += 1
if tent > 3:
    print("Perdeu playboy")
    print("o numero era", ns)