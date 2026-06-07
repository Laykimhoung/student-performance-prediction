from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Paragraph,
    PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from pathlib import Path
from datetime import datetime


def calculate_average(student):

    scores = [
        student["quiz"],
        student["homework"],
        student["assignment"],
        student["midterm"],
        student["final"],
        student["participation"],
        student["project"],
        student["behavior"]
    ]

    return round(
        sum(scores) / len(scores),
        1
    )


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
    # RISK COUNTS
    # ==================================
    high_risk = [
        s for s in students
        if s["risk"] == "High"
    ]

    medium_risk = [
        s for s in students
        if s["risk"] == "Medium"
    ]

    low_risk = [
        s for s in students
        if s["risk"] == "Low"
    ]

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
            f"Generated on: "
            f"{datetime.now().strftime('%d/%m/%Y')}",
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================
    # CLASS INFORMATION
    # ==================================
    story.append(
        Paragraph(
            "Class Information",
            heading_style
        )
    )

    info_data = [
        ["Class", class_data["name"]],
        ["Students", class_data["students"]],
        ["Attendance", f'{class_data["attendance"]}%'],
        ["Average", f'{class_data["average"]}%'],
        ["Generated", datetime.now().strftime("%d/%m/%Y")]
    ]

    info_table = Table(
        info_data,
        colWidths=[180, 300]
    )

    info_table.setStyle(TableStyle([
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

    story.append(info_table)

    story.append(
        Spacer(1, 20)
    )

    # ==================================
    # CLASS STATISTICS
    # ==================================
    story.append(
        Paragraph(
            "Class Statistics",
            heading_style
        )
    )

    stats_data = [
        [
            "Students",
            "Attendance",
            "Average",
            "High Risk",
            "Medium Risk",
            "Low Risk"
        ],
        [
            class_data["students"],
            f'{class_data["attendance"]}%',
            f'{class_data["average"]}%',
            len(high_risk),
            len(medium_risk),
            len(low_risk)
        ]
    ]

    stats_table = Table(
        stats_data,
        colWidths=[90] * 6
    )

    stats_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (-1, 0),
         colors.white),

        ("FONTNAME", (0, 0), (-1, 0),
         "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER")
    ]))

    story.append(stats_table)

    story.append(
        Spacer(1, 25)
    )

    # ==================================
    # STUDENT PERFORMANCE TABLE
    # ==================================
    story.append(
        Paragraph(
            "Student Performance",
            heading_style
        )
    )

    table_data = [[
        "ID",
        "Student",
        "Attend",
        "Quiz",
        "HW",
        "Assign",
        "Mid",
        "Final",
        "Part",
        "Project",
        "Behavior",
        "Average",
        "Risk"
    ]]

    for student in students:

        average = calculate_average(
            student
        )

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
            average,
            student["risk"]
        ])

    student_table = Table(
        table_data,
        colWidths=[
            35,
            70,
            45,
            40,
            40,
            50,
            40,
            40,
            45,
            45,
            50,
            50,
            45
        ]
    )

    style = [
        ("BACKGROUND", (0, 0), (-1, 0),
         colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (-1, 0),
         colors.white),

        ("FONTNAME", (0, 0), (-1, 0),
         "Helvetica-Bold"),

        ("FONTSIZE", (0, 0), (-1, -1),
         8),

        ("GRID", (0, 0), (-1, -1),
         1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
         "CENTER"),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE")
    ]

    for row_index, student in enumerate(
        students,
        start=1
    ):

        if student["risk"] == "Low":

            risk_color = colors.HexColor(
                "#DCFCE7"
            )

        elif student["risk"] == "Medium":

            risk_color = colors.HexColor(
                "#FEF3C7"
            )

        else:

            risk_color = colors.HexColor(
                "#FEE2E2"
            )

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

    story.append(
        Spacer(1, 25)
    )

    # ==================================
    # RISK SUMMARY
    # ==================================
    story.append(
        Paragraph(
            "Risk Summary",
            heading_style
        )
    )

    risk_text = "<br/>"

    risk_text += "<b>High Risk Students</b><br/>"

    if high_risk:

        for student in high_risk:
            risk_text += f"• {student['name']}<br/>"

    else:
        risk_text += "None<br/>"

    risk_text += "<br/><b>Medium Risk Students</b><br/>"

    if medium_risk:

        for student in medium_risk:
            risk_text += f"• {student['name']}<br/>"

    else:
        risk_text += "None<br/>"

    risk_text += "<br/><b>Low Risk Students</b><br/>"

    if low_risk:

        for student in low_risk:
            risk_text += f"• {student['name']}<br/>"

    else:
        risk_text += "None<br/>"

    story.append(
        Paragraph(
            risk_text,
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================
    # AI RECOMMENDATION
    # ==================================
    story.append(
        Paragraph(
            "AI Recommendation",
            heading_style
        )
    )

    recommendations = [
        "Monitor attendance below 65%.",
        "Provide tutoring support for weak students.",
        "Schedule intervention for High Risk students.",
        "Review quiz performance trends monthly.",
        "Continue mentoring Low Risk students."
    ]

    recommendation_text = ""

    for item in recommendations:

        recommendation_text += (
            f"• {item}<br/>"
        )

    story.append(
        Paragraph(
            recommendation_text,
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

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