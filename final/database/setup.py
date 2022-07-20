import sqlite3
from sqlite3 import Error

from .connection import create_connection


def create_tables():
    conn = create_connection()

    sql = """CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        fec_alta TEXT NOT NULL,
        user_name TEXT NOT NULL,
        codigo_zip TEXT NOT NULL,
        credit_card_num TEXT NOT NULL,
        credit_card_ccv TEXT NOT NULL,
        cuenta_numero TEXT NOT NULL,
        direccion TEXT NOT NULL,
        geo_latitud TEXT NOT NULL,
        geo_longitud TEXT NOT NULL,
        color_favorito TEXT NOT NULL,
        foto_dni TEXT NOT NULL,
        ip TEXT NOT NULL,
        auto TEXT NOT NULL,
        auto_modelo TEXT NOT NULL,
        auto_tipo TEXT NOT NULL,
        auto_color TEXT NOT NULL,
        cantidad_compras_realizadas INTEGER,
        avatar TEXT NOT NULL,
        fec_birthday TEXT NOT NULL
)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at create_tables() : {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
