import random
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

        quiz = random.randint(80, 100)
        homework = random.randint(80, 100)
        attendance = random.randint(85, 100)
        assignment = random.randint(80, 100)
        midterm = random.randint(75, 100)
        final = random.randint(80, 100)
        participation = random.randint(75, 100)
        project = random.randint(80, 100)
        behavior = random.randint(85, 100)

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

        quiz = random.randint(60, 79)
        homework = random.randint(60, 79)
        attendance = random.randint(60, 79)
        assignment = random.randint(60, 79)
        midterm = random.randint(55, 79)
        final = random.randint(60, 79)
        participation = random.randint(60, 85)
        project = random.randint(60, 79)
        behavior = random.randint(70, 90)

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

        quiz = random.randint(30, 59)
        homework = random.randint(30, 59)
        attendance = random.randint(30, 59)
        assignment = random.randint(30, 59)
        midterm = random.randint(25, 59)
        final = random.randint(30, 59)
        participation = random.randint(30, 70)
        project = random.randint(30, 59)
        behavior = random.randint(50, 80)

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
        predicted_score,
        risk_level,
        recommendation
    )
    VALUES (?, ?, ?, ?)
    """, (
        student_id,
        average,
        risk,
        recommendation
    ))

conn.commit()
conn.close()

print("EduVision AI sample data inserted successfully.")