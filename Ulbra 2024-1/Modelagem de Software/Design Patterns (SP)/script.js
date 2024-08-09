function Dono(nome)
{
    this.nome = nome
    this.cargo = "Dono"
}

function Recepcionista(nome)
{
    this.nome = nome
    this.cargo = "Recepcionista"
}

function Camareira(nome)
{
    this.nome = nome
    this.cargo = "Camareira"
}

function RH()
{
    this.criar = (nome, cargo) => {
        switch(cargo)
        {
            case 1:
                return new Dono(nome)
            case 2:
                return new Recepcionista(nome)
            case 3:
                return new Camareira(nome)
        }
    }
}

function apresentacao()
{
    console.log("Olá, sou " + this.nome + ", "+ this.cargo + " do Hotel Matos!")
}

const rh = new RH()
const funcionarios = []

funcionarios.push(rh.criar("Vinícius Matos", 2))
funcionarios.push(rh.criar("Jair Fernando", 2))
funcionarios.push(rh.criar("Eloí de Souza", 3))
funcionarios.push(rh.criar("Joelson Matos", 1))

funcionarios.forEach( emp => {
    apresentacao.call(emp)
})