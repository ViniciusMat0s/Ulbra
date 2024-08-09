export const Pagamento = function() {
    class Pagamento {
        constructor(valor, status){
            this.valor = valor
            this.status = status
        }
    
        salvar(){
            let produto = {
                valor: this.valor,
                status: this.status
            }
        }
    }
    
    class Cliente {
        constructor(nome){
            this.nome = nome
        }
    
        salvar(){
            let produto = {
                nome: this.nome
            }
            return cliente
        }
    }    
}