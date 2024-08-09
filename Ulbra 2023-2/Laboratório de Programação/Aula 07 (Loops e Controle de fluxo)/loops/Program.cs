// for (int i = 0; i <= 50; i++) {
//     Console.WriteLine(i);
// }

// Console.Write("Digite um número máximo para ser impresso. Digite [0] para sair: ");
// int max = Convert.ToInt32(Console.ReadLine());

// for (int i = 0; i <= max; i++) {
//     Console.WriteLine($"Posição {i}");
// }

// int max = 0;
// do {
//     Console.WriteLine("Insira um número máximo para sua lista ou número [0] para sair.");
//     max = Convert.ToInt32(Console.ReadLine());
//     for (int i = 0; i <= max; i++) {
//         Console.WriteLine($"Posição {i}");
//     }
// } while (max != 0);

// int num = 5;
// while (num > 0) {
//     Console.WriteLine(num);
//     num--;
// }

int numSec = 10;
int palpite;
do {
    Console.Write("Digite um número: ");
    palpite = Convert.ToInt32(Console.ReadLine());
} while (numSec != palpite);
Console.WriteLine("Parabéns, você acertou!");