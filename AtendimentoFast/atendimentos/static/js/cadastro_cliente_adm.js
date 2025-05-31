
document.addEventListener("DOMContentLoaded", function () {
  // Máscara para Telefone
  const telefoneInput = document.getElementById("telefone");
  if (telefoneInput) {
    telefoneInput.addEventListener("input", function (e) {
      let valor = e.target.value.replace(/\D/g, "");
      if (valor.length > 11) valor = valor.slice(0, 11);
      valor = valor.replace(/^(\d{2})(\d)/g, "($1) $2");
      valor = valor.replace(/(\d{1})?(\d{4})(\d{4})$/, "$1 $2-$3");
      e.target.value = valor.trim();
    });
  }

  // Máscara para CPF
  const cpfInput = document.getElementById("cpf");
  if (cpfInput) {
    cpfInput.addEventListener("input", function (e) {
      let valor = e.target.value.replace(/\D/g, "").slice(0, 11);
      valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
      valor = valor.replace(/(\d{3})(\d)/, "$1.$2");
      valor = valor.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
      e.target.value = valor;
    });
  }

  /* Máscara para Data de Nascimento
  const dataInput = document.getElementById("nascimento");
  if (dataInput) {
    dataInput.addEventListener("input", function (e) {
      let valor = e.target.value.replace(/\D/g, "").slice(0, 8);
      valor = valor.replace(/(\d{2})(\d)/, "$1/$2");
      valor = valor.replace(/(\d{2})(\d)/, "$1/$2");
      e.target.value = valor;
    });
  } */

  // Máscara para CEP
  const cepInput = document.getElementById("cep");
  if (cepInput) {
    cepInput.addEventListener("input", function (e) {
      let valor = e.target.value.replace(/\D/g, "").slice(0, 8);
      valor = valor.replace(/(\d{5})(\d)/, "$1-$2");
      e.target.value = valor;
    });
  }
});

window.onload = function() {
  const cpfExistente = document.getElementById('cpf-existente');
  const clienteCadastrado = document.getElementById('cliente-cadastrado');

  if (cpfExistente) {
    document.getElementById('modalCpfExistente').style.display = 'flex';
  }

  if (clienteCadastrado) {
    document.getElementById('modalClienteCadastrado').style.display = 'flex';
  }
}

// Função para remover um parâmetro da URL sem recarregar a página
  function removeURLParameter(url, parameter) {
      var urlparts = url.split('?');
      if (urlparts.length >= 2) {
          var prefix = encodeURIComponent(parameter) + '=';
          var params = urlparts[1].split(/[&;]/g);

          // Filtra todos os parâmetros exceto o que queremos remover
          for (var i = params.length; i-- > 0;) {
              if (params[i].lastIndexOf(prefix, 0) !== -1) {
                  params.splice(i, 1);
              }
          }

          url = urlparts[0];
          if (params.length > 0) {
              url += '?' + params.join('&');
          }
          return url;
      } else {
          return url;
      }
  }

  // Remove o parâmetro 'novo' da URL
  window.history.replaceState({}, document.title, removeURLParameter(window.location.href, 'novo'));

document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('modalCpfExistente');

  if (modal) {
    // Fecha o modal ao clicar fora do conteúdo
    modal.addEventListener('click', function (e) {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });

    // Fecha com tecla Esc
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        modal.style.display = 'none';
      }
    });
  }
});