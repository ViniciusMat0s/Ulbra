// Classe: Data
// Atributos: dia, mes, ano
// Método: ImprimirDataFormatada()
// Descrição: Crie um método que imprima a data formatada armazenada nos atributos.

class Data
{
    public int dia;
    public int mes;
    public int ano;
    public void ImprimirDataFormatada()
    {
        Console.WriteLine($"data: {dia}/{mes}/{ano}");
    }
}