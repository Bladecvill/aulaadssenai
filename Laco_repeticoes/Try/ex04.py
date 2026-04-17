def salvar_registro():
    arquivo = None
    
    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        arquivo = open("registro_usuarios.txt", "a", encoding="utf-8")
        arquivo.write (f"Nome: {nome} | Idade: {idade}\n")
        print("Registro salvo com sucesso!")
        
    except ValueError: 
        print("Valor inválido. Por favor, insira um número para a idade.")
    
    except IOError:
        print(f"Erro ao acessar o arquivo. Verifique as permissões e tente novamente. ({e})")

    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado com sucesso!")
        else:
            print("Nenhum arquivo foi aberto, portanto, não há necessidade de fechar.") 
               
salvar_registro()