-- Country 
create table Country (
	country_id integer not null unique
	, name text	
	, primary key (country_id)
);

-- Team
create table Team (
	id integer not null unique
	, team_api_id integer unique
	, team_fifa_api_id integer
	, team_long_name text
	, team_short_name text
	, primary key (id)
);

-- Player
create table Player (
	id integer not null unique
	, player_api_id integer unique
	, player_name text
	, player_fifa_api_id integer
	, birthday timestamp
	, height real
	, weight real
	, primary key (id)
);

-- League
create table League (
	league_id integer not null unique
	, country_id integer not null
	, name text
	, primary key (league_id)
	, foreign key (country_id) references country(country_id)
);

-- Player_Attributes
create table Player_Attributes (
	id integer not null unique
	, player_fifa_api_id integer 
	, player_api_id integer
	, date timestamp
	, overall_rating integer
	, potential integer
	, preferred_foot text
	, attacking_work_rate text
	, defensive_work_rate text
	, crossing integer
	, finishing integer
	, heading_accuracy integer
	, short_passing integer
	, volleys integer
	, dribbling integer
	, curve integer
	, free_kick_accuracy integer
	, long_passing integer
	, ball_control integer
	, acceleration integer
	, sprint_speed integer
	, agility integer
	, reactions integer
	, balance integer
	, shot_power integer
	, jumping integer
	, stamina integer
	, strength integer
	, long_shots integer
	, aggression integer
	, interceptions integer
	, positioning integer
	, vision integer
	, penalties integer
	, marking integer
	, standing_tackle integer
	, sliding_tackle integer
	, gk_diving integer
	, gk_handling integer
	, gk_kicking integer
	, gk_positioning integer
	, gk_reflexes integer
	, primary key (id)
	, foreign key (player_api_id) references Player (player_api_id)
);

-- Team_Attributes
create table Team_Attributes (
	id integer not null unique
	, team_fifa_api_id integer
	, team_api_id integer
	, date timestamp
	, buildUpPlaySpeed integer
	, buildUpPlaySpeedClass text
	, buildUpPlayDribbling integer
	, buildUpPlayDribblingClass text
	, buildUpPlayPassing integer
	, buildUpPlayPassingClass text
	, buildUpPlayPositioningClass text
	, chanceCreationPassing integer
	, chanceCreationPassingClass text
	, chanceCreationCrossing integer 
	, chanceCreationCrossingClass text
	, chanceCreationShooting integer
	, chanceCreationShootingClass text
	, chanceCreationPositioningClass text
	, defencePressure integer
	, defencePressureClass text
	, defenceAggression integer
	, defenceAggressionClass text
	, defenceTeamWidth integer
	, defenceTeamWidthClass text
	, defenceDefenderLineClass text
	, primary key (id)
	, foreign key (team_api_id) references Team (team_api_id)
);

-- Match
create table Match (
	id integer not null unique
	, country_id integer
	, league_id integer
	, season text
	, stage integer
	, date timestamp
	, match_api_id integer unique
	, home_team_api_id integer
	, away_team_api_id integer
	, home_team_goal integer
	, away_team_goal integer
	, home_player_X1 integer
	, home_player_X2 integer
	, home_player_X3 integer
	, home_player_X4 integer
	, home_player_X5 integer
	, home_player_X6 integer
	, home_player_X7 integer
	, home_player_X8 integer
	, home_player_X9 integer
	, home_player_X10 integer
	, home_player_X11 integer
	, away_player_X1 integer
	, away_player_X2 integer
	, away_player_X3 integer
	, away_player_X4 integer
	, away_player_X5 integer
	, away_player_X6 integer
	, away_player_X7 integer
	, away_player_X8 integer
	, away_player_X9 integer
	, away_player_X10 integer
	, away_player_X11 integer
	, home_player_Y1 integer
	, home_player_Y2 integer
	, home_player_Y3 integer
	, home_player_Y4 integer
	, home_player_Y5 integer
	, home_player_Y6 integer
	, home_player_Y7 integer
	, home_player_Y8 integer
	, home_player_Y9 integer
	, home_player_Y10 integer
	, home_player_Y11 integer
	, away_player_Y1 integer
	, away_player_Y2 integer
	, away_player_Y3 integer
	, away_player_Y4 integer
	, away_player_Y5 integer
	, away_player_Y6 integer
	, away_player_Y7 integer
	, away_player_Y8 integer
	, away_player_Y9 integer
	, away_player_Y10 integer
	, away_player_Y11 integer
	, home_player_1 integer
	, home_player_2 integer
	, home_player_3 integer
	, home_player_4 integer
	, home_player_5 integer
	, home_player_6 integer
	, home_player_7 integer
	, home_player_8 integer
	, home_player_9 integer
	, home_player_10 integer
	, home_player_11 integer
	, away_player_1 integer	
	, away_player_2 integer
	, away_player_3 integer
	, away_player_4 integer
	, away_player_5 integer
	, away_player_6 integer
	, away_player_7 integer	
	, away_player_8 integer
	, away_player_9 integer
	, away_player_10 integer
	, away_player_11 integer
	, primary key (id)
	, foreign key(country_id) references country(country_id)
	, foreign key(league_id) references League(league_id)
	, foreign key(home_team_api_id) references Team(team_api_id)
	, foreign key(away_team_api_id) references Team(team_api_id)
	, foreign key(home_player_1) references Player(player_api_id)
	, foreign key(home_player_2) references Player(player_api_id)
	, foreign key(home_player_3) references Player(player_api_id)
	, foreign key(home_player_4) references Player(player_api_id)
	, foreign key(home_player_5) references Player(player_api_id)
	, foreign key(home_player_6) references Player(player_api_id)
	, foreign key(home_player_7) references Player(player_api_id)
	, foreign key(home_player_8) references Player(player_api_id)
	, foreign key(home_player_9) references Player(player_api_id)
	, foreign key(home_player_10) references Player(player_api_id)
	, foreign key(home_player_11) references Player(player_api_id)
	, foreign key(away_player_1) references Player(player_api_id)
	, foreign key(away_player_2) references Player(player_api_id)
	, foreign key(away_player_3) references Player(player_api_id)
	, foreign key(away_player_4) references Player(player_api_id)
	, foreign key(away_player_5) references Player(player_api_id)
	, foreign key(away_player_6) references Player(player_api_id)
	, foreign key(away_player_7) references Player(player_api_id)
	, foreign key(away_player_8) references Player(player_api_id)
	, foreign key(away_player_9) references Player(player_api_id)
	, foreign key(away_player_10) references Player(player_api_id)
	, foreign key(away_player_11) references Player(player_api_id)
);