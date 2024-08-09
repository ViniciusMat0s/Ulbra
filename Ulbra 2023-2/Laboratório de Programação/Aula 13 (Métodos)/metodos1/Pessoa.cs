class Pessoa
{
    public void Caminhar()
    {
        Console.WriteLine("Pessoa caminhando.");
    }
    public void MostrarInformacoes()
    {
        Console.WriteLine($"Nome: {nome}\nIdade: {idade}\n Cidade Natal: {cidadeNatal}");
    }
    public string? nome = "Vinícius";
    public int? idade = 19;
    public string? cidadeNatal = "Capão da Canoa";
}