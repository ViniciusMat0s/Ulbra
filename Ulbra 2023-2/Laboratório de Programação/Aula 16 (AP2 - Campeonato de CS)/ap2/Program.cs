Jogador j1 = new Jogador();
j1.Nome = "Gabriel Toledo de Alcântara Sguario";
j1.Nickname = "FalleN";

Jogador j2 = new Jogador();
j2.Nome = "Marcelo Cespedes";
j2.Nickname = "Chelo";

Jogador j3 = new Jogador();
j3.Nome = "Kaike Silva Cerato";
j3.Nickname = "KSCERATO";

Jogador j4 = new Jogador();
j4.Nome = "Andrei Felipe Piovezan Machado";
j4.Nickname = "ArT";

Jogador j5 = new Jogador();
j5.Nome = "Yuri Gomes dos Santos Boian";
j5.Nickname = "Yuurih";

Jogador j6 = new Jogador();
j6.Nome = "Kaiky Santos";
j6.Nickname = "noway";

Jogador j7 = new Jogador();
j7.Nome = "Henrique Teles Ferreira da Fonseca";
j7.Nickname = "HEN1";

Jogador j8 = new Jogador();
j8.Nome = "João Cabral Vasconcellos";
j8.Nickname = "Felps";

Jogador j9 = new Jogador();
j9.Nome = "Vinicius de Almeida Figueiredo";
j9.Nickname = "VINI";

Jogador j10 = new Jogador();
j10.Nome = "Ricardo de Souza Prass";
j10.Nickname = "Boltz";

Equipe e1 = new Equipe();
e1.NomeEquipe = "Furia";
e1.AdicionarJogador(j1);
e1.AdicionarJogador(j2);
e1.AdicionarJogador(j3);
e1.AdicionarJogador(j4);
e1.AdicionarJogador(j5);

Equipe e2 = new Equipe();
e2.NomeEquipe = "Imperial";
e2.AdicionarJogador(j6);
e2.AdicionarJogador(j7);
e2.AdicionarJogador(j8);
e2.AdicionarJogador(j9);
e2.AdicionarJogador(j10);

string continuar;

do {
    Campeonato Campeonato = new Campeonato();
    Campeonato.Equipe1 = e1;
    Campeonato.Equipe2 = e2;

    Campeonato.Equipe1.j1.Jogar();
    Campeonato.Equipe1.j2.Jogar();
    Campeonato.Equipe1.j3.Jogar();
    Campeonato.Equipe1.j4.Jogar();
    Campeonato.Equipe1.j5.Jogar();

    Campeonato.Equipe2.j1.Jogar();
    Campeonato.Equipe2.j2.Jogar();
    Campeonato.Equipe2.j3.Jogar();
    Campeonato.Equipe2.j4.Jogar();
    Campeonato.Equipe2.j5.Jogar();

    Campeonato.Classificacao();

    Console.WriteLine("\nDeseja simular um novo mapa? (s/n)\n");
    continuar = Console.ReadLine().ToLower();

} while (continuar == "s");
Console.WriteLine("\nFinalizando campeonato.\n");