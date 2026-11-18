from lib.interface import *
from lib.arquivo import *

def main():
    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_estudante()

        elif opcao == "2":
            cadastrar_disciplina()

        elif opcao == "3":
            listar_disciplinas()

        elif opcao == "4":
            cadastrar_notas()

        elif opcao == "5":
            ficha_estudante()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")


main()