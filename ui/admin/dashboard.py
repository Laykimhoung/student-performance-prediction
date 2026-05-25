from ui.components.dashboard_shell import DashboardShell
import customtkinter as ctk


class AdminDashboard(DashboardShell):

    def __init__(self, parent):

        super().__init__(
            parent,
            role_name="Admin",
            accent_color="#3B82F6",
            menu_items=[
                "Dashboard",
                "Students",
                "Teachers",
                "Analytics",
                "Reports",
                "Settings"
            ]
        )

        self.build_dashboard()

    def build_dashboard(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self.content,
            text="Admin Dashboard",
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
            text="Manage teachers, classes and analytics",
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
            ("1,540", "Students"),
            ("38", "Teachers"),
            ("16", "Classes"),
            ("92%", "Attendance")
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
                text_color="#3B82F6"
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
            "Add Student",
            "Manage Teachers",
            "Generate Report",
            "Open Analytics"
        ]

        for action in actions:

            btn = ctk.CTkButton(
                quick_actions,
                text=action,
                height=52,
                corner_radius=18,
                fg_color="#3B82F6",
                hover_color="#2563EB",
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
            "• Teacher added Class A",
            "• Student report generated",
            "• Prediction model updated",
            "• Analytics exported"
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