*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     http://localhost:8000/fila_cliente/   # Ajuste conforme sua URL real

*** Test Cases ***
Página Fila Cliente Carrega
    Open Browser    ${URL}    Chrome
    Title Should Be    Fila de Atendimento
    Page Should Contain Element    xpath://h1[contains(text(), 'Fila de Atendimento')]
    Page Should Contain Element    xpath://aside[contains(@class, 'menu-lateral')]
    Page Should Contain Element    xpath://a[contains(@href, 'agendar_atendimento')]
    Page Should Contain Element    xpath://a[contains(@href, 'agendamentos_cliente')]
    Page Should Contain Element    xpath://a[contains(@href, 'fila_cliente')]
    Page Should Contain Element    xpath://a[contains(@href, 'perfil_cliente')]
    Page Should Contain Element    xpath://a[contains(@href, 'inicio')]
    [Teardown]    Close Browser