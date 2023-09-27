SELECT
	id,
	first_name,
	last_name,
	job_title,
	department_id,
	salary
From
	employees
Where
	salary > 1000
	and department_id = 4
Order by id
	