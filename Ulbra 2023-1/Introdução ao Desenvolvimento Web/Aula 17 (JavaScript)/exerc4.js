//4 - Faça um script que receba um número, calcule e mostre a tabuada desse número.

let numero = parseInt(prompt("Digite um número inteiro: "));

console.log(`Tabuada de ${numero}:`);
for (let i = 1; i <= 10; i++) {
    let resultado = numero * i;
    alert(`${numero} x ${i} = ${resultado}`);
}
