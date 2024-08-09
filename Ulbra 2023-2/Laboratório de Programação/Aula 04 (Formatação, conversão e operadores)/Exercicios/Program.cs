//Exercício 1
string nome = "Paulo";
int idade = 17;
double nota = 7.5;

Console.WriteLine($"{nome} tem {idade} anos e nota {nota}.");
Console.WriteLine(nome + " tem " + idade + " anos e nota " + nota + ".");

//Exercício 2
string nomeIdade = $"\n{nome}\n {idade}";
Console.WriteLine(nomeIdade);

//Exercício 3
Console.WriteLine("Digite a primeira letra: ");
string n1 = Console.ReadLine();
Console.WriteLine("Digite a segunda letra: ");
string n2 = Console.ReadLine();
Console.WriteLine("Digite a terceira letra: ");
string n3 = Console.ReadLine();
Console.WriteLine($"{n3}, {n2}, {n1}");
Console.WriteLine(n3 + ", " + n2 + ", " + n1);

//Exercício 4
Console.WriteLine("Digite o primeiro valor: ");
double valor1 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine("Digite o segundo valor: ");
double valor2 = Convert.ToDouble(Console.ReadLine());

Console.WriteLine($"Resultado da soma: {valor1 + valor2}");
Console.WriteLine($"Resultado da subtração: {valor1 - valor2}");
Console.WriteLine($"Resultado da multiplicação: {valor1 * valor2}");
Console.WriteLine($"Resultado da exponenciação: {Math.Pow(valor1,valor2)}");
Console.WriteLine($"Resultado da divisão: {valor1 / valor2}");
Console.WriteLine($"Resultado do módulo: {valor1 % valor2}");

//Exercício 5
double a = 1;
double b = 12;
double c = -13;
double delta = (b*b) - (4*a*c);
double x1 = ((-b + (Math.Sqrt(delta))) / (2*a));
double x2 = ((-b - (Math.Sqrt(delta))) / (2*a));
Console.WriteLine($"{x1} e {x2}");


Exercício 6
Console.WriteLine("Digite o nome de usuário: ");
string nomeVal = Console.ReadLine();
Console.WriteLine("Digite sua senha: ");
int senhaVal = Convert.ToInt32(Console.ReadLine());

string login = ((nomeVal == "admin" || nomeVal == "Maria") && senhaVal == 123) ? "Login feito com sucesso" : "Login inválido";
Console.WriteLine(login);

Exercício 7
Console.WriteLine("Digite o primeiro número inteiro: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Digite o segundo número inteiro: ");
int y = Convert.ToInt32(Console.ReadLine());

string x1 = (x % 2 == 0) ? "Par" : "Impar";
Console.WriteLine(x1);
string y1 = (y % 2 == 1) ? "Impar" : "Par";
Console.WriteLine(y1);