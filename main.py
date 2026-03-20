import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError: # Caso o arquivo esteja corrompido ou vazio
            return []
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(titulo):
    tarefas = carregar_tarefas()
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print(f"\n✅ Tarefa '{titulo}' adicionada!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    print("\n--- SUAS TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False # Retorna False para ajudar na lógica do menu
    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✖"
        print(f"{i + 1}. [{status}] {t['titulo']}")
    return True

def concluir_tarefa(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("\n⭐ Tarefa concluída com sucesso!")
    else:
        print("\n⚠ Número de tarefa inválido.")

def menu():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            adicionar_tarefa(titulo)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            if listar_tarefas(): # Só pede o número se houver tarefas
                try:
                    indice = int(input("Digite o número da tarefa para concluir: ")) - 1
                    concluir_tarefa(indice)
                except ValueError:
                    print("\n⚠ Por favor, digite um número válido.")
        elif opcao == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("\n⚠ Opção inválida.")

if __name__ == "__main__":
    menu()
