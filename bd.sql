drop database mercado;
create database mercado;
use mercado;

create table categorias(
	id_categorias int primary key auto_increment,
    nome_categoria varchar(40)
);

create table estoque(
	id_estoque int primary key auto_increment,
    nome_produto varchar(40) unique not null,
    preco float not null,
    quantidade int not null,
    categoria int,
    foreign key (categoria) references categorias(id_categorias),
    imagem varchar(100)
);

create table usuarios(
	id int primary key auto_increment,
    nome_usu varchar(50) not null,
    email varchar(50) unique not null,
    senha varchar(64) not null,
    cpf char(11) unique not null,
    telefone char(11) not null,
    imagem varchar(100)
);

insert into usuarios (nome_usu, email, senha, cpf, telefone, imagem)
values ("admin", "admin@gmail.com", sha2("admin", 256), "00000000000", "00000000000", "imgs/ft_perfil/admin.png");
select * from categorias;
select * from estoque;
select * from usuarios;