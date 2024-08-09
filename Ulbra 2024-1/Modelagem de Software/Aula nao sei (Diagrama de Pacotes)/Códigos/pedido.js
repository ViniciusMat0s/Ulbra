export const Pedido = function() {
    class Pedido {
        constructor(numero, total, cliente){
            this.numero = numero
            this.total = total
            this.cliente = cliente
        }
    
        salvar() {
            let pedido = {
                numero: this.numero,
                total: this.total,
                cliente: this.cliente
            }
            return pedido
        }
    
        atualizar() {
            let pedido = {
                numero: this.numero,
                total: this.total,
                cliente: this.cliente
            }
        }
    
        cancelar() {
            let pedido = {
                numero: this.numero,
                total: this.total,
                cliente: this.cliente
            }
        }
    
        adicionarItem() {
            let pedido = {
                numero: this.numero,
                total: this.total,
                cliente: this.cliente
            }
        }
    }
    
    class ItemPedido {
        constructor(valor, quantidade, produto){
            this.valor = valor
            this.quantidade = quantidade
            this.produto = produto
        }
    
        salvar(){
            let item = {
                valor: this.valor,
                quantidade: this.quantidade,
                produto: this.produto
            }
        }
    
        calcularTotal(){
            return this.quantidade + this.valor
        }
    }
    
    class Produto {
        constructor(nome, valor, descricao){
            this.nome = nome
            this.valor = valor
            this.descricao = descricao
        }
    
        salvar(){
            let produto = {
                nome: this.nome,
                valor: this.valor,
                descricao: this.descricao
            }
        }
    }
    return produto
}

return {Pedido, ItemPedido, Produto}