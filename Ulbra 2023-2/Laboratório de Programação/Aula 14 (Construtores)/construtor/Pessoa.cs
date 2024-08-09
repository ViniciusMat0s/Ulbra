// ATRIBUTOS DA CLASSE
class Pessoa 
{
    public string? primeiroNome;
    public string? ultimoNome;
    public string? CPF;

// MÉTODO CONSTRUTOR
    public Pessoa(string primeiro, string ultimo) 
    {
        primeiroNome = primeiro;
        ultimoNome = ultimo;
    }
// MÉTODO
    public void MostrarNome() 
    {
        Console.WriteLine($"Primeiro nome: {this.primeiroNome}\nÚltimo nome: {ultimoNome}");
    }
    public string SetarCPF(string CPF)
    {
        this.CPF = CPF;
        return this.CPF;
    }
}