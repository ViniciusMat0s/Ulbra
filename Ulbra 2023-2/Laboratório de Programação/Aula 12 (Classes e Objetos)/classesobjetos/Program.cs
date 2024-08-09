
// Pessoa p1 = new Pessoa();
// p1.nome = "Vini";
// p1.idade = 19;
// p1.sexo = "Masculino";

// Console.Write($"Nome: {p1.nome}, Idade: {p1.idade}, Sexo: {p1.sexo}");

// Pessoa p2 = new Pessoa();
// p2 = p1;
// // p2.nome = "Brunna";
// // p2.idade = 18;
// // p2.sexo = "Feminino";

// Console.Write($"Nome: {p2.nome}, Idade: {p2.idade}, Sexo: {p2.sexo}");
// class Pessoa
// {
//     public string? nome;
//     public int idade;
//     public string? sexo;
// }

// Bis bis1 = new Bis();
// bis1.sabor = "Chocolate Branco";
// bis1.tamanho = 15.6;
// bis1.validade = DateTime.Now;

// Console.Write($"Sabor: {bis1.sabor}, Tamanho: {bis1.tamanho}, Validade: {bis1.validade}");

// Bis bis2 = new Bis();
// bis2.sabor = "Morango";
// bis2.tamanho = 21.5;
// bis2.validade = DateTime.Now;
// class Bis
// {
//     public string? sabor;
//     public double? tamanho;
//     public DateTime? validade;
// }

Carro c1 = new Carro();
c1.marca = "GM";
c1.modelo = "Tracker";
c1.cor = "Azul marinho";
c1.ano = 2022;

Carro c2 = new Carro();
c2.marca = "Toyota";
c1.modelo = "Corolla GR";
c2.cor = "Branco";
c2.ano = 2023;
class Carro
{
    public string? marca;
    public string? modelo;
    public string? cor;
    public int? ano;
}