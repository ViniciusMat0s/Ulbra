// Classe: Tabuada
// Atributos: numeroBase
// Método: ImprimirTabuada()
// Descrição: Crie um método que imprima a tabuada do numeroBase.

class Tabuada
{
    public int numeroBase;
    public void InprimirTabuada()
    {
        Console.Clear();
        for (int i = 0; i <= 10; i++)
        {
            Console.WriteLine($"{numeroBase} x {i} = {numeroBase * i}");
        }
        Console.ReadKey();
    }
    public void InprimirTabuada(int num)
    {
        Console.Clear();
        for (int i = 0; i <= 10; i++)
        {
            Console.WriteLine($"{num} x {i} = {num * i}");
        }
        Console.ReadKey();
    }
}