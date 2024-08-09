//Positivo e Negativo
// Console.Write("Digite um número: ");
// double numero = Convert.ToDouble(Console.ReadLine());

// if (numero > 0) {
//     Console.WriteLine("O número é positivo.");
// }
// else {
//     Console.WriteLine("O número é negativo.");
// }

// Console.Write("Digite um número: ");
// double numero1 = Convert.ToDouble(Console.ReadLine());

// if (numero < 0) {
//     Console.WriteLine ("O número é negativo.");
// }
// else {
//     Console.WriteLine("O número é positivo.");
// }

//Par e Impar
// Console.Write("Digite um número inteiro: ");
// int numeroInt = Convert.ToInt32(Console.ReadLine());

// if (numeroInt % 2 == 0) {
//     Console.WriteLine("O número é par.");
// } 
// else {
//     Console.WriteLine("O número é ímpar.");
// }

//Consulta de média
// Console.Write("Digite sua média: ");
// double media = Convert.ToDouble(Console.ReadLine());

// if (media >= 9) {
//     Console.WriteLine("Não fez mais que a obrigação.");
// }

// else if (media >= 7) {
//     Console.WriteLine("Mais ou menos.");
// }

// else if (media >= 6) {
//     Console.WriteLine("Passou raspando, vagabundo.");
// }

// else {
//     Console.WriteLine("Rodou, piázão.");
// }

// //Calcular IMC
// Console.Write("Informe sua altura: ");
// double altura = Convert.ToDouble(Console.ReadLine());
// Console.Write("Informe seu peso: ");
// double peso = Convert.ToDouble(Console.ReadLine());

// double imc = (peso / (Math.Pow(altura, 2)));

// if (imc <= 18.5) {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você está abaixo do peso.");
// }

// else if (imc >= 18.6 && imc <= 24.9) {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você está com o peso ideal.");
// }

// else if (imc >= 25.0 && imc <= 29.9) {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você está levemente acima do peso.");
// }

// else if (imc >= 30.0 && imc <= 34.9) {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você tem obesidade de primeiro grau.");
// }

// else if (imc >= 35.0 && imc <= 39.9) {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você tem obesidade severa.");
// }

// else {
//     Console.WriteLine($"Seu IMC é {imc:F2}. Você tem obesidade mórbida.");
// }

//Dias da semana com Switch Case
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

// Console.Write("Digite o seu Estado Civil [S - Solteiro, C - Casado, D - Divorciado, V - Viúvo]: ");
// char estadoCivil = Char.ToUpper(Convert.ToChar(Console.ReadLine()));

// switch (estadoCivil) {
//     case 'S':
//     Console.WriteLine("Você está solteiro.");
//     break;

//     case 'C':
//     Console.WriteLine("Você está casado.");
//     break;

//     case 'D':
//     Console.WriteLine("Você está divorciado.");
//     break;

//     case 'V':
//     Console.WriteLine("Você é viúvo.");
//     break;
// }