CREATE OR REPLACE PROCEDURE sp_players_team_name(player_name VARCHAR(50), OUT team_name VARCHAR(45))
AS $$
BEGIN
    team_name := 'The player currently has no team';

    SELECT t.name
    INTO team_name
    FROM players AS p
    LEFT JOIN teams AS t ON p.team_id = t.id
    WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;
END;
$$ LANGUAGE plpgsql;