"CREATE SEQUENCE person_id_by_2_sequence
START 4
INCREMENT 2
OWNED BY person.id
/*
OWNED BY person.IDENTITY
Това се прави с цел когато като изтрием таблицата и
създадения sequence да се изтрие с таблицата
*\"