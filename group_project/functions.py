import mysql.connector
import threading
import random
from geopy import distance


#Flask's g
_storage = threading.local() #"_"internal use # class container

def get_g():
    if not hasattr(_storage, "storage"):
        _storage.storage = {}
    return _storage.storage

def get_db():
    g = get_g()
    if 'db' not in g:
        conn = mysql.connector.connect(
            user="root",
            password="password",
            host="127.0.0.1",
            port=3306,
            database="project",
            autocommit=True
        )
        g['conn'] = conn
        g['db'] = conn.cursor(dictionary=True)
    return g['db']

# select 30 airports for the game
def get_airports():
    db = get_db()
    db.execute("""
        SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
        FROM airport
        WHERE continent = 'EU'
        AND type = 'large_airport'
        ORDER BY RAND()
        LIMIT 30
    """)
    result = db.fetchall()
    return result

# get all goals
def get_goals():
    db = get_db()
    db.execute("SELECT * FROM goal")
    result = db.fetchall()
    return result

# create new game
def new_game(st_money, cur_airport, p_name, p_range, a_ports):
    db = get_db()
    db.execute("""
        INSERT INTO game(money, location, screen_name, player_range)
        VALUES(%s, %s, %s, %s)""", (st_money, cur_airport, p_name, p_range ))
    g_id = db.lastrowid
    # add goals/loot boxes
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal["id"])

    # exclude starting airport
    g_ports = a_ports[1:].copy()
    random.shuffle(g_ports)

    #ports table
    for i, goal_id in enumerate(goal_list):
        db.execute("INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s)", (g_id, g_ports[i]["ident"], goal_id))
        i += 1
    return g_id

# get airport info
def get_airport_info(icao):
    db = get_db()
    db.execute("""
    SELECT iso_country, ident, name, latitude_deg, longitude_deg 
    FROM airport
    WHERE ident = %s
    """, (icao,))
    result = db.fetchone()
    return result

# check if airport has goal
def check_goal(g_id, cur_airport):
    db = get_db()
    db.execute("""
    SELECT ports.id, ports.goal, goal.id as goal_id, goal.name, goal.money
    FROM ports
    JOIN goal ON goal.id = ports.goal
    WHERE game = %s
    AND airport = %s
    """, (g_id, cur_airport),)
    result = db.fetchone()
    print()
    print(result)
    if result is None:
        return False
    return result

# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km

# get airports in range
def airports_in_range(icao, a_ports, p_range):
    in_range = []
    for a_port in a_ports:
        dist = calculate_distance(icao, a_port['ident'])
        if dist <= p_range and not dist == 0:
            in_range.append(a_port)
    return in_range

#set loot box opened
# update location ###NEED add updating the time
def update_location(icao, p_range, u_money, g_id):
    db = get_db()
    db.execute( f'''UPDATE game SET location = %s, player_range = %s, money = %s WHERE id = %s''', (icao, p_range, u_money, g_id),)








def open_chest(goal, money):
    if goal['money'] > 0:
        money += goal['money']
        print(f"Congratulations! You found {goal['name']}. That is worth {goal['money']}$")
        print(f"You have now {money:.0f}$")

    elif goal['money'] == 0:

        print(f"Congratulations! You found the diamond. Now go to start.")
    else:
        money = 0
        print(f"Oh no! you have been robbed. You lost all your money")

    return money

def win_g(goal):
    if goal['money'] > 0:
        win = False
    elif goal['money'] == 0:
        win = True
    else:
        win = False
    return win

