document.addEventListener('DOMContentLoaded', () => {
  const servicoSelect = document.getElementById('servico');
  const dataInput = document.getElementById('data');
  const horariosDiv = document.getElementById('horarios');
  const form = document.getElementById('form-agendar');
  const inputServico = document.getElementById('input-servico');
  const inputData = document.getElementById('input-data');
  const inputHorario = document.getElementById('input-horario');
  const btnAgendar = document.getElementById('btnAgendar');

  let horarioSelecionado = '';

  function carregarHorariosDisponiveis(servico, data) {
    horariosDiv.innerHTML = '';

    if (servico && data) {
      const horarios = ['08:00', '09:30', '11:00', '14:00', '16:30', '18:30'];
      horarios.forEach(horario => {
        const botao = document.createElement('button');
        botao.textContent = horario;
        botao.type = 'button';
        botao.classList.add('botao-horario');
        botao.onclick = () => {
          horarioSelecionado = horario;
          inputHorario.value = horario;

          document.querySelectorAll('.botao-horario').forEach(b => b.classList.remove('selecionado'));
          botao.classList.add('selecionado');
        };
        horariosDiv.appendChild(botao);
      });
    }
  }

  servicoSelect.addEventListener('change', () => {
    carregarHorariosDisponiveis(servicoSelect.value, dataInput.value);
  });

  dataInput.addEventListener('change', () => {
    carregarHorariosDisponiveis(servicoSelect.value, dataInput.value);
  });

  btnAgendar?.addEventListener('click', (e) => {
    e.preventDefault();

    if (!servicoSelect.value) {
      alert('Por favor, selecione um serviço.');
      return;
    }

    if (!dataInput.value) {
      alert('Por favor, selecione uma data.');
      return;
    }

    if (!horarioSelecionado) {
      alert('Por favor, selecione um horário.');
      return;
    }

    // Preencher os campos ocultos corretamente
    inputServico.value = servicoSelect.value;
    inputData.value = dataInput.value;
    inputHorario.value = horarioSelecionado;

    form.submit();
  });
});