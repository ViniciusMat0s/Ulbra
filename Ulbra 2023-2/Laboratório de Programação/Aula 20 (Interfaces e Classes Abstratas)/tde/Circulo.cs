public class Circulo : Forma //Herdando classe Forma na classe Circulo
{
   public double Raio { get; set; }
    public override double CalcularArea()
    {
        return Math.PI * Math.Pow(Raio, 2); //Calculando a área com a biblioteca Math | //Sobscrevendo para a fórmula do cálculo do retângulo
    }
}