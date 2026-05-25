from ui.components.dashboard_shell import DashboardShell
import customtkinter as ctk


class TeacherDashboard(DashboardShell):

    def __init__(self, parent):

        super().__init__(
            parent,
            role_name="Teacher",
            accent_color="#EF4444",
            menu_items=[
                "Dashboard",
                "Students",
                "Attendance",
                "Grades",
                "Analytics"
            ]
        )

        self.build_dashboard()

    def build_dashboard(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self.content,
            text="Teacher Dashboard",
            font=("Segoe UI", 42, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(
            self.content,
            text="Manage students and academic performance",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(0, 35)
        )

        # ==================================
        # STATS
        # ==================================
        stats = [
            ("240", "Students"),
            ("92%", "Attendance"),
            ("18", "Assignments"),
            ("12", "Classes")
        ]

        for i, (value, label) in enumerate(stats):

            card = ctk.CTkFrame(
                self.content,
                fg_color="#0F172A",
                corner_radius=28,
                height=170
            )

            card.grid(
                row=2,
                column=i,
                sticky="nsew",
                padx=12
            )

            num = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 36, "bold"),
                text_color="#EF4444"
            )

            num.pack(pady=(42, 8))

            txt = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 18),
                text_color="#94A3B8"
            )

            txt.pack()

        # ==================================
        # QUICK ACTIONS
        # ==================================
        quick_actions = ctk.CTkFrame(
            self.content,
            fg_color="#0F172A",
            corner_radius=30
        )

        quick_actions.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=12,
            pady=25
        )

        quick_title = ctk.CTkLabel(
            quick_actions,
            text="Quick Actions",
            font=("Segoe UI", 26, "bold")
        )

        quick_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        actions = [
            "Take Attendance",
            "Add Grades",
            "Manage Students",
            "Generate Report"
        ]

        for action in actions:

            btn = ctk.CTkButton(
                quick_actions,
                text=action,
                height=52,
                corner_radius=18,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold")
            )

            btn.pack(
                fill="x",
                padx=25,
                pady=8
            )

        # ==================================
        # RECENT ACTIVITY
        # ==================================
        activity = ctk.CTkFrame(
            self.content,
            fg_color="#0F172A",
            corner_radius=30
        )

        activity.grid(
            row=3,
            column=2,
            columnspan=2,
            sticky="nsew",
            padx=12,
            pady=25
        )

        activity_title = ctk.CTkLabel(
            activity,
            text="Recent Activity",
            font=("Segoe UI", 26, "bold")
        )

        activity_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        activities = [
            "• Attendance updated",
            "• Grade report generated",
            "• Student record updated",
            "• Assignment uploaded"
        ]

        for item in activities:

            label = ctk.CTkLabel(
                activity,
                text=item,
                font=("Segoe UI", 18),
                text_color="#CBD5E1"
            )

            label.pack(
                anchor="w",
                padx=25,
                pady=8
            )