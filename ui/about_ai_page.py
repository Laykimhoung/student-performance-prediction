import customtkinter as ctk


class AboutAIPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.build_ui()

    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self,
            text="About AI",
            font=("Segoe UI", 42, "bold")
        )

        title.pack(
            anchor="w",
            padx=40,
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="How EduVision AI predicts student performance and academic risk.",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=40,
            pady=(0, 30)
        )

        # ==================================
        # MAIN CONTENT
        # ==================================
        content = ctk.CTkScrollableFrame(
            self,
            fg_color="#0F172A",
            corner_radius=20
        )

        content.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 30)
        )

        # ==================================
        # WHAT IS EDUVISION AI
        # ==================================
        ctk.CTkLabel(
            content,
            text="What is EduVision AI?",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "EduVision AI is an academic monitoring system designed "
                "to help teachers and administrators identify students "
                "who may be at academic risk. The system analyzes student "
                "performance data and provides recommendations for improvement."
            ),
            wraplength=1000,
            justify="left",
            font=("Segoe UI", 17),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=30
        )

        # ==================================
        # HOW AI WORKS
        # ==================================
        ctk.CTkLabel(
            content,
            text="How AI Works",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "Teachers enter student assessment scores into the system. "
                "The AI model analyzes performance patterns and calculates "
                "risk levels based on academic performance indicators. "
                "Students identified as at-risk receive personalized "
                "recommendations and intervention suggestions."
            ),
            wraplength=1000,
            justify="left",
            font=("Segoe UI", 17),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=30
        )

        # ==================================
        # PREDICTION FACTORS
        # ==================================
        ctk.CTkLabel(
            content,
            text="Prediction Factors",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 15)
        )

        factors_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        factors_frame.pack(
            fill="x",
            padx=30
        )

        factors = [
            ("Quiz", "#3B82F6"),
            ("Attendance", "#06B6D4"),
            ("Homework", "#8B5CF6"),
            ("Assignment", "#F59E0B"),
            ("Midterm", "#10B981"),
            ("Final Exam", "#EF4444"),
            ("Participation", "#EC4899"),
            ("Project", "#22C55E"),
            ("Behavior", "#F97316")
        ]

        for i, (factor, color) in enumerate(factors):

            card = ctk.CTkFrame(
                factors_frame,
                fg_color="#111827",
                corner_radius=15,
                width=120,
                height=60
            )

            card.grid(
                row=0,
                column=i,
                padx=8,
                pady=10
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=factor,
                font=("Segoe UI", 16, "bold"),
                text_color=color
            ).pack(
                expand=True
            )

        # ==================================
        # AI OUTPUT
        # ==================================
        ctk.CTkLabel(
            content,
            text="AI Output",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "Based on student performance data, EduVision AI predicts "
                "academic risk levels and generates recommendations. "
                "Students may be classified as Low Risk, Medium Risk, or "
                "High Risk depending on their overall performance."
            ),
            wraplength=1000,
            justify="left",
            font=("Segoe UI", 17),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=30
        )

        # ==================================
        # RISK LEVELS
        # ==================================
        risk_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        risk_frame.pack(
            fill="x",
            padx=30,
            pady=(20, 20)
        )

        risks = [
            ("Low Risk", "#10B981"),
            ("Medium Risk", "#F59E0B"),
            ("High Risk", "#EF4444")
        ]

        for title, color in risks:

            card = ctk.CTkFrame(
                risk_frame,
                fg_color="#111827",
                corner_radius=15,
                width=220,
                height=90
            )

            card.pack(
                side="left",
                padx=10
            )

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 18, "bold"),
                text_color=color
            ).pack(
                expand=True
            )

        # ==================================
        # FOOTER
        # ==================================
        footer = ctk.CTkLabel(
            content,
            text="EduVision AI • Artificial Intelligence Academic Monitoring System",
            font=("Segoe UI", 13),
            text_color="#64748B"
        )

        footer.pack(
            pady=(20, 25)
        )