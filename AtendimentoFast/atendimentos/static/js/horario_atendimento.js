// Garante que a data passada seja ajustada para a segunda-feira da semana
function getSegundaFeira(data) {
  const dia = data.getDay(); // 0=Domingo, 1=Segunda, ..., 6=Sábado
  const diff = (dia === 0 ? -6 : 1) - dia; 
  data.setDate(data.getDate() + diff);
  return data;
}

// Função para alterar a semana exibida
function alterarSemana(dias) {
  const url = new URL(window.location.href);
  const dataInicialStr = url.searchParams.get('data_inicial');
  let dataInicial = new Date();

  if (dataInicialStr) {
    const parts = dataInicialStr.split('-');
    dataInicial = new Date(parts[0], parts[1] - 1, parts[2]);
  }

  // Ajusta para segunda-feira antes de mudar a semana
  dataInicial = getSegundaFeira(dataInicial);

  // Muda a semana
  dataInicial.setDate(dataInicial.getDate() + dias);

  // Garante que sempre fique na segunda-feira após ajuste
  dataInicial = getSegundaFeira(dataInicial);

  const ano = dataInicial.getFullYear();
  const mes = String(dataInicial.getMonth() + 1).padStart(2, '0');
  const dia = String(dataInicial.getDate()).padStart(2, '0');
  const novaDataStr = `${ano}-${mes}-${dia}`;

  url.searchParams.set('data_inicial', novaDataStr);
  window.location.href = url.toString();
}

// Associa os eventos de clique às setas
document.addEventListener('DOMContentLoaded', function () {
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');

  if (btnPrev) {
    btnPrev.addEventListener('click', function () {
      alterarSemana(-7); // Voltar 7 dias
    });
  }

  if (btnNext) {
    btnNext.addEventListener('click', function () {
      alterarSemana(7); // Avançar 7 dias
    });
  }
});

// Adiciona um novo horário no dia especificado pelo índice
function adicionarHorario(diaIndex) {
  const container = document.getElementById(`horarios_${diaIndex}`);

  const horarioBloco = document.createElement('div');
  horarioBloco.className = 'horario-bloco';

  horarioBloco.innerHTML = `
    <span class="horario-brackets">[</span>
    <input type="time" name="inicio_${diaIndex}_${container.children.length}" value="">
    <span class="horario-brackets">]</span>
    <span class="horario-separador">às</span>
    <span class="horario-brackets">[</span>
    <input type="time" name="fim_${diaIndex}_${container.children.length}" value="">
    <span class="horario-brackets">]</span>
    <button type="button" onclick="removerHorario(this)">×</button>
  `;

  container.appendChild(horarioBloco);
}

// Remove um horário ao clicar no botão '×'
function removerHorario(botao) {
  const horarioBloco = botao.parentElement;
  horarioBloco.remove();
}

// Se quiser adicionar event listeners para inputs, pode colocar aqui
document.querySelectorAll('input, checkbox').forEach(elem => {
  elem.addEventListener('input', () => {
    // Nada a fazer por enquanto
  });
});