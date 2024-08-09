public abstract class ItemBiblioteca // Criando classe abstrata
{
    public int Id { get; set; } // Criando propriedade Id
    public string? Titulo { get; set; } // Criando propriedade Titulo
    protected string? DescricaoInterna { get; set; } // Criando propriedade protegida

    public ItemBiblioteca(int id, string titulo)
    {
        Id = id;
        Titulo = titulo;
        DescricaoInterna = "Descrição interna não pode ser divulgada";
    }
}
