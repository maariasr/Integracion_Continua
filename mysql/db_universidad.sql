use universidad;

CREATE TABLE curso(
    id int not null PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    creditos VARCHAR(50)
);

INSERT INTO curso(nombre, creditos)
VALUES ("Matematicas", "4"), ("Programacion Avanzada", "4"), ("Sistemas Operativos", "5");