public class Gato : Animal //Fazendo a classe Gato herdar da classe Animal
{
    public override void FazerSom() //Implementando classe abstrata | OVERRIDE SERVE PARA SOBSCREVER
    {
        Console.WriteLine("O gato miou.");
    }
}