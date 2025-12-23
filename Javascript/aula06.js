let tarefas = [];

let adicionarTarefa = function (tarefa) {
  tarefas.push(tarefa);
};

let listarTarefas = () => {
  for (let i = 0; i < tarefas.length; i++) {
    console.log(i + ": " + tarefas[i]);
  }
};

function executarOperacao(callback) {
  callback();
}

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Remover tarefa\n4 - Atualizar tarefa\n5 - Concluir tarefa\n6 - Sair"
  );

  if (opcao === "6") break;

  if (opcao === "1") {
    let tarefa = prompt("Digite a tarefa:");
    adicionarTarefa(tarefa);
  } 
  else if (opcao === "2") {
    listarTarefas();
  } 
  else if (opcao === "3") {
    executarOperacao(function () {
      let indice = Number(prompt("Digite o índice da tarefa para remover:"));
      tarefas.splice(indice, 1);
    });
  } 
  else if (opcao === "4") {
    executarOperacao(function () {
      let indice = Number(prompt("Digite o índice da tarefa para atualizar:"));
      let novaTarefa = prompt("Digite o novo valor:");
      tarefas[indice] = novaTarefa;
    });
  } 
  else if (opcao === "5") {
    executarOperacao(function () {
      let indice = Number(prompt("Digite o índice da tarefa para concluir:"));
      tarefas[indice] = "✅ " + tarefas[indice];
    });
  }
}
