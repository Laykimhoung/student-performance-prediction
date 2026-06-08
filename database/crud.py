from database.db import get_connection

# ==================================
# DASHBOARD
# ==================================

def get_total_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM students
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_classes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM classes
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_teachers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM teachers
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_high_risk_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM predictions
    WHERE risk_level = 'High'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==================================
# CLASSES
# ==================================

def get_all_classes():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        c.id,
        c.class_name,
        t.full_name
    FROM classes c
    JOIN teachers t
        ON c.teacher_id = t.id
    ORDER BY c.class_name
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ==================================
# STUDENTS
# ==================================

def get_all_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        s.id,
        s.student_code,
        s.student_name,
        s.gender,
        c.class_name
    FROM students s
    JOIN classes c
        ON s.class_id = c.id
    ORDER BY s.student_name
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_students_by_class(class_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        student_code,
        student_name,
        gender
    FROM students
    WHERE class_id = ?
    ORDER BY student_name
    """, (class_id,))

    data = cursor.fetchall()

    conn.close()

    return data

# ==================================
# AVERAGE SCORE
# ==================================
def get_average_score():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ROUND(AVG(average), 1)
    FROM assessments
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result