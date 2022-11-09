-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
-- this is in order to the parent table 'state' and the child table 'cities'
FROM cities, states
WHERE 
	states.name = "California" AND cities.state_id = states.id
ORDER BY cities.id;
