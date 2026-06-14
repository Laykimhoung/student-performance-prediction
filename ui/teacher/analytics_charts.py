import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)


# ==================================
# COLORS
# ==================================

BG_COLOR = "#0F172A"

LOW_COLOR = "#10B981"
MEDIUM_COLOR = "#F59E0B"
HIGH_COLOR = "#EF4444"

TEXT_COLOR = "#E5E7EB"


# ==================================
# RISK DONUT CHART
# ==================================

def create_risk_donut_chart(
    parent,
    high_count,
    medium_count,
    low_count
):

    fig, ax = plt.subplots(
        figsize=(7, 7),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    values = [
        low_count,
        medium_count,
        high_count
    ]

    labels = [
        "Low",
        "Medium",
        "High"
    ]

    colors = [
        LOW_COLOR,
        MEDIUM_COLOR,
        HIGH_COLOR
    ]

    wedges, texts = ax.pie(
        values,
        labels=labels,
        colors=colors,
        startangle=90,
        wedgeprops={
            "width": 0.45,
            "edgecolor": BG_COLOR
        }
    )

    for text in texts:
        text.set_color("white")
        text.set_fontweight("bold")

    ax.set_title(
        "Risk Distribution",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=parent
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    return canvas


# ==================================
# ASSESSMENT BAR CHART
# ==================================

def create_assessment_chart(
    parent,
    averages
):

    labels = [
        "Attendance",
        "Quiz",
        "Homework",
        "Assignment",
        "Midterm",
        "Final",
        "Participation",
        "Project",
        "Behavior"
    ]

    fig, ax = plt.subplots(
        figsize=(12, 6),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    bars = ax.barh(
        labels,
        averages
    )

    for bar in bars:
        bar.set_color("#3B82F6")

    ax.set_xlim(0, 100)

    ax.tick_params(
        colors="white"
    )

    ax.set_title(
        "Assessment Performance",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=parent
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    return canvas


# ==================================
# SCORE DISTRIBUTION
# ==================================

def create_score_histogram(
    parent,
    scores
):

    fig, ax = plt.subplots(
        figsize=(12, 6),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    ax.hist(
        scores,
        bins=[0, 50, 60, 70, 80, 90, 100]
    )

    ax.set_title(
        "Score Distribution",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    ax.tick_params(
        colors="white"
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=parent
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    return canvas


# ==================================
# HIGH RISK STUDENTS CHART
# ==================================

def create_high_risk_chart(
    parent,
    students
):

    if not students:
        return

    names = [
        row[0]
        for row in students
    ]

    averages = [
        row[1]
        for row in students
    ]

    fig, ax = plt.subplots(
        figsize=(12, 6),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    bars = ax.barh(
        names,
        averages
    )

    for bar in bars:
        bar.set_color(HIGH_COLOR)

    ax.tick_params(
        colors="white"
    )

    ax.set_xlim(0, 100)

    ax.set_title(
        "High Risk Students",
        color="white",
        fontsize=14,
        fontweight="bold"
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=parent
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    return canvas