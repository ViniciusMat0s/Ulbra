// let numero = 0
// while(true){

//     if (numero == 5){
//         break
//     }
//     numero++
//     console.log(numero)
// }

let numero = 0;
while(True){
    numero = prompt("Adivinhe o número que estou pensando.")
    if (numero == 5){
        alert("Parabéns, você acertou!")
        break;
    }else if (numero < 5){
        alert("Você errou, número muito baixo.")
    }else{
        alert("Você errou, número muito alto.")
    }
}