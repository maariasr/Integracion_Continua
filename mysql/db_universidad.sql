use universidad;

CREATE TABLE curso(
    id int not null PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    creditos VARCHAR(50)
);

INSERT INTO curso(nombre, creditos)
VALUES ("Programacion Avanzada", "5"), ("Programacion Web", "5"), ("Matematicas", "4"), ("Sistemas Operativos", "4");