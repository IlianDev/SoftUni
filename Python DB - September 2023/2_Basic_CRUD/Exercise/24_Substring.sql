CREATE VIEW view_initials
AS
SELECT
	SUBSTRING(first_name, 1,2) as initial, -- from 1 to 2
	last_name
from
	employees
order by
	last_name;