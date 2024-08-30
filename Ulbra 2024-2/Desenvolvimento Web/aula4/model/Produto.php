<?php

class Produto {
    public string $descricao;
    public float $preco;

    public function __construct(string $descricao, float $preco) {
        $this->descricao = $descricao;
        $this->preco = $preco;
    }

    public function cadastrar() {
        echo "O produto {$this->descricao} com o valor {$this->preco} está pronto para salvar no Banco de Dados.";
    }

    public function listar() {
        echo "Buscando no banco de dados";
    }

}