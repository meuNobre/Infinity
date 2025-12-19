import flet as ft
from datetime import datetime

# ============================
# CLASSES POO
# ============================

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    def exibir_informacoes(self):
        return f"Nome: {self.__nome}\nTelefone: {self.__telefone}\nEmail: {self.__email}"


class Cliente(Pessoa):
    _id_contador = 1

    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.__id = Cliente._id_contador
        Cliente._id_contador += 1

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

    def numero(self):
        return self.__numero

    def tipo(self):
        return self.__tipo

    def preco(self):
        return self.__preco

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

    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor
        if valor != "Ativa":
            self.__quarto.disponivel = True

    def cliente(self):
        return self.__cliente

    def quarto(self):
        return self.__quarto

    def check_in(self):
        return self.__check_in

    def check_out(self):
        return self.__check_out

    def exibir_reserva(self):
        return f"Cliente: {self.__cliente.nome} | Quarto: {self.__quarto.numero} | {self.__check_in} → {self.__check_out} | Status: {self.__status}"


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

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

    def buscar_cliente_por_id(self, id_cliente):
        for c in self.clientes:
            if c.id == id_cliente:
                return c
        return None

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def buscar_quarto_por_numero(self, numero):
        for q in self.quartos:
            if q.numero == numero:
                return q
        return None

    def verificar_disponibilidade(self):
        return [q for q in self.quartos if q.disponivel]

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, check_in, check_out)
            self.reservas.append(reserva)
            return reserva
        else:
            return None

    def cancelar_reserva(self, reserva):
        reserva.status = "Cancelada"



#FLET
def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Sistema de Reservas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    gm = GerenciadorDeReservas()

    # Dados iniciais
    gm.adicionar_quarto(Quarto(101, "Single", 150))
    gm.adicionar_quarto(Quarto(102, "Double", 250))
    gm.adicionar_quarto(Quarto(201, "Suite", 500))
    gm.adicionar_quarto(Quarto(202, "Suite Deluxe", 750))

    
    # ABA 1: QUARTOS
    
    
    lista_quartos_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=400)

    def atualizar_quartos():
        lista_quartos_view.controls.clear()
        for q in gm.quartos:
            cor = "green100" if q.disponivel else "red100"
            lista_quartos_view.controls.append(
                ft.Container(
                    content=ft.Text(q.exibir_info(), size=16),
                    bgcolor=cor,
                    padding=15,
                    border_radius=10
                )
            )
        page.update()

    aba_quartos = ft.Column([
        ft.Text("📋 Lista de Quartos Disponíveis", size=24, weight="bold"),
        ft.Divider(),
        lista_quartos_view,
        ft.ElevatedButton(
            "🔄 Atualizar Lista",
            on_click=lambda e: atualizar_quartos()
        )
    ])

    
    # ABA 2: CLIENTES
    
    
    lista_clientes_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=300)
    
    nome_cliente_input = ft.TextField(label="Nome Completo", width=300)
    telefone_cliente_input = ft.TextField(label="Telefone", width=300)
    email_cliente_input = ft.TextField(label="Email", width=300)
    
    msg_cliente = ft.Text(value="", color="green", size=14)

    def adicionar_cliente(e):
        if not nome_cliente_input.value or not telefone_cliente_input.value or not email_cliente_input.value:
            msg_cliente.value = "❌ Preencha todos os campos!"
            msg_cliente.color = "red"
            page.update()
            return
        
        cliente = Cliente(nome_cliente_input.value, telefone_cliente_input.value, email_cliente_input.value)
        gm.adicionar_cliente(cliente)
        msg_cliente.value = f"✅ Cliente {cliente.nome} adicionado com ID: {cliente.id}"
        msg_cliente.color = "green"
        nome_cliente_input.value = ""
        telefone_cliente_input.value = ""
        email_cliente_input.value = ""
        atualizar_clientes()
        page.update()

    def atualizar_clientes():
        lista_clientes_view.controls.clear()
        for c in gm.clientes:
            lista_clientes_view.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"ID: {c.id}", weight="bold", color="blue"),
                        ft.Text(c.exibir_informacoes())
                    ]),
                    bgcolor="blue50",
                    padding=15,
                    border_radius=10
                )
            )
        page.update()

    aba_clientes = ft.Column([
        ft.Text("👥 Gerenciar Clientes", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Adicionar Novo Cliente", size=18, weight="bold"),
        nome_cliente_input,
        telefone_cliente_input,
        email_cliente_input,
        ft.ElevatedButton("➕ Adicionar Cliente", on_click=adicionar_cliente),
        msg_cliente,
        ft.Divider(),
        ft.Text("Lista de Clientes Cadastrados", size=18, weight="bold"),
        lista_clientes_view,
        ft.ElevatedButton("🔄 Atualizar Lista", on_click=lambda e: atualizar_clientes())
    ], scroll=ft.ScrollMode.AUTO)

    
    # ABA 3: RESERVAS
    
    
    lista_reservas_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=250)
    
    id_cliente_reserva = ft.TextField(label="ID do Cliente", width=150)
    numero_quarto_reserva = ft.TextField(label="Número do Quarto", width=150)
    checkin_reserva = ft.TextField(label="Check-in (AAAA-MM-DD)", width=200, value="2025-01-10")
    checkout_reserva = ft.TextField(label="Check-out (AAAA-MM-DD)", width=200, value="2025-01-15")
    
    msg_reserva = ft.Text(value="", size=14)

    def criar_reserva_handler(e):
        try:
            id_cliente = int(id_cliente_reserva.value)
            numero_quarto = int(numero_quarto_reserva.value)
            
            cliente = gm.buscar_cliente_por_id(id_cliente)
            quarto = gm.buscar_quarto_por_numero(numero_quarto)
            
            if not cliente:
                msg_reserva.value = f"❌ Cliente com ID {id_cliente} não encontrado!"
                msg_reserva.color = "red"
                page.update()
                return
            
            if not quarto:
                msg_reserva.value = f"❌ Quarto {numero_quarto} não encontrado!"
                msg_reserva.color = "red"
                page.update()
                return
            
            reserva = gm.criar_reserva(cliente, quarto, checkin_reserva.value, checkout_reserva.value)
            
            if reserva:
                msg_reserva.value = f"✅ Reserva criada! Cliente: {cliente.nome}, Quarto: {quarto.numero}"
                msg_reserva.color = "green"
                id_cliente_reserva.value = ""
                numero_quarto_reserva.value = ""
            else:
                msg_reserva.value = f"❌ Quarto {numero_quarto} não está disponível!"
                msg_reserva.color = "red"
            
            atualizar_quartos()
            atualizar_reservas()
            
        except ValueError:
            msg_reserva.value = "❌ Digite números válidos para ID e Quarto!"
            msg_reserva.color = "red"
        except Exception as ex:
            msg_reserva.value = f"❌ Erro: {str(ex)}"
            msg_reserva.color = "red"
        
        page.update()

    def cancelar_reserva_handler(reserva):
        gm.cancelar_reserva(reserva)
        msg_reserva.value = f"✅ Reserva do cliente {reserva.cliente.nome} cancelada!"
        msg_reserva.color = "orange"
        atualizar_quartos()
        atualizar_reservas()
        page.update()

    def atualizar_reservas():
        lista_reservas_view.controls.clear()
        if not gm.reservas:
            lista_reservas_view.controls.append(
                ft.Text("Nenhuma reserva cadastrada ainda.", italic=True, color="grey")
            )
        else:
            for r in gm.reservas:
                cor = "green100" if r.status == "Ativa" else "orange100"
                btn_cancelar = ft.ElevatedButton(
                    "🗑️ Cancelar",
                    on_click=lambda e, reserva=r: cancelar_reserva_handler(reserva),
                    disabled=(r.status != "Ativa"),
                    bgcolor="red400" if r.status == "Ativa" else "grey",
                    color="white"
                )
                lista_reservas_view.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text(r.exibir_reserva(), size=14)
                            ], expand=True),
                            btn_cancelar
                        ]),
                        bgcolor=cor,
                        padding=15,
                        border_radius=10
                    )
                )
        page.update()

    aba_reservas = ft.Column([
        ft.Text("🏨 Gerenciar Reservas", size=24, weight="bold"),
        ft.Divider(),
        ft.Text("Criar Nova Reserva", size=18, weight="bold"),
        ft.Row([id_cliente_reserva, numero_quarto_reserva], spacing=10),
        ft.Row([checkin_reserva, checkout_reserva], spacing=10),
        ft.ElevatedButton("➕ Criar Reserva", on_click=criar_reserva_handler),
        msg_reserva,
        ft.Divider(),
        ft.Text("Lista de Reservas", size=18, weight="bold"),
        lista_reservas_view,
        ft.ElevatedButton("🔄 Atualizar Lista", on_click=lambda e: atualizar_reservas())
    ], scroll=ft.ScrollMode.AUTO)


    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="🏨 Quartos", content=aba_quartos),
            ft.Tab(text="👥 Clientes", content=aba_clientes),
            ft.Tab(text="📅 Reservas", content=aba_reservas),
        ],
        expand=1,
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("🏨 Refúgio dos Sonhos", size=32, weight="bold", color="blue"),
                ft.Text("Sistema de Gerenciamento de Reservas", size=16, italic=True, color="grey700"),
                ft.Divider(),
                tabs
            ]),
            padding=20
        )
    )

    # Inicniar listas
    atualizar_quartos()
    atualizar_clientes()
    atualizar_reservas()

ft.app(target=main)