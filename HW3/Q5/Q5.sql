
ALTER TABLE player_bios
ADD COLUMN position TEXT;

UPDATE player_bios 
SET position = new_table.position
from new_table
WHERE player_bios.id = new_table.player;

SELECT firstname, lastname, position FROM player_bios LIMIT 5;









