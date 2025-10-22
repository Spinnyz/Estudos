"""O programa mostra um menu com opções:

1️⃣ Adicionar tarefa

2️⃣ Ver tarefas

3️⃣ Remover tarefa

4️⃣ Sair

As tarefas ficam salvas numa lista.

O usuário pode adicionar e remover até sair do programa."""


def mostrar_menu():
    print ("""
    [1] Adicionar tarefa
    [2] Ver tarefas
    [3] Remover tarefa
    [4] Sair
""")
    
def tarefa_adicionar(tarefas):
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def remover_tarefa(tarefas):
    if  not  tarefas:
        print("Não há tarefas para remover.")
        return
    else:
        remover = inpur ("Qual tarefa quer remover?")