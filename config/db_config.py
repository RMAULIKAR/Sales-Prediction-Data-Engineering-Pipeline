import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aDMIN@099",  # change if needed
        database="sales_pipeline"
    )

    return conn