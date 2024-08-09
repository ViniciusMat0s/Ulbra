Calculadora calc = new Calculadora();
int soma = calc.Somar(2, 4);
calc.Somar(3, 4, 6);
Console.WriteLine(soma);

Email email1 = new Email();
email1.Enviar("Capão da Canoa");
email1.Enviar("Capão da Canoa ", " Aula de hoje");
email1.Enviar("Capão da Canoa", 34m);
email1.Enviar("Capão da Canoa ", "Vinícius ", 19);
string resultado = email1.Enviar("Capão da Canoa", "Vinícius", 19);
Console.WriteLine(resultado);