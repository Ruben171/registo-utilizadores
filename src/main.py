from .utils import verificar_idade

def main():
    utilizadores = []

    while True:
        nome = input("Nome (ou 'sair' para terminar): ")
        if nome.lower() == "sair":
            break

        idade = int(input("Idade: "))
        status = verificar_idade(idade)

        utilizadores.append({"nome": nome, "idade": idade, "status": status})

    print("\nUtilizadores registados:")
    for u in utilizadores:
        print(f"{u['nome']} tem {u['idade']} anos e é {u['status']}.")

if __name__ == "__main__":
    main()
