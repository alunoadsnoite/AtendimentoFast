from django.urls import path
from . import views
from .views import cadastrar_cliente_adm

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('pagina_inicial_cliente/', views.pagina_inicial_cliente, name='pagina_inicial_cliente'),
    path('pagina_inicial_adm/', views.pagina_inicial_adm, name='pagina_inicial_adm'),
    path('menu_adm/', views.menu_adm, name='menu_adm'),
    path('menu_cliente/', views.menu_cliente, name='menu_cliente'),
    path('agendar_atendimento/', views.agendar_atendimento, name='agendar_atendimento'),
    path('confirmar_agendamento/', views.confirmar_agendamento, name='confirmar_agendamento'),
    path('perfil_cliente/', views.perfil_cliente, name='perfil_cliente'),
    path('fila_cliente/', views.fila_cliente, name='fila_cliente'),
    path('agendamentos_cliente/', views.agendamentos_cliente, name='agendamentos_cliente'),
    path('editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('remarcar_cliente/', views.remarcar_cliente, name='remarcar_cliente'),
    path('confirmar_remarcacao', views.confirmar_remarcacao, name='confirmar_remarcacao'),
    path('buscar_cliente', views.buscar_cliente, name='buscar_cliente'),
    path('cadastrar_cliente_adm', views.cadastrar_cliente_adm, name='cadastrar_cliente_adm'),
    path('cadastrar_servicos_adm', views.cadastrar_servicos_adm, name='cadastrar_servicos_adm'),
    path('encaixa_fila_adm', views.encaixa_fila_adm, name='encaixa_fila_adm'),
    path('fila_atendimento_adm', views.fila_atendimento_adm, name='fila_atendimento_adm'),
    path('horario_atendimento', views.horario_atendimento, name='horario_atendimento'),
    path('salvar_horarios/', views.salvar_horarios, name='salvar_horarios'),
    path('pagina_inicial_adm', views.pagina_inicial_adm, name='pagina_inicial_adm'),
    path('perfil_adm', views.perfil_adm, name='perfil_adm'),
    path('remarcar_atendimento_adm', views.remarcar_atendimento_adm, name='remarcar_atendimento_adm'),
    path('servicos_cadastrado', views.listar_servicos, name='servicos_cadastrado'),
    path('agenda_adm', views.servicos_cadastrado, name='agenda_adm'),
    path('agendar-atendimento/<int:cliente_id>/', views.agendar_atendimento_adm, name='agendar_atendimento_adm'),
    path('verificar_cadastro', views.verificar_cadastro, name='verificar_cadastro'),
    path('confirmar_agendamento_adm', views.confirmar_agendamento_adm, name='confirmar_agendamento_adm'),
    path('dados_cliente_adm/<int:cliente_id>/', views.dados_cliente_adm, name='dados_cliente_adm'),
    path('servico/<int:id>/editar/', views.editar_servico, name='editar_servico'),
    path('servico/<int:id>/excluir/', views.excluir_servico, name='excluir_servico'),
]







