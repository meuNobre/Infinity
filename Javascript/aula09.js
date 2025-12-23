let aluno = {
  nome: "Ana",
  idade: 16,
  notas: [6, 8, 7],
  calcularMedia() {
    let soma = 0;
    for (let nota of this.notas) {
      soma += nota;
    }
    return soma / this.notas.length;
  }
};

let { nome, idade } = aluno;

aluno.notas = [...aluno.notas, 9];

function verificarSituacao(media) {
  if (media >= 7) {
    return "Aprovado";
  } else {
    return "Reprovado";
  }
}

console.log("Nome:", nome);
console.log("Idade:", idade);

for (let nota of aluno.notas) {
  console.log("Nota:", nota);
}

let mediaFinal = aluno.calcularMedia();
console.log("Média final:", mediaFinal);
console.log("Situação:", verificarSituacao(mediaFinal));
