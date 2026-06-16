def generate_recommendation(
    attendance,
    quiz,
    homework,
    assignment,
    midterm,
    final,
    participation,
    project,
    behavior,
    predicted_score,
    risk_level
):

    scores = {
        "Attendance": attendance,
        "Quiz": quiz,
        "Homework": homework,
        "Assignment": assignment,
        "Midterm": midterm,
        "Final Exam": final,
        "Participation": participation,
        "Project": project,
        "Behavior": behavior
    }

    strengths = []
    weaknesses = []

    for category, score in scores.items():

        if score >= 85:
            strengths.append(category)

        elif score < 70:
            weaknesses.append(category)

    report = []

    # ==================================
    # PERFORMANCE ANALYSIS
    # ==================================

    report.append(
        "Academic Performance Analysis\n"
    )

    report.append(
        f"Predicted Score: {predicted_score:.1f}\n"
    )

    report.append(
        f"Risk Level: {risk_level}\n"
    )

    # ==================================
    # RISK ANALYSIS
    # ==================================

    if risk_level == "Low":

        report.append(
            "\nYour academic profile indicates strong overall performance "
            "with a low level of academic risk."
        )

    elif risk_level == "Medium":

        report.append(
            "\nYour academic profile indicates moderate academic risk. "
            "Several assessment areas would benefit from additional attention."
        )

    else:

        report.append(
            "\nYour academic profile indicates a high academic risk level. "
            "Immediate intervention and stronger academic support are recommended."
        )

    # ==================================
    # STRENGTHS
    # ==================================

    if strengths:

        report.append(
            "\n\nCurrent Strengths:"
        )

        for item in strengths:

            report.append(
                f"\n• {item}"
            )

    # ==================================
    # WEAKNESSES
    # ==================================

    if weaknesses:

        report.append(
            "\n\nAreas Requiring Attention:"
        )

        for item in weaknesses:

            report.append(
                f"\n• {item}"
            )

    # ==================================
    # PATTERN DETECTION
    # ==================================

    report.append(
        "\n\nPerformance Insights:"
    )

    if attendance < 60:

        report.append(
            "\n• Low attendance may be limiting understanding of classroom material."
        )

    if quiz < 70 and final < 70:

        report.append(
            "\n• Assessment results suggest difficulty retaining and applying key concepts."
        )

    if participation >= 85 and average_low(
        quiz,
        homework,
        assignment,
        midterm,
        final
    ):

        report.append(
            "\n• Classroom engagement is strong, but assessment performance indicates a need for improved study strategies."
        )

    if behavior >= 85 and risk_level != "Low":

        report.append(
            "\n• Positive behavior is evident and provides a strong foundation for future academic improvement."
        )

    # ==================================
    # ACTION PLAN
    # ==================================

    report.append(
        "\n\nRecommended Actions:"
    )

    if attendance < 70:

        report.append(
            "\n• Improve attendance consistency and avoid unnecessary absences."
        )

    if quiz < 70:

        report.append(
            "\n• Review quiz mistakes and practice similar questions weekly."
        )

    if homework < 70:

        report.append(
            "\n• Complete homework consistently and seek clarification when concepts are unclear."
        )

    if assignment < 70:

        report.append(
            "\n• Improve assignment planning and begin tasks earlier."
        )

    if midterm < 70:

        report.append(
            "\n• Strengthen preparation for major assessments through structured revision."
        )

    if final < 70:

        report.append(
            "\n• Develop a long-term examination preparation strategy."
        )

    if participation < 70:

        report.append(
            "\n• Participate more actively during classroom discussions and activities."
        )

    if project < 70:

        report.append(
            "\n• Improve project organization, research, and time management skills."
        )

    if behavior < 70:

        report.append(
            "\n• Focus on maintaining positive classroom behavior and learning habits."
        )

    # ==================================
    # OVERALL OUTLOOK
    # ==================================

    report.append(
        "\n\nOverall Outlook:"
    )

    if risk_level == "Low":

        report.append(
            "\nContinue maintaining current academic habits and performance standards."
        )

    elif risk_level == "Medium":

        report.append(
            "\nWith consistent effort and improvement in weaker areas, academic performance is expected to improve significantly."
        )

    else:

        report.append(
            "\nMeaningful improvement is achievable through stronger attendance, study habits, and targeted academic support."
        )

    return "".join(report)


def average_low(
    quiz,
    homework,
    assignment,
    midterm,
    final
):

    average = (
        quiz +
        homework +
        assignment +
        midterm +
        final
    ) / 5

    return average < 70