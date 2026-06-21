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

first_names = [
    "Lim", "Chan", "Kim", "Chea", "Seng",
    "Seng", "Ly", "Horn", "Naing", "Keo",
    "Heng", "In", "Eiv", "Pich", "Hong",
    "Mom", "Vuth", "Chhay", "Hak", "Dara",
    "Chhoung", "Sim", "Lay", "Mao", "Prak"   
]

last_names = [
    "Brathna", "Sophana", "Kimhoung", "Visal", "Sonita",
    "ChanNarith", "Sreypich", "Roth", "ChanDana", "Panha",
    "Anna", "Pisey", "Vannat", "Sokuntheary", "Nary",
    "Socheat", "Ratanak", "Phanith", "Kanha", "RithyVireak",
    "Sereyboth", "Thida", "Niza", "Youe", "Sovannara"
]

student_id = 1
used_names = set()

for class_id in range(1, 7):

    for i in range(100):

        while True:

            name = (
                f"{random.choice(first_names)} "
                f"{random.choice(last_names)}"
            )

            if name not in used_names:

                used_names.add(name)

                break

        code = f"AU{student_id:03d}"

        gender = "Male" if i % 2 == 0 else "Female"

        cursor.execute("""
        INSERT INTO students
        (student_code, student_name, gender, class_id)
        VALUES (?, ?, ?, ?)
        """, (
            code,
            name,
            gender,
            class_id
        ))

        student_id += 1

# ==================================
# ASSESSMENTS
# ==================================

cursor.execute("SELECT id FROM students")
students = cursor.fetchall()

for student_id, in students:

    risk = random.choices(
        ["Low", "Medium", "High"],
        weights=[40, 30, 30],
        k=1
    )[0]

    if risk == "Low":

        quiz = random.randint(80, 100)
        homework = random.randint(75, 100)
        attendance = random.randint(85, 100)
        assignment = random.randint(75, 100)
        midterm = random.randint(75, 100)
        final = random.randint(80, 100)
        participation = random.randint(70, 100)
        project = random.randint(75, 100)
        behavior = random.randint(85, 100)

    elif risk == "Medium":

        quiz = random.randint(60, 85)
        homework = random.randint(60, 85)
        attendance = random.randint(60, 85)
        assignment = random.randint(60, 85)
        midterm = random.randint(55, 85)
        final = random.randint(60, 85)
        participation = random.randint(55, 90)
        project = random.randint(60, 85)
        behavior = random.randint(70, 95)

    else:

        high_type = random.choice(
            ["weak", "very_weak", "critical"]
        )

        if high_type == "weak":

            low = 20
            high = 49

        elif high_type == "very_weak":

            low = 10
            high = 30

        else:

            low = 1
            high = 15

        quiz = random.randint(low, high)
        homework = random.randint(low, high)
        attendance = random.randint(low, high)
        assignment = random.randint(low, high)
        midterm = random.randint(low, high)
        final = random.randint(low, high)
        participation = random.randint(low, high)
        project = random.randint(low, high)
        behavior = random.randint(low, high)

    average = round(
        (
            quiz +
            homework +
            attendance +
            assignment +
            midterm +
            final +
            participation +
            project +
            behavior
        ) / 9,
        1
    )

    if risk == "Low":
        recommendation = "Maintain current performance."

    elif risk == "Medium":
        recommendation = "Needs additional monitoring."

    else:
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