--- Создание вьюшки v_match
CREATE VIEW v_match AS (
SELECT
	c.name as country
	, m.date
	, l.name as league
	, t1.team_long_name AS home_team_name
	, t1.team_short_name AS home_team_name_short
	, t2.team_long_name AS away_team_name
	, t2.team_short_name AS away_team_name_short
	, m.home_team_goal
	, m.away_team_goal
FROM MATCH m 
LEFT JOIN Country c ON c.country_id=m.country_id
LEFT JOIN League l ON l.league_id=m.league_id
LEFT JOIN Team t1 ON t1.team_api_id=m.home_team_api_id
LEFT JOIN Team t2 ON t2.team_api_id=m.away_team_api_id
ORDER BY home_team_name, date);

--- Создание вьюшки v_player
CREATE VIEW v_player AS (
select
	player_name
	, cast(birthday as date) as birthday
	, height
	, round(weight*0.45, 2) as weight
	, cast(date as date) as date
	, preferred_foot
	, overall_rating
	, round((acceleration + sprint_speed + agility) / 3) as PAC
	, round((finishing + shot_power + long_shots) / 3) as SHO
	, round((short_passing + long_passing + ball_control + vision) / 4) as PAS
	, round((dribbling + ball_control + agility + balance) / 4) as DRI
	, round((standing_tackle + sliding_tackle + interceptions + marking + aggression) / 5) as DEF
	, round((strength + stamina + jumping + balance) / 4) as PHY
from (
select
	r.player_name
	, r.birthday
	, r.height
	, r.weight
	, ra.date 
	, ra.overall_rating
	, ra.preferred_foot
	, ra.finishing
	, ra.short_passing
	, ra.dribbling
	, ra.long_passing
	, ra.ball_control
	, ra.acceleration
	, ra.sprint_speed
	, ra.agility
	, ra.balance
	, ra.shot_power
	, ra.jumping
	, ra.stamina
	, ra.strength
	, ra.long_shots
	, ra.aggression
	, ra.interceptions
	, ra.vision
	, ra.marking
	, ra.standing_tackle
	, ra.sliding_tackle
from Player_attributes ra
left join player r on r.player_api_id=ra.player_api_id
)
order by player_name, date
)
;

--- Создание вьюшек для всех таблиц 
CREATE VIEW v_data_country AS (
select *
from Country
);
CREATE VIEW v_data_league AS (
select *
from League
);
CREATE VIEW v_data_match AS (
select *
from Match
);
CREATE VIEW v_data_player_att AS (
select *
from Player_Attributes
);
CREATE VIEW v_data_player AS (
select *
from Player
);
CREATE VIEW v_data_team_att AS (
select *
from Team_Attributes
);
CREATE VIEW v_data_team AS (
select *
from Team
);
