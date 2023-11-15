create database startup_av;

use startup_av;

create table candidato(
    candidatoId int primary key auto_increment,
    nome varchar(50),
    telefone varchar(20),
    minibio varchar(35),
    entrevista float,
    teorico float,
    pratico float,
    softSkill float
);

insert into candidato values(0, 'Carlos', '(15) 99639-2351', 'Eu sou o Carlos', 7, 7, 7, 7);
insert into candidato values(0, 'Mateus', '(15) 99639-2351', 'Eu sou o Mateus', 8, 8, 8, 8);
insert into candidato values(0, 'José', '(15) 99639-2351', 'Eu sou o José', 1, 1, 1, 1);
insert into candidato values(0, 'Kleber', '(15) 99639-2351', 'Eu sou o Kleber', 2, 2, 2, 2);
insert into candidato values(0, 'Joaquim', '(15) 99639-2351', 'Eu sou o Joaquim', 3, 3, 3, 3);
insert into candidato values(0, 'Roberto', '(15) 99639-2351', 'Eu sou o Roberto', 4, 4, 4, 4);
insert into candidato values(0, 'Julio', '(15) 99639-2351', 'Eu sou o Julio', 5, 5, 5, 5);
insert into candidato values(0, 'Gael', '(15) 99639-2351', 'Eu sou o Gael', 6, 6, 6, 6);
insert into candidato values(0, 'Tiago', '(15) 99639-2351', 'Eu sou o Tiago', 7, 7, 7, 7);
insert into candidato values(0, 'Pedro', '(15) 99639-2351', 'Eu sou o Pedro', 8, 8, 8, 8);
insert into candidato values(0, 'João', '(15) 99639-2351', 'Eu sou o João', 9, 9, 9, 9);
insert into candidato values(0, 'André', '(15) 99639-2351', 'Eu sou o André', 5, 5, 5, 5);
insert into candidato values(0, 'Judas', '(15) 99639-2351', 'Eu sou o Judas', 8, 8, 8, 8);
insert into candidato values(0, 'Inacio', '(15) 99639-2351', 'Eu sou o Inacio', 4, 4, 4, 4);
insert into candidato values(0, 'Joquebede', '(15) 99639-2351', 'Eu sou o Joquebede', 8, 8, 8, 8);
insert into candidato values(0, 'Elias', '(15) 99639-2351', 'Eu sou o Elias', 10, 10, 10, 10);
insert into candidato values(0, 'Samuel', '(15) 99639-2351', 'Eu sou o Samuel', 8, 8, 8, 8);
insert into candidato values(0, 'Adão', '(15) 99639-2351', 'Eu sou o Adão', 2, 2, 2, 2);
insert into candidato values(0, 'Junior', '(15) 99639-2351', 'Eu sou o Junior', 4, 4, 4, 4);
insert into candidato values(0, 'Nabucodonosor', '(15) 99639-2351', 'Eu sou o Nabucodonosor', 0, 0, 0, 0);

