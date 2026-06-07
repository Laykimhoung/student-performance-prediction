from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Paragraph
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from pathlib import Path
from datetime import datetime


def export_class_pdf(class_data, students):

    # ==================================
    # SAVE LOCATION
    # ==================================
    downloads_path = Path.home() / "Downloads"

    file_name = (
        f'{class_data["name"].replace(" ", "_")}'
        f'_report.pdf'
    )

    file_path = downloads_path / file_name

    # ==================================
    # PDF DOCUMENT
    # ==================================
    doc = SimpleDocTemplate(
        str(file_path),
        pagesize=landscape(A4),
        topMargin=30,
        bottomMargin=30,
        leftMargin=25,
        rightMargin=25
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    # ==================================
    # HEADER
    # ==================================
    story.append(
        Paragraph(
            "EduVision AI",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"Student Performance Report - {class_data['name']}",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d/%m/%Y')}",
            body_style
        )
    )

    story.append(Spacer(1, 20))

    # ==================================
    # CLASS INFORMATION
    # ==================================
    story.append(
        Paragraph(
            "Class Information",
            heading_style
        )
    )

    summary_data = [
        ["Class", class_data["name"]],
        ["Students", class_data["students"]],
        ["Attendance", f'{class_data["attendance"]}%'],
        ["Average", f'{class_data["average"]}%'],
        ["At Risk", class_data["risk"]]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[180, 300]
    )

    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (0, -1),
         colors.white),

        ("BACKGROUND", (1, 0), (1, -1),
         colors.HexColor("#F8FAFC")),

        ("FONTNAME", (0, 0), (-1, -1),
         "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER"),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE")
    ]))

    story.append(summary_table)

    story.append(Spacer(1, 25))

    # ==================================
    # STUDENT LIST
    # ==================================
    story.append(
        Paragraph(
            f"{class_data['name']} Student List",
            heading_style
        )
    )

    table_data = [[
        "ID",
        "Student",
        "Attendance",
        "Quiz",
        "Homework",
        "Assignment",
        "Midterm",
        "Final",
        "Participation",
        "Project",
        "Behavior",
        "Risk"
    ]]

    for student in students:

        table_data.append([
            student["id"],
            student["name"],
            student["attendance"],
            student["quiz"],
            student["homework"],
            student["assignment"],
            student["midterm"],
            student["final"],
            student["participation"],
            student["project"],
            student["behavior"],
            student["risk"]
        ])

    student_table = Table(
        table_data,
        colWidths=[
            40,   # ID
            80,   # Student
            60,   # Attendance
            45,   # Quiz
            60,   # Homework
            65,   # Assignment
            55,   # Midterm
            45,   # Final
            70,   # Participation
            50,   # Project
            55,   # Behavior
            45    # Risk
        ]
    )

    style = [
        ("BACKGROUND", (0, 0), (-1, 0),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (-1, 0),
         colors.white),

        ("FONTNAME", (0, 0), (-1, 0),
         "Helvetica-Bold"),

        ("FONTSIZE", (0, 0), (-1, -1), 8),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER"),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE")
    ]

    # ==================================
    # RISK COLORS
    # ==================================
    for row_index, student in enumerate(
        students,
        start=1
    ):

        risk = student["risk"]

        if risk == "Low":
            risk_color = colors.HexColor("#DCFCE7")

        elif risk == "Medium":
            risk_color = colors.HexColor("#FEF3C7")

        else:
            risk_color = colors.HexColor("#FEE2E2")

        style.append((
            "BACKGROUND",
            (-1, row_index),
            (-1, row_index),
            risk_color
        ))

    student_table.setStyle(
        TableStyle(style)
    )

    story.append(student_table)

    story.append(Spacer(1, 25))

    # ==================================
    # AI RECOMMENDATION
    # ==================================
    story.append(
        Paragraph(
            "AI Recommendation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "Students with weak attendance and unstable "
            "academic performance should receive additional "
            "intervention, monitoring, and tutoring.",
            body_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by EduVision AI",
            body_style
        )
    )

    # ==================================
    # BUILD PDF
    # ==================================
    doc.build(story)

    print(
        f"PDF exported: {file_path}"
    )

    return str(file_path)