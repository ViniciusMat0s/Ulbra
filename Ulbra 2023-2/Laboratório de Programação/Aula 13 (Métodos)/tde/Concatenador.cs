// Classe: Concatenador
// Métodos: Sobrecargas do método Concatenar()
// Descrição: Crie sobrecargas do método Concatenar como especificado previamente, sem utilizar atributos.

class Concatenador
{
    public void Concatenar(string nome1, string nome2)
    {
        Console.WriteLine("nome " + nome1 + ", e " + nome2 );
    }
    public void Concatenar(string nome1, string nome2, string nome3)
    {
        Console.WriteLine("nome " + nome1 + ", e " + nome2 + ", ultimo valor " + nome3);
    }
}
