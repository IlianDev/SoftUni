SELECT
		id,
		concat(first_name, ' ', last_name) as "Full Name",
		concat(job_title) as  "Job Title"
FROM
	employees