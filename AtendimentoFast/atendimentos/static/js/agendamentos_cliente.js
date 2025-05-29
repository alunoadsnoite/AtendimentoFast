function abrirModal(tipo) {
  const modal = document.getElementById('modal-' + tipo);
  if (modal) {
    modal.style.display = 'flex';
  }
}

function fecharModal() {
  const modais = document.querySelectorAll('.modal');
  modais.forEach(modal => {
    modal.style.display = 'none';
  });
}