#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    cur.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    cur.execute("DELETE FROM players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(id) FROM players;")
    countP = cur.fetchone()[0]
    return countP
    conn.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    SQL = "INSERT INTO players (player_name) VALUES (%s);"
    data = (name,)
    cur.execute(SQL, data)
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    SQL = "SELECT * FROM standings ORDER BY wins;"
    cur.execute(SQL)
    players = cur.fetchall()
    conn.close()
    return players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    SQL = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    data = (winner, loser)
    cur.execute(SQL,data)
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    conn = psycopg2.connect("dbname=tournament")
    cur = conn.cursor()
    SQL = "SELECT id, player_name FROM standings ORDER BY wins;"
    cur.execute(SQL)

    swiss_pairings = []
    list = cur.fetchall()
    total_players = len(list)
    #print list

    for i in range(0, total_players, 2):
        pair = list[i][0], list[i][1], list[i + 1][0], list[i + 1][1]
        #print pair
        swiss_pairings.append(pair)
    return swiss_pairings

    conn.close()


