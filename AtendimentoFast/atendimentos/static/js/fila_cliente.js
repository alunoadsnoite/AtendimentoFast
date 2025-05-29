document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('modalCPF');
  const cpfInput = document.getElementById('cpfInput');
  const confirmarBtn = document.getElementById('confirmarBtn');
  const fecharBtn = document.getElementById('fecharBtn');
  const erroCPF = document.getElementById('erroCPF');

  let acaoSelecionada = null; // "cancelar" ou "remarcar"
  let clienteIdSelecionado = null;

  // Abrir modal quando clicar nos botões cancelar/remarcar
  document.querySelectorAll('.acoes button').forEach(botao => {
    botao.addEventListener('click', () => {
      acaoSelecionada = botao.getAttribute('data-acao');
      clienteIdSelecionado = botao.closest('.card-fila').getAttribute('data-cliente-id');
      cpfInput.value = '';
      erroCPF.style.display = 'none';
      modal.style.display = 'block';
      cpfInput.focus();
    });
  });

  // Fechar modal sem ação
  fecharBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  // Confirmar CPF digitado
  confirmarBtn.addEventListener('click', () => {
    const cpfDigitado = cpfInput.value.trim();

    if (cpfDigitado.length !== 4 || !/^\d{4}$/.test(cpfDigitado)) {
      erroCPF.style.display = 'block';
      return;
    }
    erroCPF.style.display = 'none';

   

    if (acaoSelecionada === 'cancelar') {
      // Fechar modal e remover o card da fila para simular cancelamento
      modal.style.display = 'none';

      // Remover o card do cliente logado
      const card = document.querySelector(.card-fila[data-cliente-id="${clienteIdSelecionado}"]);
      if (card) card.remove();

      alert('Consulta cancelada com sucesso!');
      
      // Aqui poderia fazer reload ou atualizar lista via fetch
    } 
    else if (acaoSelecionada === 'remarcar') {
      // Redirecionar para página remarcar_cliente
      window.location.href = '/remarcar_cliente/';
    }
  });

  // Fechar modal ao clicar fora da área do conteúdo
  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
});