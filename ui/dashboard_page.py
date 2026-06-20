import customtkinter as ctk

from database.crud import (
    get_total_students,
    get_total_teachers,
    get_total_classes
)

class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.build_ui()

    def build_ui(self):

        # ==================================
        # HERO SECTION
        # ==================================
        hero = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        hero.pack(
            fill="x",
            padx=45,
            pady=(30, 20)
        )

        title = ctk.CTkLabel(
            hero,
            text="Welcome to EduVision AI",
            font=("Segoe UI", 48, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            hero,
            text="AI-Enhanced Student Performance Prediction and Management System",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )
        subtitle.pack(anchor="w", pady=(8, 0))

        ctk.CTkLabel(
            hero,
            text="Monitor • Predict • Improve",
            font=("Segoe UI", 18, "bold"),
            text_color="#3B82F6"
        ).pack(
            anchor="w",
            pady=(10, 0)
        )

        # ==================================
        # STATS PREVIEW
        # ==================================
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=45,
            pady=(0, 30)
        )

        stats_frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        stats = [
            (str(get_total_students()), "Students", "#3B82F6"),
            (str(get_total_teachers()), "Teachers", "#EF4444"),
            (str(get_total_classes()), "Classes", "#8B5CF6"),
            ("AI Ready", "Prediction System", "#10B981")
        ]

        for i, (number, label, color) in enumerate(stats):

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                corner_radius=28,
                border_width=1,
                border_color="#1E293B",
                height=160
            )

            card.grid(
                row=0,
                column=i,
                padx=12,
                sticky="nsew"
            )

            accent = ctk.CTkFrame(
                card,
                fg_color=color,
                height=5,
                corner_radius=100
            )

            accent.pack(
                fill="x",
                padx=22,
                pady=(22, 22)
            )

            number_label = ctk.CTkLabel(
                card,
                text=number,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            )
            number_label.pack()

            label_widget = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 16),
                text_color="#CBD5E1"
            )
            label_widget.pack(pady=(6, 18))

        # ==================================
        # FEATURE SECTION
        # ==================================
        features_title = ctk.CTkLabel(
            self,
            text="Core Features",
            font=("Segoe UI", 34, "bold")
        )
        features_title.pack(
            anchor="w",
            padx=45,
            pady=(5, 20)
        )

        features_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        features_frame.pack(
            fill="x",
            padx=45,
            pady=(0, 35)
        )

        for col in range(3):

            features_frame.grid_columnconfigure(
                col,
                weight=1
            )

        features = [
            (
                "Student Management",
                "Manage students, classrooms and academic records.",
                "#3B82F6"
            ),
            (
                "Teacher Management",
                "Assign teachers and organize classrooms efficiently.",
                "#EF4444"
            ),
            (
                "AI Prediction",
                "Detect at-risk students and recommend interventions.",
                "#10B981"
            )
        ]

        for i, (title, desc, color) in enumerate(features):

            card = ctk.CTkFrame(
                features_frame,
                fg_color="#0F172A",
                corner_radius=28,
                border_width=1,
                border_color="#1E293B",
                height=240
            )

            card.grid_propagate(False)

            card.grid(
                row=0,
                column=i,
                padx=8,
                sticky="ew"
            )

            top_line = ctk.CTkFrame(
                card,
                fg_color=color,
                height=5,
                corner_radius=100
            )

            top_line.pack(
                fill="x",
                padx=24,
                pady=(25, 25)
            )

            title_label = ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 26, "bold")
            )
            title_label.pack(anchor="w", padx=24)

            desc_label = ctk.CTkLabel(
                card,
                text=desc,
                wraplength=300,
                justify="left",
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            )

            desc_label.pack(
                anchor="w",
                padx=24,
                pady=(12, 30)
            )
        footer = ctk.CTkLabel(
            self,
            text=(
                "EduVision AI v1.0\n"
                "Artificial Intelligence in Student Management Systems\n"
                "to Enhance Academic Performance Monitoring and Intervention"
            ),
            justify="center",
            font=("Segoe UI", 13),
            text_color="#64748B"
        )

        footer.pack(
            pady=(20, 15)
        )