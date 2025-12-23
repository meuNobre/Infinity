let nomes = [];

while (true) {
  let entrada = prompt("Digite um nome (ou 'sair' para encerrar):");

  if (entrada === "sair") {
    break;
  }

  nomes.push(entrada);
}

for (let i = 0; i < nomes.length; i++) {
  console.log((i + 1) + ": " + nomes[i]);
}

for (let nome of nomes) {
  console.log("Bem-vindo(a), " + nome + "!");
}
