document.addEventListener('DOMContentLoaded', () => {
    const modalOverlay = document.getElementById('modalOverlay');
    const btnConfirmar = document.getElementById('btnConfirmar');
    const modalOkBtn = document.getElementById('modalOkBtn');

    btnConfirmar.addEventListener('click', () => {
      modalOverlay.style.display = 'flex';  // abre o modal
    });

    modalOkBtn.addEventListener('click', () => {
      modalOverlay.style.display = 'none';  // fecha o modal
      window.location.href = '/pagina_inicial_cliente/';  // redireciona
    });
  });