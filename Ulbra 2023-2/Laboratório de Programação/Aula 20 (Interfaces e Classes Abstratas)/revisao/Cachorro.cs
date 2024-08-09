public class Cachorro : Animal //Fazendo a classe Cachorro herdar Animal
{
    public override void FazerSom() //Implementando classe abstrata
    {
        Console.WriteLine("O cachorro latiu.");
    }
}