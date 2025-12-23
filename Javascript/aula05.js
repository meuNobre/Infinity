let tarefas = [];

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Remover tarefa\n4 - Concluir tarefa\n5 - Sair"
  );

  if (opcao === "5") break;

  if (opcao === "1") {
    let tarefa = prompt("Digite o nome da tarefa:");
    tarefas.push(tarefa);
  } 
  else if (opcao === "2") {
    for (let i = 0; i < tarefas.length; i++) {
      console.log(i + ": " + tarefas[i]);
    }
  } 
  else if (opcao === "3") {
    let indice = Number(prompt("Digite o índice da tarefa para remover:"));
    tarefas.splice(indice, 1);
  } 
  else if (opcao === "4") {
    let indice = Number(prompt("Digite o índice da tarefa para concluir:"));
    tarefas[indice] = "✅ " + tarefas[indice];
  }
}
