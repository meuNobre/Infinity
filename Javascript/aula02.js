let idade = Number(prompt("Digite sua idade:"));
let status = prompt("Digite seu status (registrado ou não registrado):");

let classificacao = idade >= 18 ? "Maior de idade" : "Menor de idade";
console.log(classificacao);

switch (status) {
  case "registrado":
    console.log("Bem-vindo!");
    break;
  case "não registrado":
    console.log("Complete seu registro.");
    break;
  default:
    console.log("Status desconhecido.");
}

if (idade >= 18 && status === "registrado") {
  console.log("Acesso completo.");
} else if (idade < 18 || status !== "registrado") {
  console.log("Acesso limitado.");
}
