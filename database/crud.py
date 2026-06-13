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
# CLASS DETAIL
# ==================================

def get_class_by_id(class_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        class_name
    FROM classes
    WHERE id = ?
    """, (class_id,))

    data = cursor.fetchone()

    conn.close()

    return data

def get_student_assessment(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        quiz,
        homework,
        attendance,
        assignment,
        midterm,
        final,
        participation,
        project,
        behavior,
        average
    FROM assessments
    WHERE student_id = ?
    """, (student_id,))

    data = cursor.fetchone()

    conn.close()

    return data

# ==================================
# STUDENT DETAIL
# ==================================
def get_student_detail(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT

        s.id,
        s.student_code,
        s.student_name,
        s.gender,

        c.class_name,

        a.quiz,
        a.homework,
        a.attendance,
        a.assignment,
        a.midterm,
        a.final,
        a.participation,
        a.project,
        a.behavior,
        a.average,

        p.risk_level,
        p.recommendation

    FROM students s

    JOIN classes c
        ON s.class_id = c.id

    LEFT JOIN assessments a
        ON s.id = a.student_id

    LEFT JOIN predictions p
        ON s.id = p.student_id

    WHERE s.id = ?
    """, (student_id,))

    data = cursor.fetchone()

    conn.close()

    return data

# ==================================
# STUDENT PAGE
# ==================================
def get_student_list():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        s.id,
        s.student_code,
        s.student_name,
        c.class_name,
        a.average,
        p.risk_level

    FROM students s

    JOIN classes c
        ON s.class_id = c.id

    LEFT JOIN assessments a
        ON s.id = a.student_id

    LEFT JOIN predictions p
        ON s.id = p.student_id

    ORDER BY s.student_name
    """)

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

# ==================================
# CLASS ROOM
# ==================================
def get_class_cards():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        c.id,
        c.class_name,

        COUNT(DISTINCT s.id) AS students,

        ROUND(AVG(a.average), 1) AS average,

        SUM(
            CASE
                WHEN p.risk_level = 'High'
                THEN 1
                ELSE 0
            END
        ) AS high_risk

    FROM classes c

    LEFT JOIN students s
        ON c.id = s.class_id

    LEFT JOIN assessments a
        ON s.id = a.student_id

    LEFT JOIN predictions p
        ON s.id = p.student_id

    GROUP BY c.id

    ORDER BY c.class_name
    """)

    data = cursor.fetchall()

    conn.close()

    return data

# ==================================
# TEACHER PASSWORD
# ==================================
def validate_teacher(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM teachers
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )

    teacher = cursor.fetchone()

    conn.close()

    return teacher

# ==================================
# ADMIN PASSWORD
# ==================================
def validate_admin(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM admins
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )

    admin = cursor.fetchone()

    conn.close()

    return admin

# ==================================
# ASSESSMENT
# ==================================
def get_student_dropdown():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        student_code,
        student_name
    FROM students
    ORDER BY student_name
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def update_assessment(
    student_id,
    quiz,
    homework,
    attendance,
    assignment,
    midterm,
    final,
    participation,
    project,
    behavior,
    average
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE assessments
    SET
        quiz = ?,
        homework = ?,
        attendance = ?,
        assignment = ?,
        midterm = ?,
        final = ?,
        participation = ?,
        project = ?,
        behavior = ?,
        average = ?
    WHERE student_id = ?
    """, (
        quiz,
        homework,
        attendance,
        assignment,
        midterm,
        final,
        participation,
        project,
        behavior,
        average,
        student_id
    ))

    conn.commit()
    conn.close()

def update_prediction(
    student_id,
    risk,
    recommendation
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE predictions
    SET
        risk_level = ?,
        recommendation = ?
    WHERE student_id = ?
    """, (
        risk,
        recommendation,
        student_id
    ))

    conn.commit()
    conn.close()

def get_student_id_by_dropdown(display_text):

    conn = get_connection()
    cursor = conn.cursor()

    student_code = display_text.split("(")[1].replace(")", "")

    cursor.execute("""
    SELECT id
    FROM students
    WHERE student_code = ?
    """, (student_code,))

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None

def get_student_id_by_name(student_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id
    FROM students
    WHERE student_name = ?
    """, (student_name,))

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None