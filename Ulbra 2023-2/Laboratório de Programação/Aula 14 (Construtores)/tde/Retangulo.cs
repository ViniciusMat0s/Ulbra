// Construtores Múltiplos:
// Crie uma classe Retângulo com propriedades Largura e Altura.
// Crie dois construtores: um que aceite ambos Largura e Altura e outro que inicialize o retângulo como um quadrado, 
// aceitando apenas um parâmetro para ambos os lados.

class Retangulo
{
    public double? Largura;
    public double? Altura;

    public Retangulo(double largura, double altura)
    {
        this.Largura = largura;
        this.Altura = altura;
    }
    public Retangulo(double lado)
    {
        Altura = Largura = lado;
    }
}