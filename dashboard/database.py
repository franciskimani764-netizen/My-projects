import sqlite3 
import pandas as pd
import streamlit as st

DATABASE = "business.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def initialise_database():
    conn = get_connection()
    cur = conn.cursor
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sales(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    price REAL NOT NULL,
    sale_date NOT NULL
    )
    """)

    conn = get_connection()
    cur = conn.cursor
    conn.excute("""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL)
    """)
    conn.commit()
    conn.close()