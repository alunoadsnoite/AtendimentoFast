document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const servico = urlParams.get('servico');
  const data = urlParams.get('data');
  const horario = urlParams.get('horario');

  const elServico = document.getElementById('info-servico');
  const elData = document.getElementById('info-data');
  const elHorario = document.getElementById('info-horario');

  if (elServico) elServico.textContent = servico || 'Não informado';
  if (elData) elData.textContent = data || 'Não informado';
  if (elHorario) elHorario.textContent = horario || 'Não informado';
});

document.addEventListener('DOMContentLoaded', () => {
    const modalOverlay = document.getElementById('modalOverlay');
    const btnConfirmar = document.getElementById('btnConfirmar');
    const modalOkBtn = document.getElementById('modalOkBtn');

    btnConfirmar.addEventListener('click', () => {
      modalOverlay.style.display = 'flex';  // abre o modal
    });

    modalOkBtn.addEventListener('click', () => {
      modalOverlay.style.display = 'none';  // fecha o modal
      window.location.href = '/pagina_inicial_adm/';  // redireciona
    });
  });