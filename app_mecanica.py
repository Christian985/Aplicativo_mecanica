import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
import requests
from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Mecânica"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    # Consome e mostra o JSON no app
    # Pega informações dos Clientes
    def get_info_cliente():
        url = f"http://10.135.232.27:5001/clientes"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Clientes:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Pega informações dos Veículos
    def get_info_veiculo():
        url = f"http://10.135.232.27:5001/veiculos"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Veículos:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Pega informações das Ordens
    def get_info_ordem():
        url = f"http://10.135.232.27:5001/ordem"

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

        # chamar a função para pegar o JSON
        dados = get_info_veiculo()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in dados:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_veiculo.controls.clear()
            for veiculo in dados:
                lv_veiculo.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(f"Cliente Associado - {input_cliente_associado.value}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.MORE_VERT,
                            items=[
                                ft.PopupMenuItem(text=f"Modelo - {input_modelo.value}"),
                                ft.PopupMenuItem(text=f"Placa: - {input_placa.value}"),
                                ft.PopupMenuItem(text=f"Ano de Fabricação - {input_ano_fabricacao.value}"),
                                ft.PopupMenuItem(text=f"Modelo - {input_modelo.value}"),
                                ft.PopupMenuItem(text=f"Marca: - {input_marca.value}"),
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

        # chamar a função para pegar o JSON
        dados = get_info_cliente()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in dados:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_cliente.controls.clear()
            for cliente in dados['lista_de_clientes']:
                lv_cliente.controls.append(
                    ft.Text(f'Nome: {cliente["nome"]}'),
                )
                lv_cliente.controls.append(
                    ft.Text(f'Cpf: {cliente["cpf"]}'),
                )
                lv_cliente.controls.append(
                    ft.Text(f'Email: {cliente["email"]}'),
                )
                lv_cliente.controls.append(
                    ft.Text(f'Telefone: {cliente["telefone"]}'),
                )
                lv_cliente.controls.append(
                    ft.Text(f'Endereço: {cliente["endereco"]}'),
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
        dados = get_info_ordem()

        progress.visible = False
        page.update()

        # Verificar se a API retornou erro
        if "erro" in dados:
            page.overlay.append(msg_erro)
            msg_erro.open = True
        else:
            lv_ordem.controls.clear()
            for ordem in dados["lista_de_ordens"]:
                lv_ordem.controls.append(
                    ft.Text(f'Veículo Associado: {ordem["veiculo_associado"]}'),
                )

                lv_ordem.controls.append(
                    ft.Text(f'Data de Abertura: {ordem["data_abertura"]}'),
                )

                lv_ordem.controls.append(
                    ft.Text(f'Descrição do Serviço: {ordem["descricao_servico"]}'),
                )

                lv_ordem.controls.append(
                    ft.Text(f'Status: {ordem["status"]}'),
                )

                lv_ordem.controls.append(
                    ft.Text(f'Valor Estimado: {ordem["valor_estimado"]}'),
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
                    ),
                    ft.Button(
                        text="Cadastrar Clientes",
                        on_click=lambda _: page.go("/cadastro_clientes"),
                        bgcolor=Colors.PURPLE_900,

                    ),
                    ft.Button(
                        text="Cadastrar Ordens",
                        on_click=lambda _: page.go("/cadastro_ordens"),
                        bgcolor=Colors.PURPLE_900,
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
                            on_click=lambda _: mostrar_veiculos(e),
                            bgcolor=Colors.PURPLE_900,
                        ),
                        # Irá mostrar os Dados
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_veiculos"),
                            bgcolor=Colors.PURPLE_900,
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
                            on_click=lambda _: mostrar_clientes(e),
                            bgcolor=Colors.PURPLE_900,
                        ),
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_clientes"),
                            bgcolor=Colors.PURPLE_900,
                        )
                    ]
                )
            )
        # Lista de Clientes
        if page.route == "/lista_clientes":
            mostrar_clientes(e)
            page.views.append(
                View(
                    "/Lista_clientes",
                    [
                        AppBar(title=Text("Lista de Clientes"), bgcolor=Colors.PURPLE_900),
                        lv_cliente,
                        ft.Button(
                            text="Voltar",
                            on_click=lambda _: page.go("/"),
                            bgcolor=Colors.PURPLE_900,
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
                            on_click=lambda _: mostrar_ordens(e),
                            bgcolor=Colors.PURPLE_900,
                        ),
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_ordens"),
                            bgcolor=Colors.PURPLE_900,
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
    input_cliente_associado = ft.TextField(label="Cliente Associado", bgcolor=Colors.DEEP_PURPLE)
    input_modelo = ft.TextField(label="Modelo", bgcolor=Colors.DEEP_PURPLE)
    input_placa = ft.TextField(label="Placa", bgcolor=Colors.DEEP_PURPLE)
    input_ano_fabricacao = ft.TextField(label="Ano de Fabricacao", bgcolor=Colors.DEEP_PURPLE)
    input_marca = ft.TextField(label="Marca", bgcolor=Colors.DEEP_PURPLE)

    # CLIENTES
    input_nome = ft.TextField(label="Nome", bgcolor=Colors.DEEP_PURPLE)
    input_cpf = ft.TextField(label="CPF", bgcolor=Colors.DEEP_PURPLE)
    input_telefone = ft.TextField(label="Telefone", bgcolor=Colors.DEEP_PURPLE)
    input_endereco = ft.TextField(label="Endereço", bgcolor=Colors.DEEP_PURPLE)
    input_email = ft.TextField(label="E-mail", bgcolor=Colors.DEEP_PURPLE)

    # ORDENS
    input_veiculo_associado = ft.TextField(label="Veículo Associado", bgcolor=Colors.DEEP_PURPLE)
    input_data_abertura = ft.TextField(label="Data abertura", bgcolor=Colors.DEEP_PURPLE)
    input_descricao_servico = ft.TextField(label="Descrição de Serviço", bgcolor=Colors.DEEP_PURPLE)
    input_status = ft.TextField(label="Status", hint_text="Ex: Em andamento", bgcolor=Colors.DEEP_PURPLE)
    input_valor_estimado = ft.TextField(label="Valor Estimado", hint_text="$", bgcolor=Colors.DEEP_PURPLE)

    lv_veiculo = ft.ListView(
        height=500

    )

    lv_cliente = ft.ListView(
        height=500

    )

    lv_ordem = ft.ListView(
        height=500

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
