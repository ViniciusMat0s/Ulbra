public class Retangulo : Forma
{
    public double Largura { get; set; }
    public double Altura { get; set; }
    public override double CalcularArea() //Sobscrevendo para a fórmula do cálculo do retângulo
    {
        return Largura * Altura;
    }
}