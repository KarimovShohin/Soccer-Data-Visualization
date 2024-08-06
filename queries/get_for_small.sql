--- Запрос на v_match
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2008 as year
from v_match
where extract(year from date) = 2008
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2009 as year
from v_match
where extract(year from date) = 2009
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2010 as year
from v_match
where extract(year from date) = 2010
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2011 as year
from v_match
where extract(year from date) = 2011
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2012 as year
from v_match
where extract(year from date) = 2012
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2013 as year
from v_match
where extract(year from date) = 2013
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2014 as year
from v_match
where extract(year from date) = 2014
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2015 as year
from v_match
where extract(year from date) = 2015
group by home_team_name
union all
select
    home_team_name as name
    , sum(home_team_goal) as total_home_goal
    , sum(away_team_goal) as total_away_goal
    , avg(home_team_goal) as avg_home_goal
    , avg(away_team_goal) as avg_away_goal
    , max(home_team_goal) as max_home_goal
    , max(away_team_goal) as max_away_goal
    , 2016 as year
from v_match
where extract(year from date) = 2016
group by home_team_name