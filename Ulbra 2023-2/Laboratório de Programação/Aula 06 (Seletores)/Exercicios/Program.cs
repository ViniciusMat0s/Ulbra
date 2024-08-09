// //Exercício 1:
// Console.Write("Digite um número: ");
// double numero = Convert.ToDouble(Console.ReadLine());
// if (numero > 0) {
//     Console.WriteLine("Número positivo.");
// }

// else if (numero == 0) {
//     Console.WriteLine("Número zero.");
// }

// else {
//     Console.WriteLine("Número negativo.");
// }

// //Exercício 2:
// Console.Write("Informe um número de um a sete (1 a 7), com base nos dias da semana: ");
// int numero = Convert.ToInt32(Console.ReadLine());

// switch (numero) {
//     case 1:
//     Console.WriteLine("Domingo.");
//     break;

//     case 2:
//     Console.WriteLine("Segunda-feira.");
//     break;

//     case 3:
//     Console.WriteLine("Terça-feira.");
//     break;

//     case 4:
//     Console.WriteLine("Quarta-feira.");
//     break;

//     case 5:
//     Console.WriteLine("Quinta-feira.");
//     break;

//     case 6:
//     Console.WriteLine("Sexta-feira.");
//     break;

//     case 7:
//     Console.WriteLine("Sábado.");
//     break;

//     default:
//     Console.WriteLine("Inválido.");
//     break;
// }

// //Exercício 3:
// Console.Write("Digite sua idade: ");
// int idade = Convert.ToInt32(Console.ReadLine());

// if (idade >= 0 && idade <= 12) {
//     Console.WriteLine("Criança (0-12 anos).");
// }

// else if (idade >= 13 && idade <= 18) {
//     Console.WriteLine("Adolescente (13-18 anos).");
// }

// else if (idade >= 19 && idade <= 59) {
//     Console.WriteLine("Adulto (19-59 anos)");
// }

// else if (idade >= 60) {
//     Console.WriteLine("Idoso (60 anos ou mais).");
// }
// else {
//     Console.WriteLine("Idade inválida.");
// }

// //Exercício 4:
// Console.Write("Digite o ano: ");
// int ano = Convert.ToInt32(Console.ReadLine());
// if (ano % 4 == 0 && ano % 100 !=0 || ano % 400 == 0) {
//     Console.WriteLine($"O ano {ano} é bissexto.");
// }
// else {
//     Console.WriteLine($"O ano {ano} não é bissexto.");
// }

// //Exercício 5:
// Console.WriteLine("Digite a operação que deseja fazer [1 - Soma] | [2 - Subtração] | [3 - Multiplicação] | [4 - Divisão]: ");
// int escolha = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Digite o primeiro número: ");
// double n1 = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine("Digite o segundo número: ");
// double n2 = Convert.ToDouble(Console.ReadLine());

// switch (escolha) {
//     case 1:
//     Console.WriteLine($"A soma é: {n1 + n2}");
//     break;

//     case 2:
//     Console.WriteLine($"A subtração é: {n1 - n2}");
//     break;

//     case 3:
//     Console.WriteLine($"A multiplicação é: {n1 * n2}");
//     break;

//     case 4:
//     Console.WriteLine($"A divisão é {n1 / n2 }");
//     break;

//     default:
//     Console.WriteLine("Opção inválida.");
//     break;
// }

// // Exercício 6:
// Console.Write("Digite a nota: ");
// double nota = Convert.ToDouble(Console.ReadLine());
// if (nota >= 90 && nota <= 100) {
//     Console.WriteLine("Nota A.");
// }
// else if (nota >= 80 && nota <= 89) {
//     Console.WriteLine("Nota B");
// }
// else if (nota >= 70 && nota <= 79) {
//     Console.WriteLine("Nota C.");
// }
// else if (nota >= 60 && nota <= 69) {
//     Console.WriteLine("Nota D");
// }
// else if (nota >= 0 && nota <= 59) {
//     Console.WriteLine("Nota F");
// }
// else {
//     Console.WriteLine("Nota inválida.");
// }

// // Exercício 7:
// Console.Write("Informe um número de um a doze (1 a 12), com base nos meses do ano: ");
// int numero = Convert.ToInt32(Console.ReadLine());

// switch (numero) {
//     case 1:
//     Console.WriteLine("Janeiro.");
//     break;

//     case 2:
//     Console.WriteLine("Fevereiro.");
//     break;

//     case 3:
//     Console.WriteLine("Março.");
//     break;

//     case 4:
//     Console.WriteLine("Abril.");
//     break;

//     case 5:
//     Console.WriteLine("Maio.");
//     break;

//     case 6:
//     Console.WriteLine("Junho.");
//     break;

//     case 7:
//     Console.WriteLine("Julho.");
//     break;

//     case 8:
//     Console.WriteLine("Agosto");
//     break;

//     case 9:
//     Console.WriteLine("Setembro");
//     break;

//     case 10:
//     Console.WriteLine("Outubro");
//     break;

//     case 11:
//     Console.WriteLine("Novembro.");
//     break;

//     case 12:
//     Console.WriteLine("Dezembro.");
//     break;

//     default:
//     Console.WriteLine("Opção inválida.");
//     break;
// }

// // Exercício 8:
// Console.Write("Digite o primeiro número: ");
// double n1 = Convert.ToDouble(Console.ReadLine());
// Console.Write("Digite o segundo número: ");
// double n2 = Convert.ToDouble(Console.ReadLine());
// Console.Write("Digite o terceiro número: ");
// double n3 = Convert.ToDouble(Console.ReadLine());

// if (n1 > n2 && n1 > n3) {
//     Console.WriteLine($"O maior número é o primeiro [{n1}]");
// }
// else if (n2 > n1 && n2 > n3) {
//     Console.WriteLine($"O maior número é o segundo [{n2}]");
// }
// else {
//     Console.WriteLine($"O maior número é o terceiro [{n3}]");
// }

// // Exercício 9:
// Console.Write("Informe sua idade: ");
// int idade = Convert.ToInt32(Console.ReadLine());
// Console.Write("Digite o valor da tarifa padrão: ");
// double tarifa = Convert.ToDouble(Console.ReadLine());

// if (idade >= 0 && idade <= 5) {
//     Console.WriteLine($"Tarifa padrão no valor de R$ {tarifa} | Desconto de 100% (R$ 0,00.)");
// }
// else if (idade >= 6 && idade <= 12) {
//     Console.WriteLine($"Tarifa padrão no valor de R$ {tarifa} | Desconto de 50% ({tarifa / 2}).");
// }
// else if (idade >= 13 && idade <= 59) {
//     Console.WriteLine($"Tarifa padrão no valor de R$ {tarifa} | Sem desconto ({tarifa}).");
// }
// else if (idade >= 60) {
//     Console.WriteLine($"Tarifa padrão no valor de R$ {tarifa} | Desconto de 100% (0,00).");
// }
// else {
//     Console.WriteLine("Valor inválido.");
// }

// // Exercício 10:
// Console.Write("Informe a temperatura (sem o (º): ");
// double temperatura = Convert.ToDouble(Console.ReadLine());

// if (temperatura < 0) {
//     Console.WriteLine("Congelando!");
// }
// else if (temperatura >= 0 && temperatura <= 15) {
//     Console.WriteLine("Frio!");
// }
// else if (temperatura >= 16 && temperatura <= 25) {
//     Console.WriteLine("Clima agradável");
// }
// else if (temperatura >= 26 && temperatura <= 35) {
//     Console.WriteLine("Calor!");
// }
// else {
//     Console.WriteLine("Muito quente!");
// }