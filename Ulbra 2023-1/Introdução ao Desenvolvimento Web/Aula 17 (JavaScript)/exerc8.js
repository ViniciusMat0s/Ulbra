//8 - Faça um script que leia números até que seja digitado um número negativo, ao final mostrar a média dos números digitados. 

let numero = 0;
let soma = 0;
let contador = 0;

while (numero >= 0) {
  numero = Number(prompt("Digite um número (negativo para sair):"));
  if (numero >= 0) {
    contador++;
    soma += numero;
  }
}
if (contador > 0) {
  const media = soma / contador;
  alert("A média dos números digitados é: " + media);

} else {
  alert("Nenhum número foi digitado.");
}
