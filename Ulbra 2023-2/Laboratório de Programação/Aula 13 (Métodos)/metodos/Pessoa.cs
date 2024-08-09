class Pessoa
{
    public string? nome = "Vinícius";
    public int? idade = 19;
    public string? cidadeNatal = "Capão da Canoa";
    public void MostrarInformacoes()
    {
        Console.WriteLine($"{nome}, {idade} e {cidadeNatal}");
    }
}