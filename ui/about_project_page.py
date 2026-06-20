import customtkinter as ctk


class AboutProjectPage(ctk.CTkFrame):

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
            text="About Project",
            font=("Segoe UI", 42, "bold")
        )

        title.pack(
            anchor="w",
            padx=40,
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="EduVision AI - Student Performance Prediction and Management System",
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
        # PROJECT OVERVIEW
        # ==================================
        ctk.CTkLabel(
            content,
            text="Project Overview",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "EduVision AI is an AI-Enhanced Student Performance "
                "Prediction and Management System designed to assist "
                "educational institutions in monitoring academic "
                "performance, identifying at-risk students, and "
                "supporting intervention strategies."
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
        # RESEARCH OBJECTIVE
        # ==================================
        ctk.CTkLabel(
            content,
            text="Research Objective",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "Artificial Intelligence in Student Management Systems "
                "to Enhance Academic Performance Monitoring and Intervention."
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
        # TECHNOLOGY STACK
        # ==================================
        ctk.CTkLabel(
            content,
            text="Technology Stack",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 15)
        )

        tech_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        tech_frame.pack(
            fill="x",
            padx=30
        )

        technologies = [
            ("Python", "#E0CB06"),
            ("CustomTkinter", "#3B82F6"),
            ("SQLite", "#10B981"),
            ("Scikit-Learn", "#F59E0B"),
            ("Pandas", "#8B5CF6"),
            ("NumPy", "#06B6D4"),
            ("Matplotlib", "#EF4444"),
            ("ReportLab", "#EC4899"),
            ("OpenPyXL", "#22C55E")
        ]

        for i, (tech, color) in enumerate(technologies):

            card = ctk.CTkFrame(
                tech_frame,
                fg_color="#111827",
                corner_radius=15,
                width=170,
                height=70
            )

            card.grid(
                row=0,
                column=i,
                padx=10,
                pady=10
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=tech,
                font=("Segoe UI", 16, "bold"),
                text_color=color
            ).pack(
                expand=True
            )

        # ==================================
        # USER ROLES
        # ==================================
        ctk.CTkLabel(
            content,
            text="System Roles",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 15)
        )

        roles_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        roles_frame.pack(
            fill="x",
            padx=30
        )

        roles = [
            "Admin",
            "Teacher",
            "Student"
        ]

        for i, role in enumerate(roles):

            card = ctk.CTkFrame(
                roles_frame,
                fg_color="#111827",
                corner_radius=15,
                width=220,
                height=80
            )

            card.grid(
                row=0,
                column=i,
                padx=10,
                pady=10
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=role,
                font=("Segoe UI", 18, "bold"),
                text_color="#3B82F6"
            ).pack(
                expand=True
            )

        # ==================================
        # MODULES
        # ==================================
        ctk.CTkLabel(
            content,
            text="Main Modules",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 15)
        )

        modules = [
            "Student Management",
            "Teacher Management",
            "Classroom Management",
            "Assessment Management",
            "AI Prediction",
            "Recommendation System"
        ]

        for module in modules:

            ctk.CTkLabel(
                content,
                text=f"• {module}",
                font=("Segoe UI", 17),
                text_color="#CBD5E1"
            ).pack(
                anchor="w",
                padx=50,
                pady=3
            )

        # ==================================
        # VERSION
        # ==================================
        ctk.CTkLabel(
            content,
            text="Information",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )

        ctk.CTkLabel(
            content,
            text=(
                "Version : 1.0\n"
                "Developer : Lay Kimhoung\n"
                "Major : Computer Science\n"
                "Platform : Desktop Application"
            ),
            font=("Segoe UI", 17),
            text_color="#CBD5E1",
            justify="left"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 25)
        )