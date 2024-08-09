public class ArmazArquivo : IRepositorioDados
{
    public class Carregar()
    {
        return "Carregando em arquivo.";
    }

    public void Salvar(string dados)
    {
        Console.WriteLine("Salvando em arquivo")
    }
}