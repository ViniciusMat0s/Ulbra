class Jogador
{
    public string? Nome;
    public string? Nickname;
    public int Pontos = 0;

    public int Jogar(){
        Random random = new Random();
        int numeroAleatorio = random.Next(100);
        Pontos = Pontos + numeroAleatorio;
        return Pontos;
    }
}