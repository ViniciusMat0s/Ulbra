public class ArmazBanco : IRepositorioDados
{
    public string Carregar()
    {
        return "Carregando Dados";
    }
    public void Salvar(string dados);
    {
        Console.WriteLine("Salvando no banco de dados.");
    }
}