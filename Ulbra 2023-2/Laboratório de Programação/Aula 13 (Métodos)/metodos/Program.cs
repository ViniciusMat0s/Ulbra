Pessoa p1 = new Pessoa();
Console.WriteLine("Informe o nome da pessoa 1: ");
p1.nome = Console.ReadLine();
Console.WriteLine("Informe a idade da pessoa 1: ");
p1.idade = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Informe a cidade natal da pessoa 1: ");
p1.cidadeNatal = Console.ReadLine();
p1.MostrarInformacoes();

Pessoa p2 = new Pessoa();
Console.WriteLine("Informe o nome da pessoa 2: ");
p2.nome = Console.ReadLine();
Console.WriteLine("Informe a idade da pessoa 2: ");
p2.idade = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Informe a cidade natal da pessoa 2: ");
p2.cidadeNatal = Console.ReadLine();
p2.MostrarInformacoes();