public class Livro : ItemBiblioteca
{
    public string? Autor;
    public Livro (int id, string titulo, string autor)
    {
        Id = id;
        Titulo = titulo;
        Autor = autor;
    }
    public void MostrarDescricaoInterna()
    {
        Console.WriteLine(DescricaoInterna);
    }
}