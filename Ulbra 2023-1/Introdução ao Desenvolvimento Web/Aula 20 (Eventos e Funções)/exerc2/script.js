function calcular(){
    const ap1 = Number(document.getElementById('ap1').value)
    const ap2 = Number(document.getElementById('ap2').value)
    const as = Number(document.getElementById('as').value)
    let nota = ap1 + ap2 + as
    if(nota >= 6){
        document.getElementById('nota').innerHTML = 'Nota ' + nota + '. Aprovado. Parabéns.'
    }else{
        document.getElementById('nota').innerHTML = 'Nota ' + nota + '. Reprovado. Reforce seus estudos para a realização da AF.'
    }
}

function verificaAp1(){
    const ap1 = document.getElementById('ap1').value
    if(ap1 < 0 || ap1 > 1.5){
        document.getElementById('ap1').value = ''
        alert('Nota inválida. (Digite a nota entre 0 e 1.5')
        document.getElementById('ap1').focus()
    }
}

function verificaAp2(){
    const ap2 = document.getElementById('ap2').value
    if(ap2 < 0 || ap2 > 2.5){
        document.getElementById('ap2').value = ''
        alert('Nota inválida. (Digite a nota entre 0 e 2.5')
        document.getElementById('ap2').focus()
    }
}

function verificaAs(){
    const as = document.getElementById('as').value
    if(as < 0 || as > 6.0){
        document.getElementById('as').value = ''
        alert('Nota inválida. (Digite a nota entre 0 e 6.0')
        document.getElementById('as').focus()
    }
}