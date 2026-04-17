try:
    file = open("arquivo.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Arquivo não encontrado") 

finally:
    print("Finalizando a operacao...")
    if'file' in locals() and not file.close:
        file.close()
        print("Arquivo fechado com sucesso!")