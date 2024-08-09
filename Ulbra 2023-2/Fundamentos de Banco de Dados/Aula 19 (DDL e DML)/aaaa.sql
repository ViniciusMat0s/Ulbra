INSERT INTO Categorias (Codigo, Nome)
VALUES (123, 'aaaa')

INSERT INTO Produtos (Codigo, Descricao, Data_Cadastro, Valor_Unitario, Cod_Cat)
Values (123, 'aaaa', '2023/11/13', 123123, 321)

insert into Fornecedores (Codigo, Nome)
Values (123, 'Aaaaaaa')

--INSERINDO UMA TUPLA NA TABELA

INSERT INTO Pedidos (Quantidade, Valor_Unitario, Data, Cod_Fornec, Prod_Cod)	
values (10, 10, '2023/11/13', 1237289321, 321)

select Codigo, Nome from Categorias