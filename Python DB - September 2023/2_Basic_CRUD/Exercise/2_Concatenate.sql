/*
 From the selected already data combine the "name" and "state", fields into a single field called "Cities Information".
 Rename the "area" column as "Area (km2)".

Submit your query for this task in the Judge system.
 */

SELECT
	CONCAT(
		name,
		' ',
		state
	) as "Cities Information",
	area as "Area (km2)"
from cities;


