CREATE TYPE DivisionType AS ENUM ('Atlantic', 'Central', 'Southeast', 'Northwest', 'Pacific','Southwest');
CREATE TYPE ConferenceType AS ENUM ('Western', 'Eastern');

CREATE TABLE teams (
id CHAR(3) PRIMARY KEY,
location TEXT,
name TEXT,
division DivisionType,
conference ConferenceType
);

	
SELECT * FROM teams;

insert into teams VALUES
  ('BOS', 'Boston', 'Celtics', 'Atlantic', 'Eastern'),
  ('BKN', 'Brooklyn', 'Nets', 'Atlantic', 'Eastern'),
  ('NYK', 'New York', 'Knicks', 'Atlantic', 'Eastern'),
  ('PHI', 'Philadelphia', '76ers', 'Atlantic', 'Eastern'),
  ('TOR', 'Toronto', 'Raptors', 'Atlantic', 'Eastern'),
  ('CHI', 'Chicago', 'Bulls', 'Central', 'Eastern'),
  ('CLE', 'Cleveland', 'Cavaliers', 'Central', 'Eastern'),
  ('DET', 'Detroit', 'Pistons', 'Central', 'Eastern'),
  ('IND', 'Indiana', 'Pacers', 'Central', 'Eastern'),
  ('MIL', 'Milwaukee', 'Bucks', 'Central', 'Eastern'),
  ('ATL', 'Atlanta', 'Hawks', 'Southeast', 'Eastern'),
  ('CHA', 'Charlotte', 'Bobcats', 'Southeast', 'Eastern'),
  ('MIA', 'Miami', 'Heat', 'Southeast', 'Eastern'),
  ('ORL', 'Orlando', 'Magic', 'Southeast', 'Eastern'),
  ('WAS', 'Washington', 'Wizards', 'Southeast', 'Eastern'),
  ('DEN', 'Denver', 'Nuggets', 'Northwest', 'Western'),
  ('MIN', 'Minnesota', 'Timberwolves', 'Northwest', 'Western'),
  ('OKC', 'Oklahoma City', 'Thunder', 'Northwest', 'Western'),
  ('POR', 'Portland', 'Trail Blazers', 'Northwest', 'Western'),
  ('UTA', 'Utah', 'Jazz', 'Northwest', 'Western'),
  ('GSW', 'Golden State', 'Warriors', 'Pacific', 'Western'),
  ('LAC', 'Los Angeles', 'Clippers', 'Pacific', 'Western'),
  ('LAL', 'Los Angeles', 'Lakers', 'Pacific', 'Western'),
  ('PHX', 'Phoenix', 'Suns', 'Pacific', 'Western'),
  ('SAC', 'Sacramento', 'Kings', 'Pacific', 'Western'),
  ('DAL', 'Dallas', 'Mavericks', 'Southwest', 'Western'),
  ('HOU', 'Houston', 'Rockets', 'Southwest', 'Western'),
  ('MEM', 'Memphis', 'Grizzlies', 'Southwest', 'Western'),
  ('NOP', 'New Orleans', 'Hornets', 'Southwest', 'Western'),
  ('SAS', 'San Antonio', 'Spurs', 'Southwest', 'Western');
  
  select * from teams;