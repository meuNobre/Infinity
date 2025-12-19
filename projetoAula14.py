    import flet as ft
    from datetime import date

    # ============================
    # CLASSES POO
    # ============================

    class Pessoa:
        def __init__(self, nome, telefone, email):
            self.__nome = nome
            self.__telefone = telefone
            self.__email = email

        # Encapsulamento
        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, valor):
            self.__nome = valor

        @property
        def telefone(self):
            return self.__telefone

        @telefone.setter
        def telefone(self, valor):
            self.__telefone = valor

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, valor):
            self.__email = valor

        # Polimorfismo
        def exibir_informacoes(self):
            return f"Nome: {self.__nome}\nTelefone: {self.__telefone}\nEmail: {self.__email}"


    class Cliente(Pessoa):
        _id_contador = 1

        def __init__(self, nome, telefone, email):
            super().__init__(nome, telefone, email)
            self.__id = Cliente._id_contador
            Cliente._id_contador += 1

        @property
        def id(self):
            return self.__id

        def exibir_informacoes(self):
            info = super().exibir_informacoes()
            info += f"\nID Cliente: {self.__id}"
            return info


    class Quarto:
        def __init__(self, numero, tipo, preco):
            self.__numero = numero
            self.__tipo = tipo
            self.__preco = preco
            self.__disponivel = True

        @property
        def numero(self):
            return self.__numero

        @property
        def tipo(self):
            return self.__tipo

        @property
        def preco(self):
            return self.__preco

        @property
        def disponivel(self):
            return self.__disponivel

        @disponivel.setter
        def disponivel(self, valor):
            self.__disponivel = valor

        def exibir_info(self):
            status = "Disponível" if self.__disponivel else "Ocupado"
            return f"Quarto {self.__numero} ({self.__tipo}) - R$ {self.__preco:.2f} - {status}"


    class Reserva:
        def __init__(self, cliente, quarto, check_in, check_out):
            self.__cliente = cliente
            self.__quarto = quarto
            self.__check_in = check_in
            self.__check_out = check_out
            self.__status = "Ativa"
            quarto.disponivel = False

        @property
        def status(self):
            return self.__status

        @status.setter
        def status(self, valor):
            self.__status = valor
            if valor != "Ativa":
                self.__quarto.disponivel = True

        @property
        def cliente(self):
            return self.__cliente

        @property
        def quarto(self):
            return self.__quarto

        def exibir_reserva(self):
            return f"Cliente: {self.__cliente.nome} | Quarto: {self.__quarto.numero} | {self.__check_in} -> {self.__check_out} | Status: {self.__status}"


    class GerenciadorDeReservas:
        def __init__(self):
            self.clientes = []
            self.quartos = []
            self.reservas = []

        # Clientes
        def adicionar_cliente(self, cliente):
            self.clientes.append(cliente)

        def editar_cliente(self, id_cliente, nome=None, telefone=None, email=None):
            for c in self.clientes:
                if c.id == id_cliente:
                    if nome:
                        c.nome = nome
                    if telefone:
                        c.telefone = telefone
                    if email:
                        c.email = email
                    return c
            return None

        # Quartos
        def adicionar_quarto(self, quarto):
            self.quartos.append(quarto)

        def verificar_disponibilidade(self):
            return [q for q in self.quartos if q.disponivel]

        # Reservas
        def criar_reserva(self, cliente, quarto, check_in, check_out):
            if quarto.disponivel:
                reserva = Reserva(cliente, quarto, check_in, check_out)
                self.reservas.append(reserva)
                return reserva
            else:
                return None

        def cancelar_reserva(self, reserva):
            reserva.status = "Cancelada"

    # ============================
    # INTERFACE FLET COMPLETA
    # ============================

    def main(page: ft.Page):
        page.title = "Refúgio dos Sonhos - Sistema de Reservas"
        page.vertical_alignment = ft.MainAxisAlignment.START
        gm = GerenciadorDeReservas()

        # Dados iniciais
        gm.adicionar_quarto(Quarto(101, "Single", 150))
        gm.adicionar_quarto(Quarto(102, "Double", 250))
        gm.adicionar_quarto(Quarto(201, "Suite", 500))

        mensagem = ft.Text(value="Bem-vindo!", color="green")

        # ListViews
        lista_quartos = ft.ListView(expand=True, spacing=5, padding=10)
        lista_reservas = ft.ListView(expand=True, spacing=5, padding=10)
        lista_clientes = ft.ListView(expand=True, spacing=5, padding=10)

        # --- Atualizações ---
        def atualizar_quartos():
            lista_quartos.controls.clear()
            for q in gm.quartos:
                lista_quartos.controls.append(ft.Text(q.exibir_info()))
            page.update()

        def atualizar_reservas():
            lista_reservas.controls.clear()
            for r in gm.reservas:
                btn_cancelar = ft.ElevatedButton(
                    text="Cancelar",
                    on_click=lambda e, r=r: cancelar_reserva(r)
                )
                lista_reservas.controls.append(
                    ft.Row([ft.Text(r.exibir_reserva()), btn_cancelar], spacing=10)
                )
            page.update()

        def atualizar_clientes():
            lista_clientes.controls.clear()
            for c in gm.clientes:
                btn_editar = ft.ElevatedButton(
                    text="Editar",
                    on_click=lambda e, c=c: abrir_edicao_cliente(c)
                )
                lista_clientes.controls.append(ft.Row([ft.Text(c.exibir_informacoes()), btn_editar], spacing=10))
            page.update()

        # --- Funções ---
        def adicionar_cliente(e):
            cliente = Cliente(nome_input.value, telefone_input.value, email_input.value)
            gm.adicionar_cliente(cliente)
            mensagem.value = f"Cliente {cliente.nome} adicionado!"
            nome_input.value = telefone_input.value = email_input.value = ""
            atualizar_clientes()
            page.update()

        def criar_reserva(e):
            try:
                cliente = gm.clientes[int(cliente_input.value)-1]
                quarto = gm.quartos[int(quarto_input.value)-1]
                reserva = gm.criar_reserva(cliente, quarto, checkin_input.value, checkout_input.value)
                if reserva:
                    mensagem.value = "Reserva criada com sucesso!"
                else:
                    mensagem.value = "Quarto não disponível."
                atualizar_quartos()
                atualizar_reservas()
            except:
                mensagem.value = "Erro ao criar reserva. Verifique os dados."
            page.update()

        def cancelar_reserva(reserva):
            gm.cancelar_reserva(reserva)
            mensagem.value = "Reserva cancelada!"
            atualizar_quartos()
            atualizar_reservas()
            page.update()

        # --- Edição de clientes ---
        def abrir_edicao_cliente(cliente):
            nome_edit.value = cliente.nome
            telefone_edit.value = cliente.telefone
            email_edit.value = cliente.email
            id_edit.value = str(cliente.id)  # precisa ser string para TextField
            page.update()


        def salvar_edicao(e):
            try:
                id_cliente = int(id_edit.value)  # garante que seja número
                gm.editar_cliente(
                    id_cliente,
                    nome=nome_edit.value,
                    telefone=telefone_edit.value,
                    email=email_edit.value
                )
                mensagem.value = f"Cliente {nome_edit.value} editado com sucesso!"
                atualizar_clientes()
                page.update()
            except Exception as ex:
                mensagem.value = f"Erro ao editar cliente: {ex}"
                page.update()

        # --- Inputs ---
        nome_input = ft.TextField(label="Nome", width=300)
        telefone_input = ft.TextField(label="Telefone", width=300)
        email_input = ft.TextField(label="Email", width=300)
        cliente_input = ft.TextField(label="ID Cliente", width=100)
        quarto_input = ft.TextField(label="Número do quarto (índice)", width=100)
        checkin_input = ft.TextField(label="Check-in (AAAA-MM-DD)", width=150)
        checkout_input = ft.TextField(label="Check-out (AAAA-MM-DD)", width=150)

        # Edição
        id_edit = ft.TextField(label="ID Cliente", disabled=True, width=100)
        nome_edit = ft.TextField(label="Nome", width=300)
        telefone_edit = ft.TextField(label="Telefone", width=300)
        email_edit = ft.TextField(label="Email", width=300)
        btn_salvar_edicao = ft.ElevatedButton("Salvar Edição", on_click=salvar_edicao)

        # --- Botões ---
        btn_add_cliente = ft.ElevatedButton("Adicionar Cliente", on_click=adicionar_cliente)
        btn_criar_reserva = ft.ElevatedButton("Criar Reserva", on_click=criar_reserva)
        btn_atualizar_quartos = ft.ElevatedButton("Atualizar Quartos", on_click=lambda e: atualizar_quartos())
        btn_atualizar_clientes = ft.ElevatedButton("Atualizar Clientes", on_click=lambda e: atualizar_clientes())
        btn_atualizar_reservas = ft.ElevatedButton("Atualizar Reservas", on_click=lambda e: atualizar_reservas())

        # --- Layout ---
        page.add(
            ft.Text("Lista de Quartos", size=20, weight="bold"),
            lista_quartos,
            btn_atualizar_quartos,
            ft.Divider(),
            ft.Text("Lista de Clientes", size=20, weight="bold"),
            lista_clientes,
            btn_atualizar_clientes,
            ft.Divider(),
            ft.Text("Adicionar Cliente", size=20, weight="bold"),
            nome_input, telefone_input, email_input,
            btn_add_cliente,
            ft.Divider(),
            ft.Text("Editar Cliente", size=20, weight="bold"),
            id_edit, nome_edit, telefone_edit, email_edit,
            btn_salvar_edicao,
            ft.Divider(),
            ft.Text("Lista de Reservas", size=20, weight="bold"),
            lista_reservas,
            btn_atualizar_reservas,
            ft.Divider(),
            ft.Text("Criar Reserva", size=20, weight="bold"),
            ft.Row([cliente_input, quarto_input, checkin_input, checkout_input], spacing=10),
            btn_criar_reserva,
            ft.Divider(),
            mensagem
        )

        atualizar_quartos()
        atualizar_clientes()
        atualizar_reservas()


    ft.app(target=main)
