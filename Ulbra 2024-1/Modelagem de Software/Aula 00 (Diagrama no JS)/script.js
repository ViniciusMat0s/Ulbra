class Cliente {
    constructor(nome, endereco, telefone){
        this.nome = nome
        this.endereco = endereco
        this.telefone = telefone
    }

    salvar() {
        let cliente = {
            nome: this.nome,
            endereco: this.endereco,
            telefone: this.telefone
        }
        return cliente
    }

    alterar(){
        let cliente = {
            nome: this.nome,
            endereco: this.endereco,
            telefone: this.telefone
        }
        return cliente
    }

    excluir(){
        try {
            return "Confirmado"
        } catch (error) {
            return "Erro"
        }
    }
}

const cliente = new Cliente(Vini, "Av. André Pusti", 5198954406)
console.log(cliente.salvar())