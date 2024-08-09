// Modelagem de Livros
class Aluno {
    var nome;
    var matricula;
    var idade;
    var curso;

    function mostrarInformacoes(nome, matricula, idade, curso)
    {
        console.log("Nome:" + this.nome)
        console.log("Matrícula: " + this.matricula)
        console.log("Idade: " + this.idade)
        console.log("Curso: " + this.curso)
    }
}

//Modelagem de Praia
class Praia {
    var nome;
    var localizacao;
    var temperaturaAgua;
    var tipoAreia;

    function informacoesPraia(nome, localizacao, temperaturaAgua, tipoAreia)
    {
        console.log("Nome: " + this.nome)
        console.log("Localização: " + this.localizacao)
        console.log("Temperatura da água: " + this.temperaturaAgua)
        console.log("Tipo da Areia: " + this.tipoAreia)
    }
}

//Sistema de Reservas de Voos
class Voo {
    var companhiaAerea;
    var origem;
    var destino;
    var dataPartida;
    var precoPassagem;

    function informacoesVoo(companhiaAerea, origem, destino, dataPartida, precoPassagem)
    {
        console.log("Companhia Aérea: " + this.companhiaAerea)
        console.log("Origem: " + this.origem)
        console.log("Destino: " + this.destino)
        console.log("Data de Partida: " + this.dataPartida)
        console.log("Preço da passagem: " + this.precoPassagem)
    }
}