var banco = new ArmazBanco();

banco.Carregar();
banco.Salvar("Dados");

var arquivo = new ArmazArquivo();

arquivo.Carregar();
arquivo.Salvar("Arquivo");