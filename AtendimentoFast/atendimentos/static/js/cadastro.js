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

  // Máscara para Data de Nascimento
  const dataInput = document.getElementById("nascimento");
  if (dataInput) {
    dataInput.addEventListener("input", function (e) {
      let valor = e.target.value.replace(/\D/g, "").slice(0, 8);
      valor = valor.replace(/(\d{2})(\d)/, "$1/$2");
      valor = valor.replace(/(\d{2})(\d)/, "$1/$2");
      e.target.value = valor;
    });
  }

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

// Função global para mostrar/ocultar senha e trocar o ícone
function togglePassword(inputId, iconElement) {
  const input = document.getElementById(inputId);
  if (!input) return;

  const isPassword = input.type === "password";
  input.type = isPassword ? "text" : "password";

  // Alternar ícones entre olho aberto e fechado
  iconElement.classList.toggle("fa-eye");
  iconElement.classList.toggle("fa-eye-slash");
}