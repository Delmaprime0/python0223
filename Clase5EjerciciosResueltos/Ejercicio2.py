import sqlite3


def lectura():
    conn = sqlite3.connect('Base.db')
    
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM miTabla')
    
    Rows = cursor.fetchall()

    cursor.close()
    conn.close()
    
    for filas in Rows:
        print(filas)