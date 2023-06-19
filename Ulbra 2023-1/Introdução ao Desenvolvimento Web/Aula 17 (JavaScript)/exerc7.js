//7 - Faça um script que apresenta a soma dos números múltiplos de 3 entre 0 e 100. 

let numeros = []

let soma = 0;

for (let i = 0; i <= 100; i++) {
  if (i % 3 === 0) {
    numeros.push(i,"_");
    soma += i;
    console.log(numeros);
    }
}
alert(`Os números são: \n\n${numeros}`)
alert(`A soma dos números é: ${soma}`)
