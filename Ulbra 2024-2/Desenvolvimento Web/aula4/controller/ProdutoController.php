<?php

require_once("../model/Produto.php");

class ProdutoController {
    public function cadastrar() {
        $produto = new Produto('Descricao', 2.50);

        $pagina = require_once("../view/cadastrar.php");
        //Se a minha requisição for um post
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $produto = new Produto($_POST["descricao"], $_POST["preco"]);
            $produto->cadastrar();
        }
    }

    public function listar() {
        $listaArray = [
            [
                "descricao" => "Produto X",
                "preco" => 2.50
            ],
            [
                "descricao" => "Produto Y",
                "preco" => 3.50
            ]
        ];
        
        $pagina = require_once("../view/listar.php");
        return $pagina;
    }
}


$controller = new ProdutoController();
$controller->cadastrar();