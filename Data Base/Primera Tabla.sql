drop database if exists datos;
create database datos;
use datos;
create table estudiantes(
idEstudiante binary(16) primary key default (UUID_TO_BIN(uuid())), 
nombre varchar(30) not null,
apellido varchar(30) not null,
edad int not null,
pais varchar(15) 
);
insert into estudiantes(nombre, apellido, edad, pais)
values
('Franco', 'Morales', 27, "Argentina");
select * from datos.estudiantes;