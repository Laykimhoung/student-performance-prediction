import customtkinter as ctk


class AdminDashboard(ctk.CTkFrame):

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
        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        header.pack(
            fill="x",
            padx=40,
            pady=(40, 20)
        )

        title = ctk.CTkLabel(
            header,
            text="Admin Dashboard",
            font=("Segoe UI", 42, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Manage teachers, classes and analytics",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )
        subtitle.pack(anchor="w")

        # ==================================
        # STATS CARDS
        # ==================================
        stats_container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        stats_container.pack(
            fill="x",
            padx=40,
            pady=(0, 30)
        )

        stats_container.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        stats = [
            ("1,540", "Students", "#3B82F6"),
            ("38", "Teachers", "#EF4444"),
            ("16", "Classes", "#8B5CF6"),
            ("92%", "Attendance", "#10B981")
        ]

        for i, (number, label, color) in enumerate(stats):

            card = ctk.CTkFrame(
                stats_container,
                corner_radius=30,
                fg_color="#0F172A",
                border_width=1,
                border_color="#1E293B",
                height=180
            )

            card.grid(
                row=0,
                column=i,
                padx=12,
                sticky="nsew"
            )

            accent = ctk.CTkFrame(
                card,
                height=6,
                fg_color=color,
                corner_radius=100
            )
            accent.pack(
                fill="x",
                padx=24,
                pady=(24, 25)
            )

            num_label = ctk.CTkLabel(
                card,
                text=number,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            )
            num_label.pack()

            text_label = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 17),
                text_color="#94A3B8"
            )
            text_label.pack(pady=(5, 20))

        # ==================================
        # LOWER GRID
        # ==================================
        lower = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        lower.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(0, 40)
        )

        lower.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        lower.grid_rowconfigure(
            0,
            weight=1
        )

        # ==================================
        # QUICK ACTIONS
        # ==================================
        quick_actions = ctk.CTkFrame(
            lower,
            fg_color="#0F172A",
            corner_radius=30,
            border_width=1,
            border_color="#1E293B"
        )

        quick_actions.grid(
            row=0,
            column=0,
            padx=(0, 12),
            sticky="nsew"
        )

        qa_title = ctk.CTkLabel(
            quick_actions,
            text="Quick Actions",
            font=("Segoe UI", 28, "bold")
        )
        qa_title.pack(
            anchor="w",
            padx=30,
            pady=(28, 25)
        )

        actions = [
            ("Add Teacher", "#EF4444"),
            ("Create Class", "#3B82F6"),
            ("Generate Report", "#8B5CF6"),
            ("View Analytics", "#10B981")
        ]

        for action, color in actions:

            btn = ctk.CTkButton(
                quick_actions,
                text=action,
                height=54,
                corner_radius=18,
                fg_color=color,
                hover_color=color,
                font=("Segoe UI", 16, "bold")
            )

            btn.pack(
                fill="x",
                padx=30,
                pady=8
            )

        # ==================================
        # RECENT ACTIVITY
        # ==================================
        activity = ctk.CTkFrame(
            lower,
            fg_color="#0F172A",
            corner_radius=30,
            border_width=1,
            border_color="#1E293B"
        )

        activity.grid(
            row=0,
            column=1,
            padx=(12, 0),
            sticky="nsew"
        )

        activity_title = ctk.CTkLabel(
            activity,
            text="Recent Activity",
            font=("Segoe UI", 28, "bold")
        )
        activity_title.pack(
            anchor="w",
            padx=30,
            pady=(28, 25)
        )

        activities = [
            "Teacher added to Class A",
            "Attendance report exported",
            "Admin created new class",
            "Prediction updated",
            "Student performance monitored"
        ]

        for item in activities:

            row = ctk.CTkFrame(
                activity,
                fg_color="#111827",
                corner_radius=16
            )

            row.pack(
                fill="x",
                padx=25,
                pady=8
            )

            label = ctk.CTkLabel(
                row,
                text=f"• {item}",
                font=("Segoe UI", 16),
                text_color="#CBD5E1"
            )

            label.pack(
                anchor="w",
                padx=18,
                pady=16
            )