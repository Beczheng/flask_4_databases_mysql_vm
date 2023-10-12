import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from .env file

load_dotenv()  

# Database connection settings from environment variables

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
#DB_PORT = int(os.getenv("DB_PORT", 3306))
#DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Create a connection string

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'

# Create engine

engine = create_engine(
        connection_string,
        connect_args=connect_args,
)

# Create flask application

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/doctors')
def doctors():
    with engine.connect() as connection:
        query1 = text('SELECT * FROM doctors')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('doctors.html', data1=db_data1)

@app.route('/licenses')
def licenses():
    with engine.connect() as connection:
        query2 = text('SELECT * FROM licenses')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('licenses.html', data2=db_data2)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
