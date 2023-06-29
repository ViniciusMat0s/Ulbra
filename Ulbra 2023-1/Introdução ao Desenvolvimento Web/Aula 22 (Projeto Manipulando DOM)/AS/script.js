function inserir(){
    const tarefa = document.getElementById('tarefa').value
    const li = document.createElement('li')
    li.textContent = tarefa

    const remover = document.createElement('button')
    remover.textContent = 'Remover'
    remover.type = 'button'
    remover.style.marginLeft = '20px'
    remover.addEventListener('click', function(){li.remove()})

    const concluida = document.createElement('button')
    concluida.textContent = 'Concluir tarefa'
    concluida.type = 'button'
    concluida.style.marginLeft = '20px'
    concluida.addEventListener('click', function() {
        const listacompletos = document.getElementById('concluidas');
        listacompletos.appendChild(li);
        li.removeChild(concluida);
    });

    li.appendChild(remover)
    li.appendChild(concluida)

    const ul = document.getElementById('pendentes')
    ul.appendChild(li)
}