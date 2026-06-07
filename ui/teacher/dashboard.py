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
                "Classrooms",
                "Students",
                "Analytics"
            ]
        )

        self.navigate("Dashboard")

    # ==================================
    # NAVIGATION
    # ==================================
    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def navigate(self, page_name):

        self.clear_content()

        if page_name == "Dashboard":
            self.build_dashboard()

        elif page_name == "Classrooms":
            from ui.teacher.classroom_page import ClassroomPage

            ClassroomPage(
                self.content
            ).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Students":
            from ui.teacher.students_page import StudentsPage

            StudentsPage(
                self.content
            ).pack(
                fill="both",
                expand=True
            )

        elif page_name == "Analytics":
            from ui.teacher.analytics_page import AnalyticsPage

            AnalyticsPage(
                self.content
            ).pack(
                fill="both",
                expand=True
            )

    # ==================================
    # DASHBOARD UI
    # ==================================
    def build_dashboard(self):

        # ===============================
        # HEADER
        # ===============================
        title = ctk.CTkLabel(
            self.content,
            text="Teacher Dashboard",
            font=("Segoe UI", 40, "bold")
        )
        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self.content,
            text="Monitor classes, student performance and risk prediction",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )
        subtitle.pack(
            anchor="w",
            padx=35
        )

        # ===============================
        # STATS CARDS
        # ===============================
        stats_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=30
        )

        stats = [
            ("8", "Classes", "#3B82F6"),
            ("240", "Students", "#10B981"),
            ("92%", "Attendance", "#F59E0B"),
            ("12", "High Risk", "#EF4444")
        ]

        for value, label, color in stats:

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                corner_radius=28,
                height=150
            )

            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=10
            )

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            ).pack(
                pady=(30, 5)
            )

            ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 17),
                text_color="#94A3B8"
            ).pack()

        # ===============================
        # MAIN AREA
        # ===============================
        body = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        body.grid_columnconfigure(
            0,
            weight=2
        )

        body.grid_columnconfigure(
            1,
            weight=1
        )

        body.grid_rowconfigure(
            0,
            weight=1
        )

        # ===============================
        # RECENT ALERTS
        # ===============================
        alerts_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        alerts_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        ctk.CTkLabel(
            alerts_frame,
            text="Recent Alerts",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        alerts = [
            "⚠ Sokha attendance dropped below 60%",
            "⚠ Kimlong marked High Risk",
            "✓ Grade 12A attendance improved",
            "✓ Midterm scores uploaded",
            "✓ Assignment report exported"
        ]

        for item in alerts:

            ctk.CTkLabel(
                alerts_frame,
                text=item,
                font=("Segoe UI", 17),
                text_color="#CBD5E1"
            ).pack(
                anchor="w",
                padx=25,
                pady=8
            )

        # ===============================
        # ACADEMIC INSIGHTS
        # ===============================
        insight_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        insight_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        ctk.CTkLabel(
            insight_frame,
            text="Academic Insights",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        insights = [
            ("Top Class", "Grade 12A", "#10B981"),
            ("Lowest Class", "Grade 11B", "#EF4444"),
            ("High Risk Students", "12 Students", "#F59E0B"),
            ("Attendance Trend", "Improving ↑", "#3B82F6")
        ]

        for title, value, color in insights:

            card = ctk.CTkFrame(
                insight_frame,
                fg_color="#111827",
                corner_radius=20
            )

            card.pack(
                fill="x",
                padx=20,
                pady=10
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14),
                text_color="#94A3B8"
            ).pack(
                anchor="w",
                padx=18,
                pady=(15, 2)
            )

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 22, "bold"),
                text_color=color
            ).pack(
                anchor="w",
                padx=18,
                pady=(0, 15)
            )