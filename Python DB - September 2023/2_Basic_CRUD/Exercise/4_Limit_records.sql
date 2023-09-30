/*
 Develop a SQL query that selects from the "employees" table "id", "first_name", "last_name", and

"job_title". Combine the "first_name" and "last_name" fields into a single field called "Full Name". Rename the "id"
 column as "ID" and the "job_title" column as "Job Title". Sort them by the "first_name" field in ascending
 alphabetical order. Finally, LIMIT the results to 50
 */
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
-- ORDER BY first_name ASC
-- LIMIT 50;
