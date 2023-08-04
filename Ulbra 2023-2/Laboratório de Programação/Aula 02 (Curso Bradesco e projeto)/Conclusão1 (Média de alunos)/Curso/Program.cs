class Conclusao
{
    static void Main()
    {
        float media = 0;

        Console.WriteLine("Olá, seja bem-vindo ao programa de cálculo de média!");

        Console.WriteLine("Irei auxiliá-lo a calcular a média de seu aluno!");

        Console.WriteLine("Digite a nota da AP1: ");
        int.TryParse(Console.ReadLine(), out int nota1);

        Console.WriteLine("Digite a nota da AP2: ");
        int.TryParse(Console.ReadLine(), out int nota2);

        Console.WriteLine("Digite a nota da AS: ");
        int.TryParse(Console.ReadLine(), out int nota3);

        media = (nota1 + nota2 + nota3) / 3;

        Console.WriteLine("A média do aluno é: {0}", media);

        if (media < 7)
        {
            Console.WriteLine("O aluno deve realizar a AF.");
        }
        else
        {
            Console.WriteLine("Aluno aprovado.");
        }
    }
}