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

create table mov_caixa(
	id int primary key auto_increment,
    id_user int,
    foreign key (id_user) references usuarios(id_usuario),
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao varchar(25),
    formapagamento varchar(15),
    obs text,
    valor float
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
    tipo_valor char(1),
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
    id_produto_pedido INT NOT NULL,
    quantidade_pedido INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) AS (quantidade_pedido * preco_unitario) STORED,
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda) ON DELETE CASCADE,
    FOREIGN KEY (id_produto_pedido) REFERENCES estoque(id_produto) ON DELETE RESTRICT
);

INSERT INTO usuarios (nome, email, cpf, telefone, senha, perm, foto, ativo) 
VALUES ('Admin', 'admin@email.com', '000.000.000-00', '(00) 00000-0000', SHA2('admin', 256), "1", NULL, true);

INSERT INTO formapagamento (forma_pagamento) 
VALUES 
    ("Pix"), 
    ("Débito"), 
    ("Crédito"), 
    ("Dinheiro");

-- Inserção de várias categorias na tabela categorias
INSERT INTO categorias (nome_categoria) VALUES
('Alimentos Básicos'),
('Higiene Pessoal'),
('Limpeza Doméstica'),
('Bebidas Alcoólicas'),
('Bebidas Não Alcoólicas'),
('Laticínios'),
('Carnes e Peixes'),
('Padaria'),
('Frutas e Verduras'),
('Congelados'),
('Doces e Sobremesas'),
('Snacks e Salgadinhos'),
('Produtos de Bebê'),
('Pet Shop'),
('Utilidades Domésticas');

-- Inserção de 100 produtos na tabela estoque
INSERT INTO estoque (nome_produto, preco, quantidade, categoria, tipo_valor, data_criacao, imagem) VALUES
-- 1. Alimentos Básicos (ID 1)
('Arroz Branco 5kg', 25.90, 50, 1, '0', CURRENT_TIMESTAMP, NULL),
('Feijão Preto 1kg', 8.50, 40, 1, '0', CURRENT_TIMESTAMP, NULL),
('Macarrão Espaguete 500g', 4.20, 100, 1, '0', CURRENT_TIMESTAMP, NULL),
('Azeite Extra Virgem 500ml', 19.90, 30, 1, '0', CURRENT_TIMESTAMP, NULL),
('Sal Refinado 1kg', 2.50, 80, 1, '0', CURRENT_TIMESTAMP, NULL),
('Açúcar Cristal 1kg', 5.30, 60, 1, '0', CURRENT_TIMESTAMP, NULL),
('Farinha de Trigo 1kg', 6.70, 70, 1, '0', CURRENT_TIMESTAMP, NULL),
-- 2. Higiene Pessoal (ID 2)
('Shampoo 300ml', 12.50, 30, 2, '0', CURRENT_TIMESTAMP, NULL),
('Sabonete em Barra 90g', 2.20, 150, 2, '0', CURRENT_TIMESTAMP, NULL),
('Pasta de Dente 90g', 4.50, 80, 2, '0', CURRENT_TIMESTAMP, NULL),
('Desodorante Roll-on 50ml', 9.90, 40, 2, '0', CURRENT_TIMESTAMP, NULL),
('Papel Higiênico 4un', 6.80, 60, 2, '0', CURRENT_TIMESTAMP, NULL),
-- 3. Limpeza Doméstica (ID 3)
('Detergente 500ml', 2.90, 100, 3, '0', CURRENT_TIMESTAMP, NULL),
('Sabão em Pó 1kg', 14.50, 50, 3, '0', CURRENT_TIMESTAMP, NULL),
('Esponja de Aço', 1.50, 200, 3, '0', CURRENT_TIMESTAMP, NULL),
('Água Sanitária 1L', 3.80, 70, 3, '0', CURRENT_TIMESTAMP, NULL),
('Desinfetante 2L', 7.90, 60, 3, '0', CURRENT_TIMESTAMP, NULL),
-- 4. Bebidas Alcoólicas (ID 4)
('Cerveja Lata 350ml', 4.00, 120, 4, '0', CURRENT_TIMESTAMP, NULL),
('Vinho Tinto 750ml', 29.90, 25, 4, '0', CURRENT_TIMESTAMP, NULL),
('Whisky 1L', 89.90, 10, 4, '0', CURRENT_TIMESTAMP, NULL),
('Vodka 900ml', 35.00, 15, 4, '0', CURRENT_TIMESTAMP, NULL),
-- 5. Bebidas Não Alcoólicas (ID 5)
('Refrigerante 2L', 7.50, 90, 5, '0', CURRENT_TIMESTAMP, NULL),
('Suco de Laranja 1L', 5.90, 60, 5, '0', CURRENT_TIMESTAMP, NULL),
('Água Mineral 500ml', 2.00, 150, 5, '0', CURRENT_TIMESTAMP, NULL),
('Chá Mate 900ml', 6.20, 40, 5, '0', CURRENT_TIMESTAMP, NULL),
('Energético 250ml', 8.50, 30, 5, '0', CURRENT_TIMESTAMP, NULL),
-- 6. Laticínios (ID 6)
('Leite UHT 1L', 4.90, 100, 6, '0', CURRENT_TIMESTAMP, NULL),
('Queijo Mussarela 200g', 14.90, 25, 6, '0', CURRENT_TIMESTAMP, NULL),
('Manteiga 200g', 10.50, 35, 6, '0', CURRENT_TIMESTAMP, NULL),
('Iogurte Natural 900g', 9.80, 40, 6, '0', CURRENT_TIMESTAMP, NULL),
('Requeijão 220g', 7.50, 60, 6, '0', CURRENT_TIMESTAMP, NULL),
-- 7. Carnes e Peixes (ID 7)
('Picanha Bovina', 59.90, 20, 7, '1', CURRENT_TIMESTAMP, NULL),
('Peito de Frango', 18.50, 40, 7, '1', CURRENT_TIMESTAMP, NULL),
('Linguiça Calabresa', 19.80, 25, 7, '1', CURRENT_TIMESTAMP, NULL),
('Salmão', 79.90, 10, 7, '1', CURRENT_TIMESTAMP, NULL),
('Carne Moída', 35.00, 30, 7, '1', CURRENT_TIMESTAMP, NULL),
-- 8. Padaria (ID 8)
('Pão de Forma', 6.00, 80, 8, '0', CURRENT_TIMESTAMP, NULL),
('Bolo de Chocolate', 15.00, 20, 8, '0', CURRENT_TIMESTAMP, NULL),
('Pão Francês', 0.50, 200, 8, '0', CURRENT_TIMESTAMP, NULL),
('Coxinha Congelada', 2.50, 100, 8, '0', CURRENT_TIMESTAMP, NULL),
('Rosca Doce', 7.80, 35, 8, '0', CURRENT_TIMESTAMP, NULL),
-- 9. Frutas e Verduras (ID 9)
('Banana Prata', 5.50, 70, 9, '1', CURRENT_TIMESTAMP, NULL),
('Tomate', 6.80, 90, 9, '1', CURRENT_TIMESTAMP, NULL),
('Cenoura', 5.20, 80, 9, '1', CURRENT_TIMESTAMP, NULL),
('Batata', 4.50, 100, 9, '1', CURRENT_TIMESTAMP, NULL),
('Maçã', 7.90, 60, 9, '1', CURRENT_TIMESTAMP, NULL),
-- 10. Congelados (ID 10)
('Pizza Congelada 400g', 15.90, 30, 10, '0', CURRENT_TIMESTAMP, NULL),
('Nuggets 500g', 12.50, 40, 10, '0', CURRENT_TIMESTAMP, NULL),
('Sorvete 1L', 19.90, 25, 10, '0', CURRENT_TIMESTAMP, NULL),
('Hambúrguer Congelado 4un', 14.00, 50, 10, '0', CURRENT_TIMESTAMP, NULL),
('Batata Frita 1kg', 18.50, 35, 10, '0', CURRENT_TIMESTAMP, NULL),
-- 11. Doces e Sobremesas (ID 11)
('Chocolate ao Leite 100g', 5.50, 80, 11, '0', CURRENT_TIMESTAMP, NULL),
('Geleia de Morango 300g', 8.20, 45, 11, '0', CURRENT_TIMESTAMP, NULL),
('Pudim em Pó 200g', 3.50, 70, 11, '0', CURRENT_TIMESTAMP, NULL),
('Doce de Leite 400g', 8.50, 50, 11, '0', CURRENT_TIMESTAMP, NULL),
('Creme de Avelã 350g', 19.90, 20, 11, '0', CURRENT_TIMESTAMP, NULL),
-- 12. Snacks e Salgadinhos (ID 12)
('Batata Chips 100g', 6.50, 90, 12, '0', CURRENT_TIMESTAMP, NULL),
('Amendoim Torrado 200g', 4.80, 100, 12, '0', CURRENT_TIMESTAMP, NULL),
('Biscoito Salgado 200g', 3.20, 120, 12, '0', CURRENT_TIMESTAMP, NULL),
('Pipoca de Micro-ondas 100g', 2.90, 80, 12, '0', CURRENT_TIMESTAMP, NULL),
('Castanha de Caju 150g', 15.00, 30, 12, '0', CURRENT_TIMESTAMP, NULL),
-- 13. Produtos de Bebê (ID 13)
('Fralda Descartável 30un', 29.90, 25, 13, '0', CURRENT_TIMESTAMP, NULL),
('Lenço Umedecido 50un', 8.50, 60, 13, '0', CURRENT_TIMESTAMP, NULL),
('Papinha de Fruta 120g', 4.20, 70, 13, '0', CURRENT_TIMESTAMP, NULL),
('Shampoo Bebê 200ml', 12.00, 40, 13, '0', CURRENT_TIMESTAMP, NULL),
('Sabonete Bebê 90g', 3.50, 80, 13, '0', CURRENT_TIMESTAMP, NULL),
-- 14. Pet Shop (ID 14)
('Ração para Cães 10kg', 59.90, 20, 14, '0', CURRENT_TIMESTAMP, NULL),
('Ração para Gatos 1kg', 15.50, 40, 14, '0', CURRENT_TIMESTAMP, NULL),
('Petisco para Cães 200g', 9.90, 50, 14, '0', CURRENT_TIMESTAMP, NULL),
('Areia para Gatos 4kg', 12.00, 30, 14, '0', CURRENT_TIMESTAMP, NULL),
('Shampoo Pet 500ml', 18.00, 25, 14, '0', CURRENT_TIMESTAMP, NULL),
-- 15. Utilidades Domésticas (ID 15)
('Vassoura', 15.00, 20, 15, '0', CURRENT_TIMESTAMP, NULL),
('Rodo de Pia', 8.50, 30, 15, '0', CURRENT_TIMESTAMP, NULL),
('Pano de Chão', 4.50, 50, 15, '0', CURRENT_TIMESTAMP, NULL),
('Balde 10L', 12.90, 25, 15, '0', CURRENT_TIMESTAMP, NULL),
('Lixeira 5L', 19.90, 15, 15, '0', CURRENT_TIMESTAMP, NULL),
-- Adicionais para completar 100
('Óleo de Soja 900ml', 7.90, 90, 1, '0', CURRENT_TIMESTAMP, NULL),
('Café em Pó 250g', 12.00, 45, 1, '0', CURRENT_TIMESTAMP, NULL),
('Condicionador 300ml', 13.00, 25, 2, '0', CURRENT_TIMESTAMP, NULL),
('Limpador Multiuso 500ml', 6.50, 70, 3, '0', CURRENT_TIMESTAMP, NULL),
('Cerveja 600ml', 6.00, 70, 4, '0', CURRENT_TIMESTAMP, NULL),
('Suco de Uva 1L', 6.50, 50, 5, '0', CURRENT_TIMESTAMP, NULL),
('Leite Condensado 395g', 6.70, 50, 6, '0', CURRENT_TIMESTAMP, NULL),
('Filé Mignon', 69.90, 15, 7, '1', CURRENT_TIMESTAMP, NULL),
('Torta de Frango', 20.00, 10, 8, '0', CURRENT_TIMESTAMP, NULL),
('Abacaxi', 6.00, 40, 9, '1', CURRENT_TIMESTAMP, NULL),
('Lasanha Congelada 600g', 22.50, 20, 10, '0', CURRENT_TIMESTAMP, NULL),
('Chocolate Amargo 100g', 6.00, 60, 11, '0', CURRENT_TIMESTAMP, NULL),
('Salgadinho de Milho 100g', 5.50, 80, 12, '0', CURRENT_TIMESTAMP, NULL),
('Fralda Tamanho G 20un', 25.00, 30, 13, '0', CURRENT_TIMESTAMP, NULL),
('Ração para Peixes 50g', 7.50, 40, 14, '0', CURRENT_TIMESTAMP, NULL),
('Escova de Limpeza', 9.90, 35, 15, '0', CURRENT_TIMESTAMP, NULL);

select * from categorias;
select * from formapagamento;
select * from estoque;
select * from usuarios;
select * from vendas;
select * from itens_venda;
select * from caixa;
select * from mov_caixa;