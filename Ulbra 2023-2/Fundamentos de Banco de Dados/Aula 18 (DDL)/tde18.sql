CREATE TABLE Professor
(
    Id int Not Null Primary Key,
    Nome varchar(100),
    Especializacao varchar(50),
    Idade int Not Null
)

CREATE TABLE Leciona
(
    Id int Not Null Primary Key,
    Prof_cod int Not Null,
    Dsc_cod int Not Null,
        Constraint professor_leciona
            FOREIGN KEY (Prof_cod) references Professor (Id)
        Constraint

        Constraint leciona_professor
            FOREIGN KEY (Dsc_cod) references Disciplina (Id_dsc)
        Constraint
)

CREATE TABLE Disciplina
(
    Id_dsc int Not Null Primary Key,
    Disciplina varchar (50),
    Carga_horario int Not Null
)

CREATE TABLE Utiliza
(
    Id_dsc int Not Null Primary Key,
    Dsc_cod int Not Null,
    Sft_cod int Not Null,
        Constraint disciplina_utiliza
            FOREIGN KEY (Dsc_cod) references Disciplina (Id_dsc)
        Constraint

        Constraint utiliza_disciplina
            FOREIGN KEY (Sft_cod) references Software (Id)
        Constraint
)

CREATE TABLE Software
(
    Id int Not Null Primary Key,
    Nome varchar Not Null,
    Tipo varchar Not Null,
)

