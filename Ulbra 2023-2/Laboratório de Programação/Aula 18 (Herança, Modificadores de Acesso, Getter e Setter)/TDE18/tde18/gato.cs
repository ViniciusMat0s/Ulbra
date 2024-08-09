namespace tde
{
    public class Gato : Animal
{
    public Gato(string nome, int idade) : base(nome, idade, 4) { }

    public override void EmitirSom()
    {
        Console.WriteLine("O gato faz 'miar' (gato goiano).");
        ExibirNumeroDePatas();
    }
}
}