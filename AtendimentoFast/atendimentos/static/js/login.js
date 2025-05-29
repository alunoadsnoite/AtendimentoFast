document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.querySelector(".toggle-password");
  const senhaInput = document.getElementById("senha");

  toggleBtn.addEventListener("click", function () {
    if (senhaInput.type === "password") {
      senhaInput.type = "text";
      toggleBtn.classList.remove("fa-eye");
      toggleBtn.classList.add("fa-eye-slash");
    } else {
      senhaInput.type = "password";
      toggleBtn.classList.remove("fa-eye-slash");
      toggleBtn.classList.add("fa-eye");
    }
  });
});