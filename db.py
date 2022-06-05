import sqlite3
from sqlite3 import Error
from clean import players
from random import randint

def create_connection(db_file):
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_player(conn, player):
    sql = ''' INSERT OR IGNORE INTO players(name,team,age,nation,position,jersey)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, player)
    conn.commit()
    return cur.lastrowid

def select_random_player(conn):
    index = randint(0, 276)
    sql = '''SELECT * FROM players LIMIT 1 OFFSET ?
                '''
    cur = conn.cursor()
    cur.execute(sql, (index,))
    row = cur.fetchall()
    print(row)


if __name__ == '__main__':

    players_table = """ CREATE TABLE IF NOT EXISTS players (
                                        name text,
                                        team text,
                                        age integer,
                                        nation text,
                                        position text,
                                        jersey integer
                                    ); """
    db_file = "sqlite.db"
    conn = create_connection(db_file)
    with conn:
        create_table(conn, players_table)
        for player in players:
            # print(player)
            data = (player[0], player[1], player[2], player[3], player[4], player[5])
            create_player(conn, data)
        select_random_player(conn)