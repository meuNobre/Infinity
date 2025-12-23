let lista = [];

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar item\n2 - Remover item\n3 - Atualizar item\n4 - Exibir lista\n5 - Sair"
  );

  if (opcao === "5") break;

  if (opcao === "1") {
    let item = prompt("Digite o item para adicionar:");
    lista.push(item);
  } 
  else if (opcao === "2") {
    let indice = Number(prompt("Digite o índice do item para remover:"));
    lista.splice(indice, 1);
  } 
  else if (opcao === "3") {
    let indice = Number(prompt("Digite o índice do item para atualizar:"));
    let novoItem = prompt("Digite o novo valor:");
    lista[indice] = novoItem;
  } 
  else if (opcao === "4") {
    let i = 0;
    for (let item of lista) {
      console.log(i + ": " + item);
      i++;
    }
  }
}
