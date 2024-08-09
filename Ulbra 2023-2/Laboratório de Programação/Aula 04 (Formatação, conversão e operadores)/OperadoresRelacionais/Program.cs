// //Operadores Relacionais

// int x = 10;
// int y = 20;

// // Igual
// Console.WriteLine(x == y);

// // Maior
// Console.WriteLine(x > y);

// // Menor
// Console.WriteLine(x < y);

// // Maior ou igual
// Console.WriteLine(x >= y);

// // Menor ou igual
// Console.WriteLine(x <= y);

// // Diferente
// Console.WriteLine(x != y);

// //Operadores Lógicos

// bool c1 = true;
// bool c2 = false;
// bool resultado;

// //Operador And
// resultado = c1 && c2;
// Console.WriteLine(resultado);

// //Operador Or
// resultado = c1 || c2;
// Console.WriteLine(resultado);

// //Operador Not
// resultado = !c2;
// Console.WriteLine(resultado);

//Operador Ternário
// condicao / valorSeVerdadeiro : valorSeFalse

int numero = 5;
string resultadoTernario = (numero % 2 == 0) ? "Par" : "Impar";
Console.WriteLine(resultadoTernario);