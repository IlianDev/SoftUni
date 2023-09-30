SELECT
	id as ID,
	CONCAT_WS(
		' ',
		first_name,
		middle_name,
		last_name
	) AS "Full Name",
	hire_date as "Hire Date"
FROM
	employees
ORDER BY hire_date ASC
OFFSET 9; -- offset start from 0; 0-9 are 10 numbers

