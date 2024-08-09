// Construtor Básico:
// Crie uma classe Pessoa com propriedades Nome e Idade.
// Crie um construtor para inicializar ambas as propriedades.
// Instancie um objeto da classe Pessoa e imprima as propriedades.
class Pessoa
{
    public string? Nome;
    public int? Idade;

    public Pessoa(string nome, int idade)
    {
        Nome = nome;
        Idade = idade;
    }

    public void MostrarInfo()
    {
        Console.WriteLine($"Nome: {Nome}\nIdade: {Idade}");
    }
}