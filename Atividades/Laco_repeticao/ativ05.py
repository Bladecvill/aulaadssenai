
# Simulação de urna eletrônica

# Inicialização dos contadores
votos_jair = 0
votos_carlos = 0
votos_neves = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

while True:
    print("\nAs opcoes sao:")
    print("1. Candidato Jair Rodrigues")
    print("2. Candidato Carlos Luz")
    print("3. Candidato Neves Rocha")
    print("4. Nulo")
    print("5. Branco")
    print("6. Encerrar votação")

    try:
        voto = int(input("Entre com o seu voto: "))

        if voto == 6:
            break
        elif voto == 1:
            votos_jair += 1
        elif voto == 2:
            votos_carlos += 1
        elif voto == 3:
            votos_neves += 1
        elif voto == 4:
            votos_nulos += 1
        elif voto == 5:
            votos_brancos += 1
        else:
            print("Opção inválida. Voto não computado.")
            continue # Pula para a próxima iteração sem contar o voto

        total_votos += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


# Apresentação dos resultados
print("\n--- Resultados da Votação ---")
print(f"Votos para Jair Rodrigues: {votos_jair}")
print(f"Votos para Carlos Luz: {votos_carlos}")
print(f"Votos para Neves Rocha: {votos_neves}")
print(f"Votos Nulos: {votos_nulos}")
print(f"Votos em Branco: {votos_brancos}")

if total_votos > 0:
    porc_nulos = (votos_nulos / total_votos) * 100
    porc_brancos = (votos_brancos / total_votos) * 100
    print(f"Porcentagem de votos nulos: {porc_nulos:.2f}%")
    print(f"Porcentagem de votos brancos: {porc_brancos:.2f}%")

# Determina o vencedor (considerando apenas os votos válidos nos candidatos)
votos_validos = {
    "Jair Rodrigues": votos_jair,
    "Carlos Luz": votos_carlos,
    "Neves Rocha": votos_neves
}

if not any(v > 0 for v in votos_validos.values()):
    print("Não houve vencedor (nenhum voto para os candidatos).")
else:
    vencedor = max(votos_validos, key=votos_validos.get)
    # Verifica se houve empate
    maior_votacao = votos_validos[vencedor]
    candidatos_empatados = [c for c, v in votos_validos.items() if v == maior_votacao]

    if len(candidatos_empatados) > 1:
        print(f"Houve um empate entre: {', '.join(candidatos_empatados)}")
    else:
        print(f"O candidato vencedor é: {vencedor}")
