from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

# ==================================
# ADMIN
# ==================================

cursor.execute("""
INSERT INTO admins (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

# ==================================
# TEACHERS
# ==================================

teachers = [
    ("teacher1", "123", "Mr. John"),
    ("teacher2", "123", "Mrs. Lina"),
    ("teacher3", "123", "Mr. David"),
    ("teacher4", "123", "Mrs. Sara"),
    ("teacher5", "123", "Mr. Michael"),
    ("teacher6", "123", "Dr. Alex")
]

cursor.executemany("""
INSERT INTO teachers
(username, password, full_name)
VALUES (?, ?, ?)
""", teachers)

# ==================================
# CLASSES
# ==================================

classes = [
    ("AU-IT", 1),
    ("AU-CS", 2),
    ("AU-ITSD", 3),
    ("AU-ITE", 4),
    ("AU-MIS", 5),
    ("AU-ML&AI", 6)
]

cursor.executemany("""
INSERT INTO classes
(class_name, teacher_id)
VALUES (?, ?)
""", classes)

# ==================================
# STUDENTS
# ==================================

names = [
    "Dara", "Sokha", "Kimlong", "Visal", "Nita",
    "Chantha", "Sreypich", "Rith", "Kosal", "Panha",
    "Bopha", "Pisey", "Vannak", "Sokunthea", "Malis",
    "Socheat", "Ratanak", "Sophea", "Kanha", "Mony",
    "Ravy", "Thida", "Sokly", "Dalin", "Narin"
]

student_id = 1

for class_id in range(1, 7):

    for i in range(25):

        name = names[i]

        code = f"AU{student_id:03d}"

        gender = "Male" if i % 2 == 0 else "Female"

        cursor.execute("""
        INSERT INTO students
        (student_code, student_name, gender, class_id)
        VALUES (?, ?, ?, ?)
        """, (
            code,
            f"{name} {class_id}",
            gender,
            class_id
        ))

        student_id += 1

# ==================================
# ASSESSMENTS
# ==================================

cursor.execute("SELECT id FROM students")
students = cursor.fetchall()

for index, (student_id,) in enumerate(students):

    # LOW RISK
    if index < 90:

        quiz = 85
        homework = 88
        attendance = 92
        assignment = 86
        midterm = 84
        final = 90
        participation = 91
        project = 87
        behavior = 95

        average = round(
            (
                quiz + homework + attendance +
                assignment + midterm + final +
                participation + project + behavior
            ) / 9,
            1
        )

        risk = "Low"
        recommendation = "Maintain current performance."

    # MEDIUM RISK
    elif index < 130:

        quiz = 72
        homework = 70
        attendance = 75
        assignment = 73
        midterm = 68
        final = 74
        participation = 76
        project = 71
        behavior = 80

        average = round(
            (
                quiz + homework + attendance +
                assignment + midterm + final +
                participation + project + behavior
            ) / 9,
            1
        )

        risk = "Medium"
        recommendation = "Needs additional monitoring."

    # HIGH RISK
    else:

        quiz = 55
        homework = 58
        attendance = 60
        assignment = 52
        midterm = 50
        final = 57
        participation = 61
        project = 54
        behavior = 65

        average = round(
            (
                quiz + homework + attendance +
                assignment + midterm + final +
                participation + project + behavior
            ) / 9,
            1
        )

        risk = "High"
        recommendation = "Immediate intervention recommended."

    cursor.execute("""
    INSERT INTO assessments
    (
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
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
    ))

    cursor.execute("""
    INSERT INTO predictions
    (
        student_id,
        risk_level,
        recommendation
    )
    VALUES (?, ?, ?)
    """, (
        student_id,
        risk,
        recommendation
    ))

conn.commit()
conn.close()

print("EduVision AI sample data inserted successfully.")