import customtkinter as ctk

from database.crud import (
    get_all_class_names,
    get_analytics_summary,
    get_assessment_averages,
    get_risk_distribution,
    get_high_risk_students,
    get_score_distribution
)

from ui.teacher.analytics_charts import (
    create_risk_donut_chart,
    create_assessment_chart,
    create_score_histogram,
    create_high_risk_chart
)


class AnalyticsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        class_data=None,
        back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.class_data = class_data
        self.back_command = back_command

        # ==========================
        # CURRENT CLASS
        # ==========================
        self.selected_class = (
            class_data["name"]
            if class_data
            else None
        )

        # ==========================
        # DATA
        # ==========================
        self.load_data()

        # ==========================
        # BUILD UI
        # ==========================
        self.build_ui()

    # ==================================
    # LOAD DATA
    # ==================================
    def load_data(self):

        summary = get_analytics_summary(
            self.selected_class
        )

        self.total_students = summary[0] or 0
        self.high_risk = summary[1] or 0
        self.medium_risk = summary[2] or 0
        self.low_risk = summary[3] or 0

        self.assessment_data = (
            get_assessment_averages(
                self.selected_class
            )
        )

        self.risk_distribution = (
            get_risk_distribution(
                self.selected_class
            )
        )

        self.high_risk_students = (
            get_high_risk_students(
                self.selected_class
            )
        )

        self.score_distribution = (
            get_score_distribution(
                self.selected_class
            )
        )

    # ==================================
    # REFRESH PAGE
    # ==================================
    def refresh_page(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.load_data()

        self.build_ui()

    # ==================================
    # CLASS CHANGED
    # ==================================
    def on_class_change(
        self,
        selected_class
    ):

        self.selected_class = selected_class

        self.refresh_page()

    # ==================================
    # BUILD UI
    # ==================================
    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=(25, 10)
        )

        title_frame = ctk.CTkFrame(
            top_bar,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_frame,
            text="Analytics & Risk Prediction",
            font=("Segoe UI", 40, "bold")
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            title_frame,
            text="Analyze student performance and identify intervention needs",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        ).pack(
            anchor="w"
        )

        # ==================================
        # BACK BUTTON
        # ==================================
        if self.back_command:

            back_btn = ctk.CTkButton(
                top_bar,
                text="← Back",
                width=140,
                height=46,
                corner_radius=16,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold"),
                command=self.back_command
            )

            back_btn.pack(
                side="right"
            )

        # ==================================
        # FILTER BAR
        # ==================================
        filter_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        filter_bar.pack(
            fill="x",
            padx=35,
            pady=20
        )

        # ==============================
        # CLASSROOM MODE
        # ==============================
        if self.class_data:

            class_box = ctk.CTkFrame(
                filter_bar,
                fg_color="#111827",
                corner_radius=14,
                width=220,
                height=46
            )

            class_box.pack(
                side="left"
            )

            class_box.pack_propagate(False)

            ctk.CTkLabel(
                class_box,
                text=self.selected_class,
                font=("Segoe UI", 15, "bold")
            ).pack(
                pady=10
            )

        # ==============================
        # SIDEBAR MODE
        # ==============================
        else:

            class_dropdown = ctk.CTkComboBox(
                filter_bar,
                width=220,
                height=46,
                values=get_all_class_names(),
                command=self.on_class_change,
                corner_radius=14,
                button_color="#EF4444",
                button_hover_color="#DC2626"
            )

            class_dropdown.pack(
                side="left"
            )

            if self.selected_class:

                class_dropdown.set(
                    self.selected_class
                )

            else:

                classes = get_all_class_names()

                if classes:

                    if self.selected_class is None:

                        self.selected_class = classes[0]

                        class_dropdown.set(
                            classes[0]
                        )

                        self.after(
                            100,
                            lambda: self.on_class_change(classes[0])
                        )

        # ==================================
        # CALCULATE HEALTH SCORE
        # ==================================
        health_score = 0

        if self.total_students > 0:

            health_score = round(
                (
                    (self.low_risk * 100) +
                    (self.medium_risk * 70) +
                    (self.high_risk * 30)
                )
                /
                self.total_students,
                1
            )

        # ==================================
        # KPI CARDS
        # ==================================
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )

        stats = [
            (
                str(self.total_students),
                "Students",
                "#3B82F6"
            ),
            (
                str(self.high_risk),
                "High Risk",
                "#EF4444"
            ),
            (
                str(self.medium_risk),
                "Medium Risk",
                "#F59E0B"
            ),
            (
                f"{health_score}%",
                "Health Score",
                "#10B981"
            )
        ]

        for value, label, color in stats:

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                corner_radius=28,
                height=105
            )

            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=10
            )

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 28, "bold"),
                text_color=color
            ).pack(
                pady=(28, 5)
            )

            ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            ).pack()
        
        # ==================================
        # MAIN BODY
        # ==================================
        body = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        # ==================================
        # RISK DONUT CHART
        # ==================================
        
        donut_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=550,
            width=1200
        )

        donut_frame.pack_propagate(False)

        donut_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 20)
        )

        create_risk_donut_chart(
            donut_frame,
            self.high_risk,
            self.medium_risk,
            self.low_risk
        )

        # ==================================
        # ASSESSMENT BAR CHART
        # ==================================
        assessment_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=550,
            width=1200
        )

        assessment_frame.pack_propagate(False)

        assessment_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 20)
        )

        assessment_values = []

        if self.assessment_data:

            assessment_values = [
                value if value is not None else 0
                for value in self.assessment_data
            ]

        create_assessment_chart(
            assessment_frame,
            assessment_values
        )

        # ==================================
        # SCORE HISTOGRAM
        # ==================================
        histogram_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=550,
            width=1200
        )

        histogram_frame.pack_propagate(False)

        histogram_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 20)
        )

        create_score_histogram(
            histogram_frame,
            self.score_distribution
        )

        # ==================================
        # HIGH RISK CHART
        # ==================================
        risk_students_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=550,
            width=1200
        )

        risk_students_frame.pack_propagate(False)

        risk_students_frame.pack(
            fill="both",
            expand=True,
            pady=(0, 20)
        )

        create_high_risk_chart(
            risk_students_frame,
            self.high_risk_students
        )

        # ==================================
        # AI INSIGHTS SECTION
        # ==================================
        insights_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        insights_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )

        ctk.CTkLabel(
            insights_frame,
            text="AI Insights & Recommendations",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        insights = []

        # ==========================
        # RISK INSIGHTS
        # ==========================
        if self.high_risk > 0:

            insights.append(
                f"⚠ {self.high_risk} students are currently classified as High Risk."
            )

        else:

            insights.append(
                "✓ No High Risk students detected."
            )

        if self.medium_risk > 0:

            insights.append(
                f"⚠ {self.medium_risk} students require monitoring."
            )

        if self.low_risk > 0:

            insights.append(
                f"✓ {self.low_risk} students are performing well."
            )

        # ==========================
        # ASSESSMENT INSIGHTS
        # ==========================
        if self.assessment_data:

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

            values = [
                value if value is not None else 0
                for value in self.assessment_data
            ]

            lowest_index = values.index(
                min(values)
            )

            highest_index = values.index(
                max(values)
            )

            insights.append(
                f"📉 Lowest performance area: {labels[lowest_index]} ({values[lowest_index]}%)."
            )

            insights.append(
                f"📈 Strongest area: {labels[highest_index]} ({values[highest_index]}%)."
            )

        # ==========================
        # DISPLAY INSIGHTS
        # ==========================
        for text in insights:

            ctk.CTkLabel(
                insights_frame,
                text=text,
                font=("Segoe UI", 15),
                text_color="#CBD5E1",
                justify="left"
            ).pack(
                anchor="w",
                padx=25,
                pady=5
            )

        # ==================================
        # RECOMMENDATION CARD
        # ==================================
        recommendation_card = ctk.CTkFrame(
            insights_frame,
            fg_color="#111827",
            corner_radius=20
        )

        recommendation_card.pack(
            fill="x",
            padx=25,
            pady=25
        )

        ctk.CTkLabel(
            recommendation_card,
            text="Recommended Action",
            font=("Segoe UI", 20, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        recommendation_text = ""

        if self.high_risk > 0:

            recommendation_text = (
                "Prioritize intervention sessions for High Risk students. "
                "Review attendance, quiz performance and assignment completion. "
                "Schedule teacher-parent discussions where necessary."
            )

        elif self.medium_risk > 0:

            recommendation_text = (
                "Continue monitoring Medium Risk students and provide additional "
                "academic support before risk levels increase."
            )

        else:

            recommendation_text = (
                "Current class performance is healthy. Continue reinforcement "
                "activities and maintain academic engagement."
            )

        ctk.CTkLabel(
            recommendation_card,
            text=recommendation_text,
            wraplength=900,
            justify="left",
            font=("Segoe UI", 15),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )