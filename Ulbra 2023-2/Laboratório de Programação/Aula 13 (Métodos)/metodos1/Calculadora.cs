class Calculadora
{
    public int Somar(int n1, int n2)
    {
        int result = n1 + n2;
        return result;
    }
    public void Somar(int n1, int n2, int n3)
    {
        Console.WriteLine(n1 + n2 + n3);
    }
    public void Somar(double d1, double d2)
    {
        Console.WriteLine(d1 + d2);
    }
    public void Somar()
    {
        Console.WriteLine(0+0);
    }
}