<?php

echo "<pre>";

// class Cachorro {
//     public string $nome;
//     public string $raca;

//     public function __construct(string $nome, string $raca) {
//         $this->nome = $nome;
//         $this->raca = $raca;
//     }
// }

// // $dog = new Cachorro(raca: "Pastor Alemão", nome: "Mocotó"); // Invertendo parâmetros
// $dog = new Cachorro('Mocotó', 'Pastor Alemão'); // Ordem padrão
// var_dump($dog);

class Cliente {
    public int $cod;
    public string $nome;
    public string $cpf;

    public function __construct(){
        $this->cod = 1000;
        $this->nome = 'Vinicitto';
        $this->cpf = '000.000.000-00';
    }
}

class Vaga {
    public int $numero;
    public bool $status;
    public DateTime $dataLiberacao;

    public function __construct() {
        $this->numero = 7;
        $this->status = true;
        $this->dataLiberacao = DateTime::createFromFormat('d/m/Y H:i:s', '22/08/2024 21:14:12');
    }
}

class Historico {
    public int $cod;
    public DateTime $dataAtual;
    public DateTime $dataEntrada;
    public DateTime $dataSaida;
    public Vaga $vaga;
    public Cliente $cliente;

    public function __construct() {
        $this->dataAtual = DateTime::createFromFormat('d/m/Y', '22/08/2024');
        $this->dataEntrada = DateTime::createFromFormat('d/m/Y H:i:s', '22/08/2024 21:18:30');
        $this->dataSaida = DateTime::createFromFormat('d/m/Y H:i:s', '22/08/2024 22:18:30');
        $this->vaga = new Vaga();
        $this->cliente = new Cliente();
    }
}

$historico = new Historico();
var_dump($historico);