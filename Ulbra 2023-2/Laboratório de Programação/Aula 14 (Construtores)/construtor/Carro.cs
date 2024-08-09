public class Carro
{
    public string? marca;
    public string? modelo;
    public int? ano;

//Construtora
    public Carro()
    {
        marca = "marcaindefinida";
        modelo = "modeloindenifido";
        ano = 2023;
    }

//Definindo as variáveis
    public Carro(string marcaParametro, string modeloParametro, int anoParametro)
    {
        marca = marcaParametro;
        modelo = modeloParametro;
        ano = anoParametro;
    }

// Função
    public void MostrarDetalhes(){
        Console.WriteLine($"Marca: {marca}\nModelo: {modelo}\nAno: {ano}");
    }
}