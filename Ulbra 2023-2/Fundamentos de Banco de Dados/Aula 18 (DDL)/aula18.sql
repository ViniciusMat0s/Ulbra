--Comentário de uma linha

/* Comentário
de
mais
de
uma
linha
*/

/*
Modelo lógico para exemplo

Clientes(Id int Not Null pk, Nome char(100));
Enderecos(Id int Not Null pk, Rua varchar(100) Numero int, Bairro varchar(50), Cidade varchar(50), Estado char(2), Id_cliente int Not Null references Clientes (id));
*/

CREATE TABLE Clientes
(
    Id int Not Null PRIMARY KEY,
    Nome char(100)
);

CREATE TABLE Enderecos
(
    Id int Not Nul PRIMARY KEY,
    Rua varchar(100),
    Numero int,
    Bairro varchar(50),
    Cidade varchar(50),
    Estado char(2);
    Id_cliente int Not Null
        Constraint Clientes_Endereços
            FOREIGN KEY (Id_cliente) references Clientes (Id)
);