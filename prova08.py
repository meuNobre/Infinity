import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.padding = 20

    tarefas = ft.Column()

    campo_tarefa = ft.TextField(
        label="Nova tarefa",
        width=300
    )

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() == "":
            return  # evitarra tarefa vazia

        tarefas.controls.append(
            ft.Text(campo_tarefa.value)
        )
        campo_tarefa.value = ""
        page.update()

    botao_adicionar = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_tarefa
    )

    page.add(
        campo_tarefa,
        botao_adicionar,
        tarefas
    )

ft.app(target=main)
