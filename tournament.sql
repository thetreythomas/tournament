-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- DROP old tables
-- DROP old views
DROP VIEW IF EXISTS wins;
DROP VIEW IF EXISTS standings;
DROP TABLE IF EXISTS players CASCADE ;
DROP TABLE IF EXISTS matches CASCADE ;


-- Creating players table with id and player name
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  player_name VARCHAR(71)
);

-- Creating matches table with match_id, winner, and loser
CREATE TABLE matches (
  match_id SERIAL PRIMARY KEY,
  winner INT REFERENCES players(id) NOT NULL,
  loser INT REFERENCES players(id) NOT NULL
);

-- Creating a view to show player id, player name, wins, and total matches
CREATE VIEW standings AS
  SELECT players.id, players.player_name,
    (SELECT count(matches.winner) FROM matches
      WHERE players.id = matches.winner)
      AS wins,
    (SELECT count(matches.match_id) FROM matches
      WHERE players.id = matches.winner
      OR players.id = matches.loser)
      AS matches
  FROM players
  ORDER BY wins;