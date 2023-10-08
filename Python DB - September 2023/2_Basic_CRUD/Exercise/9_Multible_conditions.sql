SELECT
	number,
	street
FROM
	addresses
where
	id BETWEEN 50 AND 100
		OR
	number < 1000;

