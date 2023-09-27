SELECT
	id,
	concat(first_name,' ', last_name) as full_name,
	job_title,
	salary
From
	employees
Where
	salary > 1000
	and id <> 3 -- id is different <> of 3
Order by id
