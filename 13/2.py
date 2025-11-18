from flask import Flask, jsonify, g
import mysql.connector


app = Flask(__name__)

DATABASE = "flight_game"

def get_db():
    if 'db' not in g:
        conn = mysql.connector.connect(
            user="root",
            password="password",
            host="127.0.0.1",
            port=3306,
            database=DATABASE,
            autocommit=True
        )
        g.conn = conn
        g.db = conn.cursor(dictionary=True)
    return g.db


@app.route("/airport/<icao>")
def fetch_icao(icao):
    db = get_db()
    db.execute("""
        SELECT c.name as location, a.name FROM country c 
        JOIN airport a ON a.iso_country = c.iso_country 
        WHERE a.ident = %s
    """, (icao,))
    country = db.fetchone()

    if country is None:
        return jsonify({
            "ICAO": icao,
            "Country": None,
            "message": "No country found"
        }), 404

    response = {
        "ICAO": icao,
        "Name": country["name"],
        "Location": country["location"]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True, host='127.0.0.1', port=5000)