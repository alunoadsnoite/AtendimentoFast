 // Lista de horários simulados
  const horariosDisponiveis = [
    '09:00', '09:30', '10:00', '10:30',
    '11:00', '11:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30'
  ];

  const containerHorarios = document.getElementById('horarios');
  const btnAgendar = document.getElementById('btnAgendar');
  let horarioSelecionado = null;

  // Gera os botões de horário
  horariosDisponiveis.forEach(horario => {
    const btn = document.createElement('div');
    btn.classList.add('horario-item');
    btn.textContent = horario;

    btn.addEventListener('click', () => {
      // Desmarcar anterior
      if (horarioSelecionado) {
        horarioSelecionado.classList.remove('selected');
      }
      // Marcar novo
      btn.classList.add('selected');
      horarioSelecionado = btn;
    });

    containerHorarios.appendChild(btn);
  });

  // Simula o agendamento (sem backend)
  btnAgendar.addEventListener('click', () => {
    const servico = document.getElementById('servico').value;
    const data = document.getElementById('data').value;

    if (!servico || !data || !horarioSelecionado) {
      alert('Por favor, selecione um serviço, data e horário.');
      return;
    }

    const horario = horarioSelecionado.textContent;

    // Simulação de confirmação
    alert(Agendamento confirmado:\n\nServiço: ${servico}\nData: ${data}\nHorário: ${horario});
  });