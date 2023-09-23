CREATE TYPE address as(
	street TEXT,
	city TEXT,
	postalCode CHAR(4)
);

CREATE TABLE customers(
	id serial PRIMARY KEY,
	customer_name TEXT,
	customer_address adress
);


INSERT INTO
	customers(customer_name, customer_address)
VALUES
	('Diyan',('some street', 'Sofia', '1618'));



