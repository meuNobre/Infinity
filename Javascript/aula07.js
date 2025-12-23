let nomes = [];

while (true) {
  let opcao = prompt(
    "Escolha uma opção:\n1 - Adicionar nome\n2 - Filtrar nomes\n3 - Buscar nome\n4 - Transformar em maiúsculas\n5 - Verificar tamanho\n6 - Sair"
  );

  if (opcao === "6") break;

  if (opcao === "1") {
    let nome = prompt("Digite um nome:");
    nomes.push(nome);
    console.log(nomes);
  } 
  else if (opcao === "2") {
    let letra = prompt("Digite a letra inicial:");
    let filtrados = nomes.filter(n => n.startsWith(letra));
    console.log(filtrados);
  } 
  else if (opcao === "3") {
    let busca = prompt("Digite o nome para buscar:");
    let encontrado = nomes.find(n => n === busca);
    console.log(encontrado ? encontrado : "Nome não encontrado");
  } 
  else if (opcao === "4") {
    let maiusculos = nomes.map(n => n.toUpperCase());
    console.log(maiusculos);
  } 
  else if (opcao === "5") {
    let todosMaiores = nomes.every(n => n.length > 3);
    console.log(todosMaiores);
  }
}
