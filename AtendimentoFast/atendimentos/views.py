from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .models import Servico
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ClienteForm
from django.db.models import Q
from .models import HorarioAtendimento
from .models import Agendamento
from datetime import datetime, timedelta, date
from django.utils.dateparse import parse_date
from django.http import HttpResponseBadRequest, HttpResponse
from django.utils import timezone
from datetime import time
from collections import defaultdict
from django.http import HttpResponseRedirect
from django.urls import reverse
import calendar
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

DIAS_SEMANA_PT = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

def inicio_view(request):
    return render(request,'html/inicio.html')

def login_view(request):
    return render(request, 'html/login.html')

def cadastro_view(request):
    return render(request, 'html/cadastro.html')

def pagina_inicial_cliente(request):
    return render(request, 'html/pagina_inicial_cliente.html')

def pagina_inicial_adm(request):
    return render(request, 'html/pagina_inicial_adm.html')

def menu_adm(request):
    return render(request, 'html/menu_adm.html')

def menu_cliente(request):
    return render(request, 'html/menu_cliente.html')

def agendar_atendimento(request):
    return render(request, 'html/agendar_atendimento.html')

def confirmar_agendamento(request):
    return render(request, 'html/confirmar_agendamento.html')

def perfil_cliente(request):
    return render(request, 'html/perfil_cliente.html')

def agendamentos_cliente(request):
    return render(request, 'html/agendamentos_cliente.html')

def editar_cliente(request):
    return render(request, 'html/editar_cliente.html')

def fila_cliente(request):
    return render(request, 'html/fila_cliente.html')

def remarcar_cliente(request):
    return render(request, 'html/remarcar_cliente.html')

def confirmar_remarcacao(request):
    return render(request, 'html/confirmar_remarcacao.html')

def buscar_cliente(request):
    return render(request, 'adm/buscar_cliente.html')

def agenda_adm(request):
    hoje = timezone.now().date()
    periodo = request.GET.get('periodo', 'dia')  
    data_str = request.GET.get('data', '')
    data_selecionada = parse_date(data_str) or hoje
    dias_do_mes = None

    if periodo == 'dia':
        agendamentos_qs = Agendamento.objects.filter(data=data_selecionada).order_by('hora')
        dia_anterior = data_selecionada - timedelta(days=1)
        dia_posterior = data_selecionada + timedelta(days=1)

        context = {
            'periodo_selecionado': periodo,
            'agendamentos': agendamentos_qs,
            'data_selecionada': data_selecionada,
            'hoje': hoje,
            'dia_anterior': dia_anterior.isoformat(),
            'dia_posterior': dia_posterior.isoformat(),
        }
        return render(request, 'adm/agenda_adm.html', context)

    elif periodo == 'semana':
        semana_param = request.GET.get('semana')
        if semana_param:
            try:
                hoje = parse_date(semana_param) or hoje
            except ValueError:
                pass

        dias_da_semana = [hoje + timedelta(days=i) for i in range(7)]
        fim = dias_da_semana[-1]

        agendamentos_qs = Agendamento.objects.filter(data__range=[hoje, fim]).order_by('data', 'hora')
        agendamentos_por_dia = defaultdict(list)
        for ag in agendamentos_qs:
            agendamentos_por_dia[ag.data].append(ag)

        nomes_dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']

        semana_anterior = (hoje - timedelta(days=7)).isoformat()
        semana_proxima = (hoje + timedelta(days=7)).isoformat()

        context = {
            'periodo_selecionado': periodo,
            'dias_da_semana': dias_da_semana,
            'agendamentos_por_dia': agendamentos_por_dia,
            'nomes_dias_semana': nomes_dias_semana,
            'agendamentos': agendamentos_qs,
            'hoje': timezone.now().date(),
            'semana_anterior': semana_anterior,
            'semana_proxima': semana_proxima,
        }
        return render(request, 'adm/agenda_adm.html', context)

    elif periodo == 'mes':
        mes_param = request.GET.get('mes')  # Espera formato "2025-06"
        if mes_param:
            try:
                ano, mes = map(int, mes_param.split('-'))
                hoje = date(ano, mes, 1)
            except ValueError:
                ano = hoje.year
                mes = hoje.month
        else:
            ano = hoje.year
            mes = hoje.month

        primeiro_dia = date(ano, mes, 1)
        dias_no_mes = calendar.monthrange(ano, mes)[1]
        dias_do_mes = [primeiro_dia + timedelta(days=i) for i in range(dias_no_mes)]

        mes_anterior = (primeiro_dia.replace(day=1) - timedelta(days=1)).replace(day=1)
        mes_posterior = (primeiro_dia.replace(day=28) + timedelta(days=4)).replace(day=1)

        agendamentos_qs = Agendamento.objects.filter(
            data__year=ano,
            data__month=mes
        ).order_by('data', 'hora')

        agendamentos_por_dia = defaultdict(list)
        for ag in agendamentos_qs:
            agendamentos_por_dia[ag.data].append(ag)

        context = {
            'periodo_selecionado': periodo,
            'dias_do_mes': dias_do_mes,
            'agendamentos_por_dia': agendamentos_por_dia,
            'agendamentos': agendamentos_qs,
            'hoje': hoje,
            'mes_anterior': mes_anterior.strftime('%Y-%m'),
            'mes_posterior': mes_posterior.strftime('%Y-%m'),
        }
        return render(request, 'adm/agenda_adm.html', context)

def cadastrar_servicos_adm(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        duracao = request.POST.get('duracao')

        print(f"POST: nome={nome}, descricao={descricao}, preco={preco}, duracao={duracao}")

        if nome and duracao:
            try:
                duracao = int(duracao)
                preco = float(preco) if preco else None

                servico = Servico(
                    nome=nome,
                    descricao=descricao,
                    preco=preco,
                    duracao=duracao
                )
                servico.save()
                print("Serviço salvo com sucesso.")
                messages.success(request, 'Serviço cadastrado com sucesso!')
                return redirect('cadastrar_servicos_adm')

            except ValueError:
                messages.error(request, 'Preencha os campos corretamente.')
        else:
            messages.error(request, 'Nome e duração são obrigatórios.')

    return render(request, 'adm/cadastrar_servicos_adm.html')


def encaixa_fila_adm(request):
    return render(request, 'adm/encaixa_fila_adm.html')


def pagina_inicial_adm(request):
    return render(request, 'adm/pagina_inicial_adm.html')

def servicos_cadastrado(request):
    return render(request, 'adm/servicos_cadastrado.html')

def verificar_cadastro(request):
    return render(request, 'adm/verificar_cadastro.html')

def agendar_atendimento_adm(request, cliente_id=None):
    cliente = None
    if cliente_id:
        cliente = get_object_or_404(Cliente, id=cliente_id)

    servicos = Servico.objects.all()

    servico_id = request.GET.get('servico')
    data_str = request.GET.get('data')

    duracao_servico = None
    servico = None
    if servico_id:
        try:
            servico = Servico.objects.get(id=servico_id)
            duracao_servico = servico.duracao
        except Servico.DoesNotExist:
            servico = None
            duracao_servico = None

    data = None
    horarios_disponiveis = []

    if data_str:
        data = datetime.strptime(data_str, '%Y-%m-%d').date()

        weekday = data.weekday()
        dia_semana = '0' if weekday == 6 else str(weekday + 1)

        horarios = HorarioAtendimento.objects.filter(
            dia_semana=dia_semana,
            ativo=True
        )

        agendamentos = Agendamento.objects.filter(data=data)

        def horario_disponivel(hora_teste):
            for ag in agendamentos:
                ag_inicio = datetime.combine(data, ag.hora)
                ag_fim = ag_inicio + timedelta(minutes=ag.servico.duracao)
                teste_inicio = datetime.combine(data, hora_teste)
                teste_fim = teste_inicio + timedelta(minutes=duracao_servico)
                if (teste_inicio < ag_fim) and (ag_inicio < teste_fim):
                    return False
            return True

        for horario in horarios:
            hora_atual = datetime.combine(data, horario.hora_inicio)
            hora_fim = datetime.combine(data, horario.hora_fim)

            while hora_atual + timedelta(minutes=duracao_servico or 30) <= hora_fim:
                # Filtra horários que já passaram se for hoje
                if data == datetime.today().date():
                    if hora_atual.time() < datetime.now().time():
                        hora_atual += timedelta(minutes=30)
                        continue

                if duracao_servico:
                    if horario_disponivel(hora_atual.time()):
                        horarios_disponiveis.append(hora_atual.time())
                else:
                    horarios_disponiveis.append(hora_atual.time())
                hora_atual += timedelta(minutes=30)

    context = {
        'cliente': cliente,
        'cliente_id': cliente_id,
        'servicos': servicos,
        'servico_id': servico_id,
        'data': data,
        'horarios_disponiveis': horarios_disponiveis
    }

    return render(request, 'adm/agendar_atendimento_adm.html', context)


def dados_cliente_adm(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'adm/dados_cliente_adm.html', {'cliente': cliente})


def buscar_cliente(request):
    query = request.GET.get('query')
    clientes = None

    if query:
        clientes = Cliente.objects.filter(
            Q(nome_completo__icontains=query) | Q(cpf__icontains=query)
        )
    
    return render(request, 'adm/buscar_cliente.html', {'clientes': clientes, 'query': query})


def listar_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'adm/servicos_cadastrado.html', {'servicos': servicos})

def editar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)

    if request.method == 'POST':
        servico.nome = request.POST.get('nome')
        servico.descricao = request.POST.get('descricao')
        servico.preco = request.POST.get('preco')
        servico.duracao = request.POST.get('duracao')
        servico.save()
        messages.success(request, 'Serviço atualizado com sucesso!')
        return redirect('servicos_cadastrado')  

    return render(request, 'adm/editar_servico.html', {'servico': servico})

def excluir_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    messages.success(request, 'Serviço excluído com sucesso!')
    return redirect('servicos_cadastrado') 
   


def cadastrar_cliente_adm(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        endereco = request.POST.get('endereco')
        cep = request.POST.get('cep')
        cpf = request.POST.get('cpf')

        if not all([nome_completo, email, telefone, data_nascimento, endereco, cep, cpf]):
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return redirect('cadastrar_cliente_adm')

        if Cliente.objects.filter(cpf=cpf).exists():
            return redirect('/cadastrar_cliente_adm?cpf_existente=1')

        cliente = Cliente.objects.create(
            nome_completo=nome_completo,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            endereco=endereco,
            cep=cep,
            cpf=cpf
        )

        return redirect(f'/cadastrar_cliente_adm?cliente_id={cliente.id}&novo=1')

    cliente_id = request.GET.get('cliente_id')
    novo = request.GET.get('novo') == '1'
    cpf_existente = request.GET.get('cpf_existente') == '1'

    return render(request, 'adm/cadastrar_cliente_adm.html', {
        'cliente_id': cliente_id,
        'novo': novo,
        'cpf_existente': cpf_existente,
    })


def horario_atendimento(request):
    hoje = datetime.today()

    data_inicial_str = request.GET.get('data_inicial')
    if data_inicial_str:
        data_inicial = datetime.strptime(data_inicial_str, '%Y-%m-%d')
    else:
        if hoje.weekday() == 0:  # segunda
            data_inicial = hoje
        else:
            data_inicial = hoje - timedelta(days=hoje.weekday())

    dias_semana = []

    for i in range(7):  # Segunda a domingo
        data = data_inicial + timedelta(days=i)
        dia_semana = data.weekday()  # 0 = segunda, ..., 6 = domingo
        django_dia_semana = '0' if dia_semana == 6 else str(dia_semana + 1)

        horarios_queryset = HorarioAtendimento.objects.filter(dia_semana=django_dia_semana)

        horarios = []
        for h in horarios_queryset:
            horarios.append({
                'inicio': h.hora_inicio.strftime('%H:%M'),
                'fim': h.hora_fim.strftime('%H:%M'),
            })

        dias_semana.append({
            'data': data.strftime('%d/%m/%Y'),
            'data_iso': data.strftime('%Y-%m-%d'),
            'dia_semana_nome': DIAS_SEMANA_PT[dia_semana],
            'codigo': django_dia_semana,
            'horarios': horarios,
            'ativo': any(h.ativo for h in horarios_queryset)
        })

    data_anterior = data_inicial - timedelta(days=7)
    data_proximo = data_inicial + timedelta(days=7)

    contexto = {
        'dias': dias_semana,
        'data_inicial': data_inicial.strftime('%Y-%m-%d'),
        'data_anterior': data_anterior.strftime('%Y-%m-%d'),
        'data_proximo': data_proximo.strftime('%Y-%m-%d'),
    }

    return render(request, 'adm/horario_atendimento.html', contexto)


def salvar_horarios(request):
    if request.method == "POST":
        data_inicial = request.POST.get('data_inicial')

        for i in range(7):  # 0 a 6 - Segunda a Domingo
            ativo = request.POST.get(f'ativo_{i}') == 'on'
            horarios = []

            j = 0
            while True:
                inicio = request.POST.get(f'inicio_{i}_{j}')
                fim = request.POST.get(f'fim_{i}_{j}')

                if not inicio or not fim:
                    break

                horarios.append((inicio, fim))
                j += 1

            django_dia_semana = '0' if i == 6 else str(i + 1)

            # Exclui os horários antigos para o mesmo dia
            HorarioAtendimento.objects.filter(dia_semana=django_dia_semana).delete()

            # Salva novos horários
            for inicio, fim in horarios:
                HorarioAtendimento.objects.create(
                    dia_semana=django_dia_semana,
                    hora_inicio=datetime.strptime(inicio, '%H:%M').time(),
                    hora_fim=datetime.strptime(fim, '%H:%M').time(),
                    ativo=ativo
                )

        return redirect('horario_atendimento')  # Redireciona após salvar

    return redirect('horario_atendimento')

def formatar_cpf(cpf):
    # Supondo que cpf venha só números "00000000000"
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def formatar_telefone(telefone):
    # Supondo telefone numérico "00000000000" ou "0000000000"
    tel = ''.join(filter(str.isdigit, telefone))
    if len(tel) == 11:
        return f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
    elif len(tel) == 10:
        return f"({tel[:2]}) {tel[2:6]}-{tel[6:]}"
    return telefone

def formatar_data(data):
    # Data é um objeto date
    if isinstance(data, datetime):
        return data.strftime('%d/%m/%Y %H:%M')
    elif hasattr(data, 'strftime'):
        return data.strftime('%d/%m/%Y')
    return data

def dados_cliente_adm(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    agendamentos = Agendamento.objects.filter(cliente=cliente).order_by('data', 'hora')

    # Formatar os dados do cliente
    cliente.cpf_formatado = formatar_cpf(cliente.cpf)
    cliente.telefone_formatado = formatar_telefone(cliente.telefone)
    cliente.data_nascimento_formatada = formatar_data(cliente.data_nascimento)

    # Formatar datas e horas dos agendamentos
    for ag in agendamentos:
        ag.data_formatada = formatar_data(ag.data)
        if ag.hora:
            ag.hora_formatada = ag.hora.strftime('%H:%M')
        else:
            ag.hora_formatada = ''

    context = {
        'cliente': cliente,
        'agendamentos': agendamentos,
    }
    return render(request, 'adm/dados_cliente_adm.html', context)

def confirmar_agendamento_adm(request):
    print("Entrou na view confirmar_agendamento_adm")
    print(f"Request method: {request.method}")

    if request.method == 'POST' and 'confirmar' in request.POST:
        cliente_id = request.POST.get('cliente_id')
        servico_id = request.POST.get('servico_id')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        print(f"servico_id recebido (confirmar): {servico_id}")

        # Validar se IDs são válidos
        if not (cliente_id and cliente_id.isdigit()) or not (servico_id and servico_id.isdigit()):
            return HttpResponseBadRequest("ID do cliente ou serviço inválido")

        # Buscar os objetos Cliente e Serviço
        cliente = get_object_or_404(Cliente, id=int(cliente_id))
        servico = get_object_or_404(Servico, id=int(servico_id))

        # Criar agendamento
        agendamento = Agendamento.objects.create(
            cliente=cliente,
            servico=servico,
            data=data,
            hora=hora,
            status='confirmado'
        )

        contexto = {
            'agendamento': agendamento,
            'mostrar_modal_sucesso': True,
            'cliente': cliente,
            'servico': servico,
            'data': data,
            'hora': hora,
        }

        return render(request, 'adm/confirmar_agendamento_adm.html', contexto)

    elif request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        servico_id = request.POST.get('servico_id')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        print("servico_id recebido (confirmar_agendamento_adm):", servico_id)

        if not servico_id or not servico_id.isdigit():
            return HttpResponseBadRequest("ID do serviço inválido")

        cliente = get_object_or_404(Cliente, id=cliente_id)
        servico = get_object_or_404(Servico, id=int(servico_id))

        contexto = {
            'cliente': cliente,
            'servico': servico,
            'data': data,
            'hora': hora,
        }

        return render(request, 'adm/confirmar_agendamento_adm.html', contexto)

    elif request.method == 'GET':
         cliente_id = request.GET.get('cliente_id')
    servico_id = request.GET.get('servico_id')
    data = request.GET.get('data')
    hora = request.GET.get('hora')

    if cliente_id and servico_id and data and hora:
        cliente = get_object_or_404(Cliente, id=cliente_id)
        servico = get_object_or_404(Servico, id=servico_id)

        contexto = {
            'cliente': cliente,
            'servico': servico,
            'data': data,
            'hora': hora,
        }

        return render(request, 'adm/confirmar_agendamento_adm.html', contexto)

    return redirect('pagina_inicial_adm')
    

def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.delete()
    messages.success(request, 'Agendamento cancelado com sucesso.')

    # Primeira prioridade: se tiver "next", redireciona pra ele
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)

    # Segunda prioridade: monta com periodo e data, se existirem
    periodo = request.GET.get('periodo')
    data = request.GET.get('data')

    if periodo and data:
        return redirect(f'/agenda_adm?periodo={periodo}&data={data}')
    
    # Fallback padrão
    return redirect('/agenda_adm?periodo=dia')

def remarcar_atendimento_adm(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    servico = agendamento.servico
    cliente = agendamento.cliente
    duracao_servico = servico.duracao

    data_str = request.GET.get('data')
    data = None
    horarios_disponiveis = []

    if data_str:
        data = datetime.strptime(data_str, '%Y-%m-%d').date()

        weekday = data.weekday()
        dia_semana = '0' if weekday == 6 else str(weekday + 1)

        horarios = HorarioAtendimento.objects.filter(
            dia_semana=dia_semana,
            ativo=True
        )

        agendamentos_no_dia = Agendamento.objects.filter(data=data).exclude(id=agendamento.id)

        for horario in horarios:
            hora_atual = datetime.combine(data, horario.hora_inicio)
            hora_fim = datetime.combine(data, horario.hora_fim)

            while hora_atual + timedelta(minutes=duracao_servico) <= hora_fim:
                # Remover horários que já passaram se for hoje
                if data == datetime.today().date():
                    if hora_atual.time() < datetime.now().time():
                        hora_atual += timedelta(minutes=30)
                        continue

                sobreposto = False
                for ag in agendamentos_no_dia:
                    inicio_ag = datetime.combine(ag.data, ag.hora)
                    fim_ag = inicio_ag + timedelta(minutes=ag.servico.duracao)
                    fim_atual = hora_atual + timedelta(minutes=duracao_servico)

                    if (hora_atual < fim_ag) and (fim_atual > inicio_ag):
                        sobreposto = True
                        break

                if not sobreposto:
                    horarios_disponiveis.append(hora_atual.time())

                hora_atual += timedelta(minutes=30)

    if request.method == 'POST':
        nova_data = request.POST.get('data')
        nova_hora = request.POST.get('hora')

        if nova_data and nova_hora:
            url_confirmar = reverse('confirmar_agendamento_adm') + f'?cliente_id={cliente.id}&servico_id={servico.id}&data={nova_data}&hora={nova_hora}'
            return HttpResponseRedirect(url_confirmar)

    context = {
        'agendamento': agendamento,
        'cliente': cliente,
        'servico': servico,
        'data': data,
        'horarios_disponiveis': horarios_disponiveis,
    }
    return render(request, 'adm/remarcar_atendimento_adm.html', context)

def fila_atendimento_adm(request):
    hoje = timezone.localdate()
    agora = timezone.localtime().time()

    # 1. Pega os agendamentos do dia com status pendente ou confirmado
    agendamentos_do_dia = Agendamento.objects.filter(
        data=hoje,
        status__in=['pendente', 'confirmado']
    )

    # 2. Atualiza para "pendente" os que já passaram do horário
    for agendamento in agendamentos_do_dia:
        if agendamento.status == 'confirmado' and agendamento.hora < agora:
            agendamento.status = 'pendente'
            agendamento.save()

    # 3. Filtra somente os agendamentos ainda válidos para exibir na fila
    fila = Agendamento.objects.filter(
        data=hoje,
        status__in=['pendente', 'confirmado'],
        hora__gte=agora  # só exibe os que ainda não aconteceram
    ).order_by('hora')

    return render(request, 'adm/fila_atendimento_adm.html', {'fila': fila})


@require_POST
def finalizar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    agendamento.status = 'finalizado'
    agendamento.save()
    messages.success(request, 'Agendamento finalizado com sucesso.')
    return redirect('fila_atendimento_adm')  

@login_required
def perfil_adm(request):
   return render(request, 'adm/perfil_adm.html', {
        'user': request.user
    })

