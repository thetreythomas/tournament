# Udacity - Tournament Results

## Synopsis

This project creates a Python module that uses a PostgreSQL database to keep track of players and matches in a game tournment using the Swiss pairings system.

https://en.wikipedia.org/wiki/Swiss-system_tournament

# Files
* tournament.py
* tournament_test.py
* tournament.sql

# Usage

You will first need to make sure the tournament database is created.
```shell
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
psql (9.3.12)
Type "help" for help.

vagrant=> CREATE DATABASE tournament;
CREATE DATABASE
vagrant=> \q
```

After creating the *tournament* database, you can load the tables using the tournament.sql file.
```shell
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
psql (9.3.12)
Type "help" for help.

vagrant=> \i tournament.sql
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE VIEW
tournament=>
```

You can run the tournament_test.py file to make sure all the tables and the tournament.py is working accordingly.
```shell
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
[(5, 'Bruno Walton', 0L, 0L), (6, "Boots O'Neal", 0L, 0L), (7, 'Cathy Burton', 0L, 0L), (8, 'Diane Grant', 0L, 0L)]
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$
```