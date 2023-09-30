SELECT
    id AS ID,
    CONCAT(first_name, ' ', last_name) AS "Full Name",
    job_title AS "Job Title"
FROM
    employees
ORDER BY
    first_name ASC
LIMIT 50;


-- SELECT
-- 	id as "ID",
-- 	conctat_WS(' ',
-- 			   first_name,
-- 			   last_name
-- 			  ) as "Full name",
-- 	job_title as "Job Title"
-- FROM
-- 	employees
-- ORDER BY
-- 	first_name ASC
-- LIMIT 50;
