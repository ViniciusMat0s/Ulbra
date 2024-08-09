// Classe: Mensagem
// Método: Exibir()
// Descrição: Crie um método que imprima a mensagem “Bem-vindo ao C#” sem receber parâmetros e sem utilizar atributos.

class Mensagem
{
    public string? nome;
    public void Exibir(string nome)
    {
        Console.WriteLine($"Bem-vindo ao {nome}");
    }
}