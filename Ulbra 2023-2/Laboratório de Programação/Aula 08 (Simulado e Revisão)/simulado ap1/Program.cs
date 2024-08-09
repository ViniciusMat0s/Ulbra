string continuar;
do {
    //Coletando os dados:
    Console.Write("Digite o nome do aluno (sem acentuação): ");
    string nome = Console.ReadLine();
    Console.Write("\nDigite a primeira nota do aluno: ");
    double nota1 = Convert.ToDouble(Console.ReadLine());
    Console.Write("Digite a segunda nota do aluno: ");
    double nota2 = Convert.ToDouble(Console.ReadLine());
    Console.Write("Digite a terceira nota do aluno: ");
    double nota3 = Convert.ToDouble(Console.ReadLine());

    //Calculando média
    double media = (nota1 + nota2 + nota3) / 3;

    string status;
    if (media >= 7) {
        status = "Aprovado";
    }
    else {
        status = "Reprovado";
    }
    //Relatório
    Console.WriteLine("\n =-=-=-=-=-=-=-= Desempenho =-=-=-=-=-=-=-=");
    Console.WriteLine($"Nome do aluno: {nome}\n");
    Console.WriteLine($"Notas:\nPrimeira avaliação: {nota1}\nSegunda avaliação: {nota2}\nTerceira avaliação: {nota3}");
    Console.WriteLine("\nMedia final: " + media);
    Console.WriteLine("Resultado: " + status);

    //Verificação de continuação.
    Console.WriteLine("Deseja gerar um novo relatório? (s/n)");
    continuar = Console.ReadLine().ToLower();

} while (continuar == "s");
Console.WriteLine("Encerrando programa.");