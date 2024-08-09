// // Exercício 1: Classe Mensagem
// var mensagem1 = new Mensagem();
// Console.WriteLine("informe a linguagem: (C#)");
// mensagem1.nome = Console.ReadLine();
// mensagem1.Exibir(mensagem1.nome);

// // Exercício 2: Classe Quadrado
// var quadrado1 = new Quadrado();
// Console.WriteLine("digite o numero:");
// quadrado1.numero = Convert.ToDouble(Console.ReadLine());
// quadrado1.CalcularEImprimirQuadrado(quadrado1.numero);

// // Exercício 3: Classe CalculadoraSimples
// var calculadora1 = new CalculadoraSimples();
// calculadora1.Somar(3,4,5);  

// // Exercício 4: Classe Concatenador
// var concatena1 = new Concatenador();
// concatena1.Concatenar("teste", "ola mundo", "final");

// // Exercício 5: Classe ConversorTemperatura
// var conversor1 = new ConversorTemperatura();
// Console.Clear();
// Console.WriteLine("digite a temperatura em celsius:");
// conversor1.temperaturaCelsius = Convert.ToDouble(Console.ReadLine());
// double temperaturaFahrenheit = conversor1.ConverterParaFahrenheit();
// Console.Clear();
// Console.WriteLine($"temperatura em Fahrenheit {temperaturaFahrenheit.ToString("F3")}");
// Console.ReadKey();

// Exercício 6: Classe Data
var data1 = new Data();
Console.WriteLine("digite o dia");
data1.dia = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("digite o mes");
data1.mes = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("digite o ano");
data1.ano = Convert.ToInt32(Console.ReadLine());
Console.Clear();
data1.ImprimirDataFormatada();

// // Exercício 7: Classe CalculadoraArea
// var area1 = new CalculadoraArea();
// area1.CalcularArea(23);   
// area1.CalcularArea(23,4);   
// area1.CalcularArea(235,5,10);   

// // Exercício 8: Classe Tabuada
// var tabuada1 = new Tabuada();
// Console.WriteLine("digite o numero que voce deseja exibir a tabuada");
// tabuada1.numeroBase = Convert.ToInt32(Console.ReadLine());
// tabuada1.InprimirTabuada();
// // tabuada1.InprimirTabuada(7);