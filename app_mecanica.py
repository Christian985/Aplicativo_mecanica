import flet as ft
from flet import AppBar, Text, View
from flet.core.alignment import center_left
from flet.core.colors import Colors
import requests
from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Mecânica"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.WHITE
    page.window.width = 375
    page.window.height = 667

    # Funções
    # Consome e mostra o JSON no app
    # Pega informações dos Clientes
    def get_info_cliente():
        url = f"http://10.135.235.34:5001/clientes"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Clientes:", resposta.json())
            return resposta.json()
        else:
            return {"erro": resposta.json()}

    def post_nova_ordem():
        url = f"http://10.135.235.34:5001/ordems"
        dados = {
            "veiculo_associado": str(),
            "data_abertura": str(),
            "descricao_servico": str(),
            "status": str(),
            "valor_estimado": str()
        }

    def post_novo_cliente():
        url = f"http://10.135.235.34:5001/clientes"
        dados = {
            "nome": str(),
            "cpf": str(),
            "telefone": str(),
            "endereco": str(),
            "email": str(),
        }

    def post_novo_veiculo():
        url = f"http://10.135.235.34:5001/veiculos"
        dados = {
            "cliente_associado": str(),
            "modelo": str(),
            "placa": str(),
            "ano_fabricacao": str(),
            "marca": str(),
        }

    # Salva as informações das Ordens
    def salvar_ordem(e):
        # Caso eles não possuam valores
        if input_veiculo_associado.value == "" or input_data_abertura.value == "" or input_descricao_servico.value == "" or input_status.value == "" or input_valor_estimado.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_ordem = Ordem(
                veiculo_associado=input_veiculo_associado.value,
                data_abertura=input_data_abertura.value,
                descricao_servico=input_descricao_servico.value,
                status=input_status.value,
                valor_estimado=input_valor_estimado.value,

            )
            # Adiciona o Valor de veiculo_associado, data_abertura, descricao_servico, status e valor_estimado na Lista
            input_veiculo_associado.value = ""
            input_data_abertura.value = ""
            input_descricao_servico.value = ""
            input_status.value = ""
            input_valor_estimado.value = ""

            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # Pega informações dos Veículos
    def get_info_veiculo():
        url = f"http://10.135.235.34:5001/veiculos"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Veículos:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Pega informações das Ordens
    def get_info_ordem():
        url = f"http://10.135.235.34:5001/ordem"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Ordens:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Mostrar Veículos
    def mostrar_veiculos(e):
        progress.visible = True
        page.update()

        # Chamar a função para pegar o JSON
        veiculos = get_info_veiculo()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in veiculos:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_veiculo.controls.clear()
            for veiculo in veiculos:
                lv_veiculo.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(f"Veículo - {veiculo["modelo"]}"),
                        subtitle=ft.Text(f"cliente - {veiculo["cliente_associado"]}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text=f"Placa - {veiculo["placa"]}"),
                                ft.PopupMenuItem(text=f"Ano de Fabricação - {veiculo["ano_fabricacao"]}"),
                                ft.PopupMenuItem(text=f"Marca - {veiculo["marca"]}"),
                            ]
                        )
                    )
                )
            msg_sucesso.content = ft.Text("Entrada Válida")
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

        page.update()

    # Mostrar Clientes
    def mostrar_clientes(e):
        progress.visible = True
        page.update()

        # Chamar a função para pegar o JSON
        clientes = get_info_cliente()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in clientes:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_cliente.controls.clear()
            for cliente in clientes["clientes"]:
                lv_cliente.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(f"Cliente - {cliente["nome"]}"),
                        subtitle=ft.Text(f"CPF - {cliente["cpf"]}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text=f"Email - {cliente["email"]}"),
                                ft.PopupMenuItem(text=f"Telefone - {cliente["telefone"]}"),
                                ft.PopupMenuItem(text=f"Endereço - {cliente["endereco"]}"),
                            ]
                        )
                    )
                )
            msg_sucesso.content = ft.Text("Entrada Válida")
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

        page.update()

    # Mostrar Ordens
    def mostrar_ordens(e):
        progress.visible = True
        page.update()

        # chamar a função para pegar o JSON
        ordens = get_info_ordem()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in ordens:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_ordem.controls.clear()
            for ordem in ordens:
                lv_ordem.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(f"Ordem/Veículo - {ordem["veiculo_associado"]}"),
                        subtitle=ft.Text(f"Data de Abertura - {ordem["data_abertura"]}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text=f"Descrição do Serviço - {ordem["descricao_servico"]}"),
                                ft.PopupMenuItem(text=f"Status - {ordem["status"]}"),
                                ft.PopupMenuItem(text=f"Valor Estimado - {ordem["valor_estimado"]}"),
                            ]
                        )
                    )
                )
            msg_sucesso.content = ft.Text("Entrada Válida")
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

        page.update()

    # Gerencia o caminho das Rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(  # Início
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PURPLE_900),
                    ft.Button(
                        text="Cadastrar Veículos",
                        on_click=lambda _: page.go("/cadastro_veiculos"),
                        bgcolor=Colors.PURPLE_900,
                        height=50,
                        width=340,
                    ),
                    ft.Button(
                        text="Cadastrar Clientes",
                        on_click=lambda _: page.go("/cadastro_clientes"),
                        bgcolor=Colors.PURPLE_900,
                        height=50,
                        width=340,
                    ),
                    ft.Button(
                        text="Cadastrar Ordens",
                        on_click=lambda _: page.go("/cadastro_ordens"),
                        bgcolor=Colors.PURPLE_900,
                        height=50,
                        width=340,
                    )
                ],
                bgcolor=Colors.GREY_900,
            )
        )
        # Cadastro de veículos
        if page.route == "/cadastro_veiculos" or page.route == "/lista_veiculos":
            page.views.append(
                View(
                    "/cadastro_veiculos",
                    [
                        AppBar(title=Text("Cadastro de Veículos"), bgcolor=Colors.PURPLE_900),
                        input_cliente_associado,
                        input_modelo,
                        input_placa,
                        input_ano_fabricacao,
                        input_marca,
                        # Irá salvar os Dados
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: post,
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        ),
                        # Irá mostrar os Dados
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_veiculos"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        ),
                        ft.Column(
                            [
                                progress
                            ],
                            width=page.window.width,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        )
                    ],
                )
            )
        # Lista de Veículos
        if page.route == "/lista_veiculos":
            mostrar_veiculos(e)
            page.views.append(
                View(
                    "/Lista_veiculos",
                    [
                        AppBar(title=Text("Lista de Veículos"), bgcolor=Colors.PURPLE_900),
                        lv_veiculo,
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        )
                    ],
                )
            )
        # Cadastro de Clientes
        if page.route == "/cadastro_clientes" or page.route == "/lista_clientes":
            page.views.append(
                View(
                    "/cadastro_clientes",
                    [
                        AppBar(title=Text("Cadastro de Clientes"), bgcolor=Colors.PURPLE_900),
                        input_nome,
                        input_cpf,
                        input_telefone,
                        input_endereco,
                        input_email,
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: get_info_cliente,
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        ),
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_clientes"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        )
                    ]
                )
            )
        # Lista de Clientes
        if page.route == "/lista_clientes":
            mostrar_clientes(e)
            page.views.append(
                View(
                    "/lista_clientes",
                    [
                        AppBar(title=Text("Lista de Clientes"), bgcolor=Colors.PURPLE_900),
                        lv_cliente,
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        )
                    ],
                )
            )
        # Cadastro de Ordens
        if page.route == "/cadastro_ordens" or page.route == "/lista_ordens":
            page.views.append(
                View(
                    "/cadastro_ordens",
                    [
                        AppBar(title=Text("Cadastro de Ordens"), bgcolor=Colors.PURPLE_900),
                        input_veiculo_associado,
                        input_data_abertura,
                        input_descricao_servico,
                        input_status,
                        input_valor_estimado,
                        ft.Button(
                            text="Salvar",
                            on_click=lambda _: get_info_ordem,
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        ),
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_ordens"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        )
                    ]
                )
            )
        # Lista de Ordens
        if page.route == "/lista_ordens":
            mostrar_ordens(e)
            page.views.append(
                View(
                    "/Lista_ordens",
                    [
                        AppBar(title=Text("Lista de Ordens"), bgcolor=Colors.PURPLE_900),
                        lv_ordem,
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                            bgcolor=Colors.PURPLE_900,
                            height=50,
                            width=340,
                        )
                    ],
                )
            )
        page.update()

        # FIM da Transição de Páginas

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    # Mostra que está carregando
    progress = ft.ProgressRing(visible=False)

    msg_sucesso = ft.SnackBar(
        content=ft.Text("SALVOU"),
        bgcolor=Colors.GREEN
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("ERRO"),
        bgcolor=Colors.RED
    )
    # VEÍCULOS
    input_cliente_associado = ft.TextField(label="Cliente Associado", bgcolor=Colors.PURPLE_900)
    input_modelo = ft.TextField(label="Modelo", bgcolor=Colors.PURPLE_900)
    input_placa = ft.TextField(label="Placa", bgcolor=Colors.PURPLE_900)
    input_ano_fabricacao = ft.TextField(label="Ano de Fabricacao", bgcolor=Colors.PURPLE_900)
    input_marca = ft.TextField(label="Marca", bgcolor=Colors.PURPLE_900)

    # CLIENTES
    input_nome = ft.TextField(label="Nome", bgcolor=Colors.PURPLE_900)
    input_cpf = ft.TextField(label="CPF", bgcolor=Colors.PURPLE_900)
    input_telefone = ft.TextField(label="Telefone", bgcolor=Colors.PURPLE_900)
    input_endereco = ft.TextField(label="Endereço", bgcolor=Colors.PURPLE_900)
    input_email = ft.TextField(label="E-mail", bgcolor=Colors.PURPLE_900)

    # ORDENS
    input_veiculo_associado = ft.TextField(label="Veículo Associado", bgcolor=Colors.PURPLE_900)
    input_data_abertura = ft.TextField(label="Data abertura", bgcolor=Colors.PURPLE_900)
    input_descricao_servico = ft.TextField(label="Descrição de Serviço", bgcolor=Colors.PURPLE_900)
    input_status = ft.TextField(label="Status", hint_text="Ex: Em andamento", bgcolor=Colors.PURPLE_900)
    input_valor_estimado = ft.TextField(label="Valor Estimado", hint_text="$", bgcolor=Colors.PURPLE_900)

    lv_veiculo = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1,
    )

    lv_cliente = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1

    )

    lv_ordem = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1

    )
    # FIM dos Componentes

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)
    # FIM dos Eventos


# Comando que executa o Aplicativo
# Deve estar sempre colado na linha
ft.app(main)
