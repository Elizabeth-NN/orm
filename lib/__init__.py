# lib/__init__.py
import sqlite3

CONN = sqlite3.connect('clinic.db')
CURSOR = CONN.cursor()