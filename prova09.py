import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.padding = 20

    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    mensagem = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=3,
        max_lines=5,
        width=300
    )

    confirmacao = ft.Text("", color="green")

    def enviar_formulario(e):
        if not nome.value or not email.value or not mensagem.value:
            confirmacao.value = "Preencha todos os campos."
            confirmacao.color = "red"
        else:
            # processamento simples (escopo da atividade)
            confirmacao.value = "Formulário enviado com sucesso!"
            confirmacao.color = "green"

            nome.value = ""
            email.value = ""
            mensagem.value = ""

        page.update()

    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        on_click=enviar_formulario
    )

    page.add(
        nome,
        email,
        mensagem,
        botao_enviar,
        confirmacao
    )

ft.app(target=main)
