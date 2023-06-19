//2 - Faça um script que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

let numero = Number(prompt("Digite um número: "))

if (numero % 2 == 0){
    alert(`O número ${numero} é par.`)
}else{
    alert(`O número ${numero} é ímpar.`)
}
