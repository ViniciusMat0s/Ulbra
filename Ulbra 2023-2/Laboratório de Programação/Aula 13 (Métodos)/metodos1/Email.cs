class Email
{
    public void Enviar(string endereco)
    {
        Console.WriteLine($"Endereço: {endereco}");
        Console.WriteLine("Assunto padrão");
    }

    public void Enviar(string endereco, string assunto)
    {
        Console.WriteLine($"Endereço: {endereco}");
        Console.WriteLine($"Assunto {assunto}");
    }

    public void Enviar(string endereco, decimal valor)
    {
        Console.WriteLine($"Endereço: {endereco}");
        Console.WriteLine($"Proposta comercial: {valor}");
    }

    public string Enviar(string endereco, string nome, int idade)
    {
        return endereco + nome + idade;
    }
}