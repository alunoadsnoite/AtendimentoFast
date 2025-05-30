*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:8000/pagina_inicial_cliente/    # Ajuste conforme sua URL real

*** Test Cases ***
Página Inicial do Cliente Carrega e Tem Botões
    Open Browser    ${URL}    Chrome
    Title Should Be    Área do Cliente
    Page Should Contain Element    xpath://h1[contains(text(), 'Bem-vindo, Cliente!')]
    Page Should Contain Element    xpath://a[contains(@href, 'perfil_cliente') and contains(text(), 'Perfil')]
    Page Should Contain Element    xpath://a[contains(@href, 'fila_cliente') and contains(text(), 'Fila de espera')]
    Page Should Contain Element    xpath://a[contains(@href, 'agendamentos_cliente') and contains(text(), 'Meus agendamentos')]
    Page Should Contain Element    xpath://a[contains(@href, 'agendar_atendimento') and contains(text(), 'Agendar atendimento')]
    Page Should Contain Element    xpath://a[contains(@href, 'inicio') and contains(text(), 'Sair')]
    [Teardown]    Close Browser