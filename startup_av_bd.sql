create database startup_av;

use startup_av;

create table candidato(
    candidatoId int primary key auto_increment,
    nome varchar(50),
    telefone varchar(50),
    minibio varchar(140),
    entrevista float,
    teorico float,
    pratico float,
    softSkill float
);

