import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # 创建 users 表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # 创建 course 表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_description TEXT,
            instructor TEXT
        )
    ''')

    # 创建 user_course 关联表 (Many-to-Many)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_course (
            user_id INTEGER,
            course_id INTEGER,
            enrollment_date TEXT DEFAULT (datetime('now', 'localtime')),
            PRIMARY KEY (user_id, course_id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

# 创建表
create_tables()