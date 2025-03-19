drop database mercado;
create database mercado;
use mercado;

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(15),
    senha VARCHAR(255) NOT NULL,
    perm char(1),
    foto VARCHAR(255),
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE
);

create table caixa(
	id_caixa int primary key auto_increment,
    id_user int,
    foreign key (id_user) references usuarios(id_usuario),
    saldo_ini float,
    saldo_atual float,
    saldo_final float,
    data_abertura DATETIME,
    data_fechar DATETIME,
	valor_sangria float,
    valor_suprimento float,
    status char(1) default "0"
);

CREATE TABLE categorias (
    id_categorias INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL UNIQUE,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE estoque (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL UNIQUE,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    categoria INT NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    imagem varchar(100),
    FOREIGN KEY (categoria) REFERENCES categorias(id_categorias) ON DELETE RESTRICT
);

create table formapagamento(
	id_forma_pagamento int primary key auto_increment,
    forma_pagamento varchar(50) unique not null
);
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    data_venda DATETIME DEFAULT current_date,
    valor_total DECIMAL(10, 2) NOT NULL,
	id_forma_pagamento int,
    foreign key (id_forma_pagamento) references formapagamento(id_forma_pagamento),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE RESTRICT
);

CREATE TABLE itens_venda (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) AS (quantidade * preco_unitario) STORED,
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda) ON DELETE CASCADE,
    FOREIGN KEY (id_produto) REFERENCES estoque(id_produto) ON DELETE RESTRICT
);

INSERT INTO usuarios (nome, email, cpf, telefone, senha, perm, foto, ativo) 
VALUES ('Admin', 'admin@email.com', '000.000.000-00', '(00) 00000-0000', SHA2('admin', 256), "1", NULL, true);

INSERT INTO formapagamento (forma_pagamento) 
VALUES 
    ("Pix"), 
    ("Débito"), 
    ("Crédito"), 
    ("Dinheiro");
select * from categorias;
select * from formapagamento;
select * from estoque;
select * from usuarios;
select * from vendas;
select * from itens_venda;
select * from caixa;