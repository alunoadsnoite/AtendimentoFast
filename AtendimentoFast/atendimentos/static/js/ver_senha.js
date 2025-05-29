function abrirModal() {
  document.getElementById('modalSenha').style.display = 'flex';
  document.getElementById('mensagemErro').style.display = 'none';
  document.getElementById('senhaReveladaModal').innerText = '';
  document.getElementById('cpf').value = '';
}

function fecharModal() {
  document.getElementById('modalSenha').style.display = 'none';
}

function verificarCPF() {
  const cpfInput = document.getElementById('cpf').value;
  const cpfCorreto = '1234'; // Altere isso para os 4 últimos dígitos reais
  const senha = 'minhaSenha123'; // Altere para a senha real do usuário

  if (cpfInput === cpfCorreto) {
    document.getElementById('mensagemErro').style.display = 'none';
    document.getElementById('senhaReveladaModal').innerText = 'Senha: ' + senha;
  } else {
    document.getElementById('mensagemErro').style.display = 'block';
    document.getElementById('senhaReveladaModal').innerText = '';
  }
}

function abrirModalEditarSenha() {
  document.getElementById('modalEditarSenha').style.display = 'flex';
}

function fecharModalEditarSenha() {
  document.getElementById('modalEditarSenha').style.display = 'none';
  document.getElementById('mensagemErro').textContent = '';
}

function salvarNovaSenha() {
  const senhaAtual = document.getElementById('senhaAtual').value;
  const novaSenha = document.getElementById('novaSenha').value;
  const confirmarSenha = document.getElementById('confirmarSenha').value;
  const msg = document.getElementById('mensagemErro');

  if (!senhaAtual || !novaSenha || !confirmarSenha) {
    msg.textContent = 'Preencha todos os campos.';
    return;
  }

  if (novaSenha !== confirmarSenha) {
    msg.textContent = 'As senhas não coincidem.';
    return;
  }

  
  alert('Senha alterada com sucesso!');
  fecharModalEditarSenha();
}