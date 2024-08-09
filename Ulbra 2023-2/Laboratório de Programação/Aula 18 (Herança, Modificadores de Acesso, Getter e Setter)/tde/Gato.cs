public class Gato: Animal 
// COM O :ANIMAL DO LADO DA CLASSE,
// VOU HERDAR OS MÉTODOS E PROPRIEDADES DA CLASSE ANIMAL
{
    public override void EmitirSom()
    {
        Console.WriteLine("O gato emite um som.");
    }

    public override void Andar()
    {
        Console.WriteLine("O gato está andando.");
    }
}