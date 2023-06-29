function inserir(){
    const tarefa = document.getElementById('tarefa').value
    const li = document.createElement('li')
    li.textContent = tarefa
    //fazer o if para ver se tá vazio

    const remover = document.createElement('button')
    remover.textContent = 'Remover' //colocar imagem da lixeirinha
    remover.style.backgroundImage = 'url da imagem de lixeirinha'
    remover.type = 'button'
    remover.style.marginLeft = '20px'
    remover.addEventListener('click', function(){li.remove()})

    const concluir = document.createElement('button')
    concluir.textContent = 'Concluída' //colocar imagem da lixeirinha
    concluir.style.backgroundImage = 'url da imagem de lixeirinha'
    concluir.type = 'button'
    concluir.style.marginLeft = '20px'
    concluir.addEventListener('click', function(){li.add()})

    li.appendChild(remover)
    li.appendChild(concluir)

    const ol = document.getElementById('pendentes', 'concluidas')
    ol.appendChild(li)
    //fazer o focus igual no outro
}