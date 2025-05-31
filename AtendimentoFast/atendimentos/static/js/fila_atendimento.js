function abrirModal(agendamentoId) {
  const modal = document.getElementById("modal-cancelar");
  const form = document.getElementById("form-cancelar");
  form.action = `/cancelar_agendamento/${agendamentoId}/?next=/fila_atendimento_adm`; 
  modal.style.display = "flex";
}

function fecharModal() {
  document.getElementById("modal-cancelar").style.display = "none";
}

// Fechar o modal ao clicar fora
window.onclick = function(event) {
  const modal = document.getElementById("modal-cancelar");
  if (event.target === modal) {
    fecharModal();
  }
}