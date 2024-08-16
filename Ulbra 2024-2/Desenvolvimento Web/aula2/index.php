<?php //tag para definir a linguagem

$numero1 = 10; //variável começa com $
$numero2 = 50;

$soma = $numero1 + $numero2;
$subtracao = $numero1 - $numero2;
$multiplicacao = $numero1 * $numero2;
$divisao = $numero1 / $numero2;

//echo é o print
echo "O resultado da soma é: $soma";
echo "<br>O resultado da subtração é: $subtracao";
echo "<br>O resultado da multiplicação é: $multiplicacao";
echo "<br>O resultado da divisão é: $divisao";

$nome = "Vini";
$sobrenome = "Matos";

$nomeCompleto = "<br>Meu nome é $nome $sobrenome";
echo $nomeCompleto . "<br>";

$array = ["Ayrton", "Pelé", "Renato"];

echo "<pre>"; // habilita formatação (\n, \t)
var_dump($array); //printar o array

krsort($array); //inveter ordem
var_dump($array);

$array = array_flip($array); //inverter item e valor
var_dump($array);

$dados = [ //definindo item e valor de array
    "nome" => "Vini",
    "idade" => 20
];

var_dump($dados);

for ($i=1; $i <= 10; $i++) { 
    echo "\n$i";
}

foreach ($array as $key => $value) {
    echo "\nChave: $key, Valor: $value";
}

$count = 0;
do {
    echo "\nExecutou no do while $count";
    $count++;
} while ($count <= 10);

$count = 0;
while ($count <= 10) {
    echo "\nExecutou no while $count";
    $count++;
}