 const form = document.getElementById('form-servico');
  const modal = document.getElementById('modal');
  const btnVerServicos = document.getElementById('btn-ver-servicos');
  const btnCadastrarNovo = document.getElementById('btn-cadastrar-novo');

  form.addEventListener('submit', function(e) {
   

    modal.style.display = 'flex';
  });

  btnVerServicos.addEventListener('click', () => {
    window.location.href = '/servicos_cadastrado';
  });

  btnCadastrarNovo.addEventListener('click', () => {
    modal.style.display = 'none';
    form.reset();
  });