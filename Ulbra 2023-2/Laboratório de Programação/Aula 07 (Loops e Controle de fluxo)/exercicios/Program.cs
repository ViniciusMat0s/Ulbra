// // Exercício 1: Soma de Números de 1 a 10
// // Escreva um programa que utilize um loop for para calcular e exibir na tela a soma dos números inteiros de 1 a 10. Mostre o resultado final após o loop.
// int soma = 0;

// for (int i = 1; i <= 10; i++) {
//     soma = soma + i;
// }
// Console.WriteLine($"A soma dos valores de um a dez é: {soma}");

// // Exercício 2: Contagem Regressiva com while
// // Crie um programa que use um loop while para realizar uma contagem regressiva a partir de 10 até 0. A cada iteração, o programa deve exibir o número atual no console.
// int i = 10;
// while (i >= 0) {
//     Console.WriteLine(i);
//     i++;
// }

// // Exercício 3: Pular Números Ímpares
// // Desenvolva um programa que utilize um loop for e a palavra-chave continue para imprimir todos os números pares entre 1 e 20. Evite imprimir os números ímpares.
// for (int i = 1; i <= 20; i++) {
//     if (i % 2 != 0) {
//         continue;
//     }
//     Console.WriteLine(i);
// }

// // Exercício 4: Sair Quando o Quadrado For Maior que 50
// // Escreva um programa que utilize um loop while e a palavra-chave break. O programa deve calcular os quadrados dos números inteiros começando com 1 e parar assim que um quadrado maior que 50 for encontrado. Exiba esse valor no console.
// int i = 1;
// while (true) {
//     int quadrado = i * i;
//     if (quadrado > 50) {
//         Console.WriteLine($"O quadrado de {i} é {quadrado}, que é maior que 50.");
//         break;
//     }
//     i++;
// }


// // Exercício 5: Tabuada de um Número Usando for
// // Crie um programa que solicite ao usuário um número inteiro. Utilize um loop for para imprimir a tabuada desse número, de 1 a 10. Mostre cada linha da tabuada no console.
// Console.Write("Digite um número inteiro: ");
// int num = Convert.ToInt32(Console.ReadLine());
// for (int i = 1; i <= 10; i++) {
//     Console.WriteLine($"{num} x {i} = {num * i}");
// }

// // Exercício 6: Soma com Loop do-while
// // Desenvolva um programa que utilize um loop do-while para solicitar números inteiros ao usuário. Continue somando esses números até que o usuário insira o número 0. Mostre a soma total ao final.
// int soma = 0;
// int num = 0;
// do {
//     Console.Write("Digite um número inteiro (0 - para sair): ");
//     num = Convert.ToInt32(Console.ReadLine());
//     soma += num;
// } while (num != 0);
// Console.Write($"A soma dos números é: {soma}");

// Exercício 7: Encontrar o Primeiro Múltiplo de 3 e 7
// Utilize um loop for e a palavra-chave break para procurar o primeiro número que seja múltiplo tanto de 3 quanto de 7, dentro do intervalo de 1 a 100. Exiba esse número no console.
// for (int i = 1; i <= 100; i++) {
//     if (i % 3 == 0 && i % 7 == 0) {
//         Console.WriteLine($"O primeiro múltiplo de 3 e de 7 é {i}");
//         break;
//     }
// }

// // Exercício 8: Fatorial de um Número
// // Peça ao usuário para inserir um número inteiro positivo. Utilize um loop for para calcular o fatorial desse número. Exiba o resultado no console.

// Console.Write("Digite um número inteiro positivo: ");
// int num = Convert.ToInt32(Console.ReadLine());
// long fatorial = 1;
// for (int i = 1; i <= num; i++) {
//     fatorial *= i;
// }
// Console.WriteLine($"O fatorial de {num} é {fatorial}.");