from flask import Flask
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL using environment variables
def connect_db():
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db',  # 'db' is the service name of PostgreSQL in docker-compose
        port=5432
    )
    return conn

@app.route('/')
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT 'Hello, World!'")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
