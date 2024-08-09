namespace tde
{
    public class Cachorro : Animal
{
    public Cachorro(string nome, int idade) : base(nome, idade, 4) { }

    public override void EmitirSom()
    {
        Console.WriteLine("O cachorro faz 'Au, Au'.");
        ExibirNumeroDePatas();
    }
}
}
// Sobrescreva o método EmitirSom() para que o Cachorro emita um latido e o Gato um miado.