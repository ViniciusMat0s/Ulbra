class Conclusao2
{
    static void Main()
    {
        bool opcao = true;

        Console.WriteLine("Olá, irei realizar a soma dos números que você deseja até onde você quiser");

        Console.WriteLine("Digite o valor inicial: ");
        float.TryParse(Console.ReadLine(), out float inicial);

        while(opcao == true)
        {
            Console.WriteLine("Digite o número que você deseja somar ao número inicial: ");
            float.TryParse(Console.ReadLine(), out float n1);
            inicial = inicial + n1;
            Console.WriteLine("A soma até o momento é: {0}", inicial);
            Console.WriteLine("Digite [1] para sair do programa ou [2] para continuar: ");
            int.TryParse(Console.ReadLine(), out int saida);
            switch (saida)
            {
                case 1:
                    Console.WriteLine("Saindo do Programa.");
                    opcao = false;
                    break;
                case 2:
                    Console.WriteLine("Continuando a soma.");
                    break;
                default:
                    Console.WriteLine("Opção inválida, retornando à soma.");
                    break;

            }
        }
    }
}