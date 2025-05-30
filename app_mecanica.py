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
    # Pega informações dos Clientes
    def get_info_cliente(cliente):
        url = f"http://10.135.232.27:5001/clientes"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Clientes:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Consome e mostra o JSON no app
    def mostrar():
        progress.visible = True
        page.update()
        if input_cep.value == "":
            msg_error.content = ft.Text("CEP Invalido")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:

            # chamar a função para pegar o JSON
            dados = get_info(int(input_cep.value))

            progress.visible = False
            page.update()

    # Pega informações dos Veículos
    def get_info_veiculo(veiculo):
        url = f"http://10.135.232.27:5001/veiculos"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Veículos:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Pega informações das Ordens
    def get_info_ordem(ordem):
        url = f"http://10.135.232.27:5001/ordem"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Info Ordens:", resposta.json())
            return resposta.json()
        else:
            return {"Erro": resposta.json()}

    # Salva as informações dos veículos
    def salvar_veiculo(e):
        # Caso eles não possuam valores
        if input_cliente_associado.value == "" or input_modelo.value == "" or input_placa.value == "" or input_ano_fabricacao.value == "" or input_marca.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_veiculo = Veiculo(
                cliente_associado=input_cliente_associado.value,
                modelo=input_modelo.value,
                placa=input_placa.value,
                ano_fabricacao=input_ano_fabricacao.value,
                marca=input_marca.value,

            )
            # Adiciona o Valor de cliente_associado, modelo, placa, ano_fabricacao e marca na Lista
            input_cliente_associado.value = ""
            input_modelo.value = ""
            input_placa.value = ""
            input_ano_fabricacao.value = ""
            input_marca.value = ""
            Local_session.add(obj_veiculo)
            Local_session.commit()
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento de Veículos

    # Salva as informações dos Clientes
    def salvar_cliente(e):
        # Caso eles não possuam valores
        if input_nome.value == "" or input_cpf.value == "" or input_email.value == "" or input_telefone.value == "" or input_endereco.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_cliente = Cliente(
                nome=input_nome.value,
                cpf=input_cpf.value,
                email=input_email.value,
                telefone=input_telefone.value,
                endereco=input_endereco.value,

            )
            # Adiciona o Valor de cliente_associado, modelo, placa, ano_fabricacao e marca na Lista
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_telefone.value = ""
            input_endereco.value = ""
            Local_session.add(obj_cliente)
            Local_session.commit()
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento de Clientes

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
            Local_session.add(obj_ordem)
            Local_session.commit()
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento das Ordens

    # FIM da exibição da lista

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
                            on_click=lambda _: salvar_veiculo(e),
                            bgcolor=Colors.PURPLE_900,
                        ),
                        # Irá mostrar os Dados
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/cadastro_veiculos"),
                            bgcolor=Colors.PURPLE_900,
                        )
                    ],
                )
            )
        # Lista de Veículos
        if page.route == "/lista_veiculos":
            page.views.append(
                View(
                    "/Lista_veiculos",
                    [
                        AppBar(title=Text("Lista de Veículos"), bgcolor=Colors.PURPLE_900),
                        salvar_veiculo,
                        lv_nome,
                        ft.Button(
                            text="Sair",
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
                            on_click=lambda _: salvar_cliente(e),
                            bgcolor=Colors.PURPLE_900,
                        ),
                        ft.Button(
                            text="Exibir lista",
                            on_click=lambda _: page.go("/lista_clientes"),
                        )
                    ]
                )
            )
        # Lista de Clientes
        if page.route == "/lista_clientes":
            page.views.append(
                View(
                    "/Lista_clientes",
                    [
                        AppBar(title=Text("Lista de Clientes"), bgcolor=Colors.PURPLE_900),
                        salvar_cliente,
                        lv_nome,
                        ft.Button(
                            text="Sair",
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
                            on_click=lambda _: page.go("lista_ordens"),
                            bgcolor=Colors.PURPLE_900,
                        )
                    ]
                )
            )
            # Lista de Ordens
            if page.route == "/lista_ordens":
                page.views.append(
                    View(
                        "/Lista_ordens",
                        [
                            AppBar(title=Text("Lista de Ordens"), bgcolor=Colors.PURPLE_900),
                            salvar_ordem,
                            lv_nome,
                            ft.Button(
                                text="ir",
                                on_click=lambda _: page.go("/terceira"),
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

    # FIM da seta de Voltar

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
    input_valor_estimado = ft.TextField(label="Valor Estimado", bgcolor=Colors.DEEP_PURPLE)
    lv_nome = ft.ListView(
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
