// scripts.js – funcionalidades básicas para o sistema FASAR

document.addEventListener("DOMContentLoaded", function () {
  console.log("📦 FASAR scripts.js carregado com sucesso");

  // Exemplo: scroll automático para os resultados após upload
  if (document.querySelector("table")) {
    document.querySelector("table").scrollIntoView({ behavior: "smooth" });
  }

  // Exemplo: alerta se mais de 10 arquivos forem selecionados no leitor OCR
  const inputFiles = document.getElementById("files");
  if (inputFiles) {
    inputFiles.addEventListener("change", function () {
      if (this.files.length > 10) {
        alert("⚠️ Você só pode enviar até 10 arquivos por vez.");
        this.value = "";
      }
    });
  }
});

