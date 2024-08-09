namespace tde
{
    public class Animal
    {
        protected int NumPatas;

        public Animal(string nome, int idade, int numPatas)
        {
            Nome = nome;
            Idade = idade;
            NumPatas = numPatas;
        }

        public string Nome { get; set; }
        public int Idade { get; set; }

        protected void ExibirNumeroDePatas()
        {
            Console.WriteLine($"O bichinho tem {NumPatas} patas.");
        }

        public virtual void EmitirSom()
        {
            Console.WriteLine("O animal faz sons.");
            ExibirNumeroDePatas();
        }
    }
}