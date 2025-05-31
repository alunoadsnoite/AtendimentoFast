document.addEventListener('DOMContentLoaded', () => {
  const inputData = document.getElementById('data');
  if (!inputData) return;

  const hoje = new Date().toISOString().split('T')[0];
  inputData.setAttribute('min', hoje);
});