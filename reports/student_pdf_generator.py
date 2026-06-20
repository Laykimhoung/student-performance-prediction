from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Paragraph
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import pagesizes
from datetime import datetime
from tkinter import filedialog


def export_student_pdf(student):

    # ==================================
    # SAVE LOCATION
    # ==================================
    file_path = filedialog.asksaveasfilename(
        title="Save Student Report",
        defaultextension=".pdf",
        initialfile=f'{student["name"]}_report.pdf',
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    # ==================================
    # PDF DOCUMENT
    # ==================================
    doc = SimpleDocTemplate(
        str(file_path),
        pagesize=pagesizes.A4,
        topMargin=35,
        bottomMargin=35,
        leftMargin=35,
        rightMargin=35
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    average = student["average"]

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
            f'Student Performance Report - {student["name"]}',
            heading_style
        )
    )

    story.append(
        Paragraph(
            f'Generated on: '
            f'{datetime.now().strftime("%d/%m/%Y")}',
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================
    # STUDENT INFORMATION
    # ==================================
    story.append(
        Paragraph(
            "Student Information",
            heading_style
        )
    )

    info_data = [
        ["Student", student["name"]],
        ["ID", student["id"]],
        ["Class", student["class"]],
        ["Average Score", f"{average}%"],
        ["Predicted Score", f'{student["predicted_score"]:.1f}%'],
        ["Risk Level", student["risk"]]
    ]

    info_table = Table(
        info_data,
        colWidths=[180, 250]
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
        Spacer(1, 25)
    )

    # ==================================
    # PERFORMANCE SUMMARY
    # ==================================
    story.append(
        Paragraph(
            "Performance Summary",
            heading_style
        )
    )

    summary_data = [
        ["Attendance", student["attendance"]],
        ["Quiz", student["quiz"]],
        ["Homework", student["homework"]],
        ["Assignment", student["assignment"]],
        ["Midterm", student["midterm"]],
        ["Final", student["final"]],
        ["Participation", student["participation"]],
        ["Project", student["project"]],
        ["Behavior", student["behavior"]],
        ["Average", f"{average}%"]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[220, 180]
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

    story.append(
        Spacer(1, 25)
    )

    # ==================================
    # AI RISK PREDICTION
    # ==================================
    story.append(
        Paragraph(
            "AI Risk Prediction",
            heading_style
        )
    )

    risk_color = "#DCFCE7"

    if student["risk"] == "Medium":
        risk_color = "#FEF3C7"

    elif student["risk"] == "High":
        risk_color = "#FEE2E2"

    risk_table = Table(
        [
            ["Predicted Score", f'{student["predicted_score"]:.1f}%'],
            ["Risk Level", student["risk"]]
        ],
        colWidths=[200, 200]
    )

    risk_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0),
        colors.HexColor("#1E3A8A")),

        ("TEXTCOLOR", (0, 0), (0, 0),
        colors.white),

        ("BACKGROUND", (1, 0), (1, 0),
        colors.HexColor(risk_color)),

        ("FONTNAME", (0, 0), (-1, -1),
        "Helvetica-Bold"),

        ("GRID", (0, 0), (-1, -1),
        1, colors.black),

        ("ALIGN", (0, 0), (-1, -1),
        "CENTER")
    ]))

    story.append(risk_table)

    story.append(
        Spacer(1, 25)
    )

    # ==================================
    # AI RISK ANALYSIS
    # ==================================
    story.append(
        Paragraph(
            "AI Risk Analysis",
            heading_style
        )
    )

    story.append(
        Paragraph(
            student.get(
                "recommendation",
                "No AI analysis available."
            ).replace("\n", "<br/>"),
            body_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # ==================================
    # PERFORMANCE STATUS
    # ==================================
    story.append(
        Paragraph(
            "Performance Status",
            heading_style
        )
    )

    if student["risk"] == "Low":

        performance_text = (
            "The student demonstrates strong academic performance "
            "and is currently classified as low risk by the AI model."
        )

    elif student["risk"] == "Medium":

        performance_text = (
            "The student demonstrates moderate academic risk and "
            "should continue improving weaker assessment areas."
        )

    else:

        performance_text = (
            "The student is classified as high risk and would benefit "
            "from additional academic support and intervention."
        )

    story.append(
        Paragraph(
            performance_text,
            body_style
        )
    )

    story.append(
        Spacer(1, 25)
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
        f"Student PDF exported: {file_path}"
    )

    return str(file_path)