let idAgendamentoParaCancelar = null;
const modalCancelar= document.getElementById('modalCancelar')


document.addEventListener('DOMContentLoaded', function() {
  const divDia = document.querySelector('.agenda-dia');
  const divSemana = document.querySelector('.agenda-semana');
  const divMes = document.querySelector('.agenda-mes');
  const seletor = document.querySelector('#seletorPeriodo');

  function atualizarExibicao() {
    if (!seletor || !divDia || !divSemana || !divMes) return;

    const valor = seletor.value;
    divDia.style.display = 'none';
    divSemana.style.display = 'none';
    divMes.style.display = 'none';

    if (valor === 'Dia') {
      divDia.style.display = 'block';
    } else if (valor === 'Semana') {
      divSemana.style.display = 'block';
    } else if (valor === 'Mês') {
      divMes.style.display = 'grid';
    }
  }

  if (seletor) {
    seletor.addEventListener('change', atualizarExibicao);
    atualizarExibicao();
  }

  // --- Modal de confirmação de cancelamento ---
  const modal = document.getElementById('modalCancelar');
  const btnsCancelar = document.querySelectorAll('.btn-cancelar');
  const btnConfirmar = document.getElementById('confirmarCancelarBtn');
  const btnFechar = document.getElementById('fecharModalBtn');

  let idAgendamentoParaCancelar = null;

  if (btnsCancelar.length > 0 && modal) {
    btnsCancelar.forEach(btn => {
      btn.addEventListener('click', function(event) {
        event.preventDefault();
        idAgendamentoParaCancelar = this.getAttribute('data-id');
        modal.style.display = 'flex';
      });
    });
  }

  if (btnFechar && modal) {
    btnFechar.addEventListener('click', () => {
      modal.style.display = 'none';
      idAgendamentoParaCancelar = null;
    });
  }

  if (btnConfirmar && modal) {
   btnConfirmar.addEventListener('click', () => {
  console.log("ID a cancelar:", idAgendamentoParaCancelar);

  if (idAgendamentoParaCancelar) {
    const currentParams = new URLSearchParams(window.location.search);
    const currentPath = window.location.pathname;
    const nextUrl = currentPath + '?' + currentParams.toString();

    const url = `/cancelar_agendamento/${idAgendamentoParaCancelar}/?next=${encodeURIComponent(nextUrl)}`;
    console.log("Redirecionando para:", url);
    window.location.href = url;
  } else {
    console.log("Nenhum ID para cancelar!");
  }
});
  }

  if (modal) {
    window.addEventListener('click', (event) => {
      if (event.target === modal) {
        modal.style.display = 'none';
        idAgendamentoParaCancelar = null;
      }
    });
  }
});

//Modal da semana

function abrirModal(id) {
  const agendamento = agendamentosSemana[id];
  if (!agendamento) return alert('Agendamento não encontrado');

  document.getElementById('modalCliente').textContent = agendamento.cliente;
  document.getElementById('modalServico').textContent = agendamento.servico;
  document.getElementById('modalHorario').textContent = agendamento.horario;

  // Guarda o id no dataset do modal para usar nos botões
  const modal = document.getElementById('modalDetalheAgendamento');
  modal.dataset.agendamentoId = id;
  modal.style.display = 'flex';
}

function fecharModalDetalhe() {
  document.getElementById('modalDetalheAgendamento').style.display = 'none';
}

// Botão fechar
document.getElementById('btnFecharDetalhe').addEventListener('click', fecharModalDetalhe);

// Botão cancelar
document.getElementById('btnCancelar').addEventListener('click', function() {
  const modalDetalhe = document.getElementById('modalDetalheAgendamento');
  const id = modalDetalhe.dataset.agendamentoId;

  fecharModalDetalhe(); // Fecha o modal de detalhe

  idAgendamentoParaCancelar = id;
document.getElementById('modalCancelarSemana').style.display = 'flex';
});

// Botão remarcar
document.getElementById('btnRemarcar').addEventListener('click', function() {
  const modal = document.getElementById('modalDetalheAgendamento');
  const id = modal.dataset.agendamentoId;

  
  window.location.href = `/remarcar_atendimento_adm/${id}/`;
});

// Fechar o modal clicando fora da área do conteúdo
window.addEventListener('click', function(event) {
  const modal = document.getElementById('modalDetalheAgendamento');
  if (event.target === modal) {
    fecharModalDetalhe();
  }
});


// --- Eventos do novo modalCancelarSemana ---
const modalCancelarSemana = document.getElementById('modalCancelarSemana');
const btnConfirmarSemana = document.getElementById('confirmarCancelarSemanaBtn');
const btnFecharSemana = document.getElementById('fecharModalSemanaBtn');

if (btnFecharSemana && modalCancelarSemana) {
  btnFecharSemana.addEventListener('click', () => {
    modalCancelarSemana.style.display = 'none';
    idAgendamentoParaCancelar = null;
  });
}

if (btnConfirmarSemana && modalCancelarSemana) {
  btnConfirmarSemana.addEventListener('click', () => {
    console.log("ID a cancelar (SEMANA):", idAgendamentoParaCancelar);

    if (idAgendamentoParaCancelar) {
      const currentParams = new URLSearchParams(window.location.search);
      const currentPath = window.location.pathname;
      const nextUrl = currentPath + '?' + currentParams.toString();

      const url = `/cancelar_agendamento/${idAgendamentoParaCancelar}/?next=${encodeURIComponent(nextUrl)}`;
      console.log("Redirecionando (SEMANA) para:", url);
      window.location.href = url;
    } else {
      console.log("Nenhum ID para cancelar (SEMANA)!");
    }
  });
}

function abrirModalMes(id) {
  const elemento = document.querySelector(`.evento-dia[onclick="abrirModalMes('${id}')"]`);
  if (!elemento) return alert('Agendamento não encontrado.');

  const cliente = elemento.getAttribute('data-cliente');
  const servico = elemento.getAttribute('data-servico');
  const horario = elemento.getAttribute('data-horario');

  document.getElementById('modalCliente').textContent = cliente;
  document.getElementById('modalServico').textContent = servico;
  document.getElementById('modalHorario').textContent = horario;

  const modal = document.getElementById('modalDetalheAgendamento');
  modal.dataset.agendamentoId = id;
  modal.style.display = 'flex';
}