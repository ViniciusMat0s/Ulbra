function alo(){
    alert('Alô!')
}

function olaNome(nome){
    alert('Olá ' + nome + '. Seja bem-vindo ao curso.') //Concatenação de strings
}

function saudacao(){
    const nome = document.getElementById('nome').value
    alert(`Boa noite ${nome}.`) //Interpolação de texto
}

function mouseSobre(){
    alert('O mouse está em cima!')
}

function mouseFora(){
    alert('O mouse saiu!')
}

function textoMudou(){
    alert('O texto mudou.')
}

function emFoco(){
    const user = document.getElementById('user')
    user.style.border = '5px green solid'
    user.style.backgroundColor = 'grey'
}

function perdeuFoco(){
    const user = document.getElementById('user')
    user.style.border = '1px black solid'
    user.style.backgroundColor = 'white'
}