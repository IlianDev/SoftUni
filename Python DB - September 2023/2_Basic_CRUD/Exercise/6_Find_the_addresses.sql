SELECT
	id,
	CONCAT_WS(' ', number, street) as "adress",
	city_id
from addresses
WHERE id >= 20;
