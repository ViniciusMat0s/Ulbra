function inserir(){
    const tarefa = document.getElementById('tarefa').value
    const li = document.createElement('li')
    li.textContent = tarefa
    //fazer o if para ver se tá vazio

    const btn = document.createElement('button')
    btn.textContent = 'Remover' //colocar imagem da lixeirinha
    btn.style.backgroundImage = 'url da imagem de lixeirinha'
    btn.type = 'button'
    btn.style.marginLeft = '20px'
    btn.addEventListener('click', function(){li.remove()})

    li.appendChild(btn)

    const ol = document.getElementById('pendentes')
    ol.appendChild(li)
    //fazer o focus igual no outro
}