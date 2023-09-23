/*
CREATE TYPE adress as(
	street TEXT,
	city TEXT,
	postalCode CHAR(4)
);

CREATE TABLE cusomers(
	id serial PRIMARY KEY,
	customer_name TEXT,
	customer_adress adress
);
*/

INSERT INTO
	customers(customer_name, customer_addres)
VALUES
	('Diyan',('some street', 'Sofia', '1618'));



