function somar(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
    if(num1 != '' && num2 != ''){
        let soma = num1 + num2
        document.getElementById('result').innerHTML = 'Resultado: ' + soma  
    }else{
        alert('Preencha todos os campos!')
    }
}

function subtrair(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
    let subtracao = num1 - num2
    document.getElementById('result').innerHTML = 'Resultado: ' + subtracao
}

function multiplicar(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
    let multiplicacao = num1 * num2
    document.getElementById('result').innerHTML = 'Resultado: ' + multiplicacao
}

function dividir(){
    const num1 = Number(document.getElementById('num1').value)
    const num2 = Number(document.getElementById('num2').value)
    if(num1 != '0' && num2 != '0'){
        let divisao = num1 / num2
        document.getElementById('result').innerHTML = 'Resultado: ' + divisao
    }else{
        alert('O número 0 não é válido para a divisão.')
    }
}

function limpar(){
    document.getElementById('num1').value = ''
    document.getElementById('num2').value = ''
    document.getElementById('result').innerHTML = 'Resultado:'
}