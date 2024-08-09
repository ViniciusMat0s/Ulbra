

// Classe: CalculadoraSimples
// Métodos: Sobrecargas do método Somar(int a, int b) e Somar(int a, int b, int c)
// Descrição: Crie métodos que retornem a soma dos parâmetros passados. Não utilize atributos.

class CalculadoraSimples
{
    public void Somar(int a ,int b)
    {
        int calculo = a + b;
        Console.WriteLine($"soma de {a} + {b} = {calculo}.");
    }
    public void Somar(int a ,int b, int c)
    {
        int calculo = a + b + c;
        Console.WriteLine($"soma de {a} + {b} + {c} = {calculo}");
    }
}