import random

ATTENDANCE_TEMPLATES = [

    "Improving attendance consistency may significantly strengthen understanding of classroom topics and reduce learning gaps.",

    "Regular class attendance is recommended because missed lessons can make it difficult to follow later material.",

    "Attending classes more consistently will provide greater exposure to teacher explanations and classroom discussions.",

    "Reducing unnecessary absences could lead to noticeable improvement in future assessment results.",

    "Consistent attendance is one of the strongest foundations for academic success and should remain a priority.",

    "Making a greater effort to attend all scheduled classes may help improve overall academic performance.",

    "Better attendance habits can improve both confidence and understanding of course concepts.",

    "Frequent classroom participation begins with regular attendance and consistent engagement.",

    "Attending lessons consistently can help reinforce important concepts before assessments occur.",

    "Developing stronger attendance habits may create more opportunities for academic improvement."
]

QUIZ_TEMPLATES = [

    "Reviewing quiz mistakes carefully can help identify recurring areas of misunderstanding.",

    "Completing additional practice questions may improve future quiz performance.",

    "Quiz results suggest that regular review sessions could be beneficial.",

    "Consider focusing on topics that repeatedly appear challenging during quizzes.",

    "Short weekly revision sessions may improve performance in smaller assessments.",

    "Analyzing previous quiz errors can help prevent similar mistakes in the future.",

    "Practicing under timed conditions may improve confidence during quizzes.",

    "Additional concept review before quizzes may lead to stronger results.",

    "Creating summary notes after each lesson may improve quiz preparation.",

    "Developing a consistent revision routine can strengthen quiz performance over time."
]

HOMEWORK_TEMPLATES = [

    "Completing homework consistently can reinforce concepts learned during class.",

    "Homework should be viewed as an opportunity to practice and strengthen understanding.",

    "Allocating dedicated study time for homework may improve academic consistency.",

    "Seeking clarification on difficult homework tasks can prevent misunderstandings from accumulating.",

    "Regular homework completion often leads to stronger assessment performance.",

    "Improving homework habits may strengthen long-term academic development.",

    "Completing assignments independently before seeking help can improve problem-solving skills.",

    "Using homework to review classroom material may improve retention of key concepts.",

    "Organizing homework tasks earlier can reduce stress and improve quality of work.",

    "Consistent homework effort often contributes to greater academic confidence."
]

ASSIGNMENT_TEMPLATES = [

    "Improving assignment planning and time management may lead to higher quality work.",

    "Starting assignments earlier can reduce pressure and allow more time for revision.",

    "Breaking large assignments into smaller tasks may improve productivity and organization.",

    "Assignment performance may improve through better research and preparation strategies.",

    "Reviewing assignment requirements carefully before starting can help avoid unnecessary mistakes.",

    "Developing a structured workflow may strengthen assignment completion and quality.",

    "Allocating dedicated time for assignments each week can improve consistency.",

    "Seeking feedback on completed assignments may help identify areas for improvement.",

    "Improving assignment organization can strengthen both academic performance and confidence.",

    "Careful planning and early preparation often lead to stronger assignment outcomes."
]

MIDTERM_TEMPLATES = [

    "A more structured revision plan may improve midterm examination performance.",

    "Midterm preparation could benefit from earlier and more consistent review sessions.",

    "Regular self-testing may help identify weak areas before major assessments.",

    "Focusing on difficult topics during revision may strengthen future midterm results.",

    "Developing stronger study habits before major assessments could improve performance.",

    "Reviewing class notes weekly may reduce the amount of revision required before examinations.",

    "Creating a study schedule before the midterm may improve knowledge retention.",

    "Practicing past assessment questions may increase examination confidence.",

    "Additional revision of key concepts may strengthen performance in future midterm assessments.",

    "A balanced preparation strategy across all subjects may lead to better examination outcomes."
]

FINAL_EXAM_TEMPLATES = [

    "Developing a long-term examination preparation strategy may improve final assessment performance.",

    "Starting revision earlier can reduce pressure and improve retention of important concepts.",

    "Practice examinations may help identify areas requiring additional study.",

    "Breaking revision into smaller weekly goals can make preparation more manageable.",

    "Exam performance may improve through consistent review rather than last-minute study.",

    "Creating a structured revision schedule could strengthen examination readiness.",

    "Focusing on weaker topics during revision may lead to better examination outcomes.",

    "Regular self-testing can improve confidence before major assessments.",

    "Reviewing past examination questions may help develop stronger assessment strategies.",

    "Balanced preparation across all topics may improve overall examination results."
]

PARTICIPATION_TEMPLATES = [

    "Participating more actively during lessons may strengthen understanding and confidence.",

    "Greater involvement in classroom discussions can improve engagement with course material.",

    "Asking questions when concepts are unclear may help prevent future misunderstandings.",

    "Active participation often contributes to stronger learning outcomes and classroom confidence.",

    "Sharing ideas during discussions can help reinforce understanding of key concepts.",

    "Taking a more active role during classroom activities may improve academic development.",

    "Consistent classroom participation can support both learning and communication skills.",

    "Engaging more frequently with lesson activities may improve overall performance.",

    "Participating confidently in class discussions can strengthen critical thinking abilities.",

    "Greater classroom involvement may help build stronger connections between theory and practice."
]

PROJECT_TEMPLATES = [

    "Improving project planning and organization may lead to stronger outcomes.",

    "Breaking projects into smaller milestones can improve time management and quality.",

    "Additional research and preparation may strengthen future project performance.",

    "Developing a structured project workflow can improve efficiency and consistency.",

    "Careful planning before beginning project work may reduce common mistakes.",

    "Project success often improves through stronger organization and preparation.",

    "Allocating dedicated time for project development may improve final results.",

    "Improving documentation and research skills may strengthen future project work.",

    "Setting clear project goals early can support more effective execution.",

    "Regular progress reviews may help identify and address project challenges sooner."
]

BEHAVIOR_TEMPLATES = [

    "Developing positive classroom habits may support stronger academic progress.",

    "Maintaining respectful and focused behavior can create a more productive learning environment.",

    "Improving classroom discipline may help increase concentration during lessons.",

    "Positive learning behaviors often contribute to long-term academic success.",

    "Greater focus during learning activities may improve overall performance.",

    "Strengthening self-discipline can support both academic and personal development.",

    "Maintaining a positive attitude toward learning may lead to better outcomes.",

    "Consistent learning habits can improve both confidence and achievement.",

    "Developing stronger classroom routines may support future academic growth.",

    "Positive behavior provides a foundation for continued academic improvement."
]

PATTERN_TEMPLATES = {

    "good_attendance_poor_exam": [

        "Attendance is consistently strong, but examination results suggest that key concepts may not be fully retained when working independently.",

        "Class attendance demonstrates commitment to learning, yet assessment performance indicates additional revision may be beneficial.",

        "Regular attendance is evident; however, examination results suggest that deeper understanding of course material may be required.",

        "The student appears engaged through attendance, but examination scores indicate challenges when applying knowledge during assessments.",

        "Strong attendance habits are present, although examination performance suggests revision strategies could be improved."
    ],

    "practical_strong_theory_weak": [

        "Project performance demonstrates strong practical ability, while examination results suggest theoretical understanding may require additional attention.",

        "Hands-on learning appears to be a strength, though theoretical assessment performance indicates room for improvement.",

        "The student performs well in practical tasks but may benefit from additional review of underlying concepts and theory.",

        "Project work reflects strong problem-solving skills, while examination outcomes suggest theory revision should become a higher priority.",

        "Practical application skills are evident; however, theoretical mastery appears weaker than practical performance."
    ],

    "engaged_but_low_score": [

        "Classroom engagement is strong, but current assessment results indicate that study strategies may not be producing the desired outcomes.",

        "The student actively participates in learning activities, yet academic performance suggests further support may be beneficial.",

        "Participation reflects a positive learning attitude, although assessment performance remains below potential.",

        "Strong engagement suggests motivation to learn, but current results indicate a need for more effective revision techniques.",

        "The student contributes actively in class, yet assessment outcomes suggest additional academic support may help."
    ],

    "good_behavior_high_risk": [

        "Positive classroom behavior suggests strong learning potential despite current academic challenges.",

        "The student's attitude toward learning appears constructive, providing a solid foundation for future improvement.",

        "Behavior is a clear strength and indicates that academic improvement is achievable with targeted support.",

        "Strong behavioral performance reflects maturity and willingness to learn despite current academic difficulties.",

        "Positive learning habits provide a valuable advantage when addressing current academic weaknesses."
    ],

    "homework_good_exam_weak": [

        "Homework performance is encouraging, but examination results suggest difficulties transferring knowledge to assessment situations.",

        "The student appears capable during coursework, though examination performance indicates a need for stronger test preparation.",

        "Homework results demonstrate effort and understanding, while examination scores suggest assessment techniques could be improved.",

        "Coursework performance is stronger than examination performance, indicating a need for additional exam-focused practice.",

        "Consistent homework completion suggests commitment, but examination preparation strategies may require adjustment."
    ]
}

STRENGTH_TEMPLATES = {

    "Attendance": [
        "Consistent attendance demonstrates strong commitment to learning.",
        "Regular classroom attendance supports academic success and engagement.",
        "Attendance habits indicate a positive approach toward learning."
    ],

    "Quiz": [
        "Quiz performance suggests a solid understanding of regularly assessed concepts.",
        "Strong quiz results demonstrate effective short-term knowledge retention.",
        "Performance in quizzes reflects consistent preparation."
    ],

    "Homework": [
        "Homework completion reflects a positive learning attitude and personal responsibility.",
        "Strong homework performance demonstrates commitment outside the classroom.",
        "Homework results suggest effective independent learning habits."
    ],

    "Project": [
        "Project work demonstrates strong practical and problem-solving abilities.",
        "Project performance reflects effective application of learned concepts.",
        "Practical work appears to be one of the student's strengths."
    ],

    "Behavior": [
        "Positive classroom behavior supports long-term academic success.",
        "Behavioral performance reflects maturity and learning readiness.",
        "Strong behavior provides an excellent foundation for future improvement."
    ]
}

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

    lowest_category = min(
        scores,
        key=scores.get
    )

    lowest_score = scores[
        lowest_category
    ]

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

    report.append(
        "\n\nExecutive Summary:"
    )

    if risk_level == "Low":

        report.append(
            "\nThe student is currently performing well and demonstrates strong academic stability across most assessment categories."
        )

    elif risk_level == "Medium":

        report.append(
            "\nThe student shows moderate academic risk with several areas requiring attention, but overall improvement is highly achievable."
        )

    else:

        report.append(
            "\nThe student currently faces significant academic challenges and would benefit from targeted intervention and structured support."
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

            if item in STRENGTH_TEMPLATES:

                report.append(
                    f"\n• {random.choice(STRENGTH_TEMPLATES[item])}"
                )

            else:

                report.append(
                    f"\n• Strong performance in {item}"
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

    # Good Attendance + Poor Exam

    if attendance >= 80 and final < 65:

        report.append(
            f"\n• {random.choice(PATTERN_TEMPLATES['good_attendance_poor_exam'])}"
        )

    # Strong Project + Weak Theory

    if project >= 85 and final < 65:

        report.append(
            f"\n• {random.choice(PATTERN_TEMPLATES['practical_strong_theory_weak'])}"
        )

    # High Participation + Low Average

    if participation >= 85 and average_low(
        quiz,
        homework,
        assignment,
        midterm,
        final
    ):

        report.append(
            f"\n• {random.choice(PATTERN_TEMPLATES['engaged_but_low_score'])}"
        )

    # Good Behavior + High Risk

    if behavior >= 85 and risk_level == "High":

        report.append(
            f"\n• {random.choice(PATTERN_TEMPLATES['good_behavior_high_risk'])}"
        )

    # Homework Good + Exam Weak

    if homework >= 80 and final < 65:

        report.append(
            f"\n• {random.choice(PATTERN_TEMPLATES['homework_good_exam_weak'])}"
        )

    # ==================================
    # TOP PRIORITY
    # ==================================

    report.append(
        "\n\nTop Priority Area:"
    )

    report.append(
        f"\n• {lowest_category} ({lowest_score})"
    )

    report.append(
        "\nThis area currently has the greatest impact on overall academic performance and should be addressed first."
    )

    # ==================================
    # ACTION PLAN
    # ==================================

    report.append(
        "\n\nRecommended Actions:"
    )

    if attendance < 70:

        report.append(
            f"\n• {random.choice(ATTENDANCE_TEMPLATES)}"
        )

    if quiz < 70:

        report.append(
            f"\n• {random.choice(QUIZ_TEMPLATES)}"
        )

    if homework < 70:

        report.append(
            f"\n• {random.choice(HOMEWORK_TEMPLATES)}"
        )

    if assignment < 70:

        report.append(
            f"\n• {random.choice(ASSIGNMENT_TEMPLATES)}"
        )

    if midterm < 70:

        report.append(
            f"\n• {random.choice(MIDTERM_TEMPLATES)}"
        )

    if final < 70:

        report.append(
            f"\n• {random.choice(FINAL_EXAM_TEMPLATES)}"
        )

    if participation < 70:

        report.append(
            f"\n• {random.choice(PARTICIPATION_TEMPLATES)}"
        )

    if project < 70:

        report.append(
            f"\n• {random.choice(PROJECT_TEMPLATES)}"
        )

    if behavior < 70:

        report.append(
            f"\n• {random.choice(BEHAVIOR_TEMPLATES)}"
        )

    # ==================================
    # IMPROVEMENT POTENTIAL
    # ==================================

    report.append(
        "\n\nImprovement Potential:"
    )

    if behavior >= 85 and participation >= 80:

        report.append(
            "\n• High Potential"
        )

        report.append(
            "\nThe student demonstrates positive learning habits and engagement, suggesting strong capacity for future academic growth."
        )

    elif behavior >= 70:

        report.append(
            "\n• Moderate Potential"
        )

        report.append(
            "\nThe student shows several positive indicators that could support academic improvement with consistent effort."
        )

    else:

        report.append(
            "\n• Developing Potential"
        )

        report.append(
            "\nImprovement remains achievable but may require stronger learning habits and increased academic engagement."
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