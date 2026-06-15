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

    if (
        high_count == 0
        and medium_count == 0
        and low_count == 0
    ):
        return

    fig, ax = plt.subplots(
        figsize=(5.5, 5.5),
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
        text.set_fontsize(11)
        text.set_fontweight("bold")

    ax.set_title(
        "Risk Distribution",
        color="white",
        fontsize=16,
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

    if not averages:
        return

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
        figsize=(6, 4),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    ax.bar(
        labels,
        averages,
        color="#3B82F6"
    )

    plt.setp(
        ax.get_xticklabels(),
        rotation=25,
        ha="right"
    )

    ax.set_ylim(0, 100)

    ax.grid(
        axis="y",
        alpha=0.25,
        linestyle="--"
    )
    
    ax.tick_params(
        colors="white"
    )

    ax.set_title(
        "Assessment Performance",
        color="white",
        fontsize=16,
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
# SCORE TREND
# ==================================

def create_score_histogram(
    parent,
    scores
):

    if not scores:
        return

    scores = sorted(scores)

    fig, ax = plt.subplots(
        figsize=(6, 4),
        facecolor=BG_COLOR
    )

    ax.set_facecolor(BG_COLOR)

    ax.plot(
        range(len(scores)),
        scores,
        marker="o",
        linewidth=3,
        color="#10B981"
    )

    ax.fill_between(
        range(len(scores)),
        scores,
        alpha=0.25,
        color="#10B981"
    )

    ax.set_ylim(0, 100)

    ax.grid(
        alpha=0.25,
        linestyle="--"
    )
    
    ax.tick_params(
        colors="white"
    )

    ax.set_title(
        "Score Distribution",
        color="white",
        fontsize=16,
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
