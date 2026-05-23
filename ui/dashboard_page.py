import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#0F172A")

        self.build_ui()

    def build_ui(self):

        # ==========================
        # HEADER
        # ==========================
        header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        header_frame.pack(
            fill="x",
            padx=40,
            pady=(40, 20)
        )

        title = ctk.CTkLabel(
            header_frame,
            text="Dashboard",
            font=("Segoe UI", 42, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Monitor academic performance and student insights",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )
        subtitle.pack(anchor="w")

        # ==========================
        # STATS CARDS
        # ==========================
        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(
            fill="x",
            padx=40,
            pady=20
        )

        cards_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        stats = [
            ("540", "Students"),
            ("32", "High Risk"),
            ("92%", "Attendance"),
            ("18", "Classes")
        ]

        for i, (value, label) in enumerate(stats):

            card = ctk.CTkFrame(
                cards_frame,
                height=170,
                corner_radius=28,
                fg_color="#111827",
                border_width=1,
                border_color="#1E293B"
            )

            card.grid(
                row=0,
                column=i,
                padx=14,
                sticky="nsew"
            )

            number = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 38, "bold"),
                text_color="#60A5FA"
            )
            number.pack(pady=(40, 8))

            title_label = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 18),
                text_color="#CBD5E1"
            )
            title_label.pack()

        # ==========================
        # LOWER SECTION
        # ==========================
        lower_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        lower_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=(20, 40)
        )

        lower_frame.grid_columnconfigure((0, 1), weight=1)
        lower_frame.grid_rowconfigure(0, weight=1)

        # Quick Actions
        quick_actions = ctk.CTkFrame(
            lower_frame,
            corner_radius=30,
            fg_color="#111827",
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
            pady=(30, 20)
        )

        actions = [
            "Add Student",
            "Generate Report",
            "Open Analytics",
            "Manage Classes"
        ]

        for action in actions:
            btn = ctk.CTkButton(
                quick_actions,
                text=action,
                height=52,
                corner_radius=18,
                fg_color="#2563EB",
                hover_color="#1D4ED8",
                font=("Segoe UI", 16)
            )
            btn.pack(
                fill="x",
                padx=30,
                pady=8
            )

        # Recent Activity
        recent_activity = ctk.CTkFrame(
            lower_frame,
            corner_radius=30,
            fg_color="#111827",
            border_width=1,
            border_color="#1E293B"
        )

        recent_activity.grid(
            row=0,
            column=1,
            padx=(12, 0),
            sticky="nsew"
        )

        activity_title = ctk.CTkLabel(
            recent_activity,
            text="Recent Activity",
            font=("Segoe UI", 28, "bold")
        )
        activity_title.pack(
            anchor="w",
            padx=30,
            pady=(30, 20)
        )

        activities = [
            "Teacher added Class A",
            "Student report generated",
            "Prediction updated",
            "Analytics exported"
        ]

        for item in activities:
            label = ctk.CTkLabel(
                recent_activity,
                text=f"• {item}",
                font=("Segoe UI", 17),
                text_color="#CBD5E1"
            )
            label.pack(
                anchor="w",
                padx=30,
                pady=8
            )