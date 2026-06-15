from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

# ==================================
# ADMINS
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# ==================================
# TEACHERS
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
""")

# ==================================
# CLASSES
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL UNIQUE,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
)
""")

# ==================================
# STUDENTS
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_code TEXT NOT NULL UNIQUE,
    student_name TEXT NOT NULL,
    gender TEXT NOT NULL,
    class_id INTEGER NOT NULL,

    FOREIGN KEY (class_id) REFERENCES classes(id)
)
""")

# ==================================
# ASSESSMENTS
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER NOT NULL UNIQUE,

    quiz REAL DEFAULT 0,
    homework REAL DEFAULT 0,
    attendance REAL DEFAULT 0,
    assignment REAL DEFAULT 0,
    midterm REAL DEFAULT 0,
    final REAL DEFAULT 0,
    participation REAL DEFAULT 0,
    project REAL DEFAULT 0,
    behavior REAL DEFAULT 0,

    average REAL DEFAULT 0,

    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

# ==================================
# PREDICTIONS
# ==================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER NOT NULL UNIQUE,
    predicted_score REAL DEFAULT 0,
    risk_level TEXT DEFAULT 'Low',
    recommendation TEXT DEFAULT '',

    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

conn.commit()
conn.close()

print("EduVision AI database created successfully.")