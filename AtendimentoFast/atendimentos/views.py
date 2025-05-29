from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .models import Servico
from django.contrib import messages
from .forms import ClienteForm
from django.db.models import Q
from .models import HorarioAtendimento
from .models import Agendamento
from datetime import datetime, timedelta
import calendar

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
    return render(request, 'adm/agenda_adm.html')

def cadastrar_cliente_adm(request):
    return render(request, 'adm/cadastrar_cliente_adm.html')

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

def dados_cliente_adm(request):
    return render(request, 'adm/dados_cliente_adm.html')

def encaixa_fila_adm(request):
    return render(request, 'adm/encaixa_fila_adm.html')

def fila_atendimento_adm(request):
    return render(request, 'adm/fila_atendimento_adm.html')

def pagina_inicial_adm(request):
    return render(request, 'adm/pagina_inicial_adm.html')

def perfil_adm(request):
    return render(request, 'adm/perfil_adm.html')

def remarcar_atendimento_adm(request):
    return render(request, 'adm/remarcar_atendimento_adm.html')

def servicos_cadastrado(request):
    return render(request, 'adm/servicos_cadastrado.html')

def verificar_cadastro(request):
    return render(request, 'adm/verificar_cadastro.html')

def agendar_atendimento_adm(request, cliente_id=None):
    cliente = None
    if cliente_id:
        cliente = get_object_or_404(Cliente, id=cliente_id)

    servicos = Servico.objects.all()

    context = {
        'cliente': cliente,
        'servicos': servicos,
    }
    return render(request, 'adm/agendar_atendimento_adm.html', context)


def confirmar_agendamento_adm(request):
    return render(request, 'adm/confirmar_agendamento_adm.html')

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
                    hora_inicio=inicio,
                    hora_fim=fim,
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

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        endereco = request.POST.get('endereco')
        cep = request.POST.get('cep')
        cpf = request.POST.get('cpf')

        if not all([nome, email, telefone, data_nascimento, endereco, cep, cpf]):
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'html/cadastro.html')

        if Cliente.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return render(request, 'html/cadastro.html')

        Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            endereco=endereco,
            cep=cep,
            cpf=cpf
        )
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')

    return render(request, 'html/cadastro.html')