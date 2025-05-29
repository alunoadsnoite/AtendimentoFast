// Função para adicionar novo horário no dia indicado
function adicionarHorario(diaIndex) {
  const container = document.getElementById(`horarios_${diaIndex}`);

  const div = document.createElement('div');
  div.classList.add('horario-bloco');

  // Cria inputs com nomes dinâmicos para múltiplos blocos
  const timestamp = Date.now();

  const inputInicio = document.createElement('input');
  inputInicio.type = 'time';
  inputInicio.name = `inicio_${diaIndex}_novo_${timestamp}`;
  inputInicio.value = '08:00';

  const inputFim = document.createElement('input');
  inputFim.type = 'time';
  inputFim.name = `fim_${diaIndex}_novo_${timestamp}`;
  inputFim.value = '12:00';

  const btnRemover = document.createElement('button');
  btnRemover.type = 'button';
  btnRemover.innerHTML = '×';
  btnRemover.onclick = function() {
    div.remove();
  };

  div.appendChild(inputInicio);
  div.appendChild(inputFim);
  div.appendChild(btnRemover);

  container.appendChild(div);
}

// Função para remover horário ao clicar no botão de remover
function removerHorario(button) {
  button.parentElement.remove();
}

// Função para alterar a semana exibida (navegar entre semanas)
function alterarSemana(dias) {
  const url = new URL(window.location.href);
  const dataInicialStr = url.searchParams.get('data_inicial');
  let dataInicial = new Date();

  if (dataInicialStr) {
    // Corrige o formato da data para evitar fuso horário
    const parts = dataInicialStr.split('-');
    dataInicial = new Date(parts[0], parts[1] - 1, parts[2]);
  }

  dataInicial.setDate(dataInicial.getDate() + dias);

  // Formata a data para yyyy-mm-dd
  const ano = dataInicial.getFullYear();
  const mes = String(dataInicial.getMonth() + 1).padStart(2, '0');
  const dia = String(dataInicial.getDate()).padStart(2, '0');
  const novaDataStr = `${ano}-${mes}-${dia}`;

  url.searchParams.set('data_inicial', novaDataStr);
  window.location.href = url.toString();
}

// Adiciona eventos para os botões das setas, após o carregamento do DOM
document.addEventListener('DOMContentLoaded', function() {
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');

  if (btnPrev) {
    btnPrev.addEventListener('click', function() {
      alterarSemana(-7);
    });
  }

  if (btnNext) {
    btnNext.addEventListener('click', function() {
      alterarSemana(7);
    });
  }
});

const btnSalvar = document.getElementById('btn-salvar');
const form = document.querySelector('form');

// Escuta mudanças em qualquer input dentro do form
form.addEventListener('input', () => {
  btnSalvar.style.display = 'inline-block';
});