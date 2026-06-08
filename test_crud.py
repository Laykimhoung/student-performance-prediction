from database.crud import *

print(
    "Students:",
    get_total_students()
)

print(
    "Classes:",
    get_total_classes()
)

print(
    "Teachers:",
    get_total_teachers()
)

print(
    "High Risk:",
    get_high_risk_students()
)