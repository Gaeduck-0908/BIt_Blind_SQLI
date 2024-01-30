import pymysql

def sql_init():
    database = 'test_db'  # 새로 생성할 데이터베이스 이름
    host = 'localhost'
    user = 'root'
    password = '1234'

    conn = pymysql.connect(host=host, user=user, password=password)
    c = conn.cursor()

    c.execute(f"DROP DATABASE IF EXISTS {database}")
    c.execute(f"CREATE DATABASE {database}")
    c.execute(f"USE {database}")

    c.execute("DROP TABLE IF EXISTS Users")

    c.execute('''
        CREATE TABLE Users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL
        )
    ''')

    c.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", ('admin', 'SECRET_P@SSW0RD'))
    c.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", ('guest', 'guest'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    sql_init()
