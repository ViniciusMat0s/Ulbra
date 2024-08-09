// Classe: CalculadoraArea
// Métodos: Sobrecargas do método CalcularArea()
// Descrição: Crie sobrecargas do método CalcularArea() conforme especificado anteriormente. Não utilize atributos.


class CalculadoraArea
{
    public void CalcularArea(double Quadrado)
    {
        Console.WriteLine($"{Quadrado * Quadrado} metros quadrados");
    }
    public void CalcularArea(double lado1, double lado2)
    {
        Console.WriteLine($"area do retangulo {lado1 * lado2}");
    }
    public void CalcularArea(double lado1, double lado2, double lado3)
    {
        Console.WriteLine($"Area sera {lado1 * lado2 * lado3}");
    }
}