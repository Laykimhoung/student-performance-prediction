import customtkinter as ctk

from ui.dashboard_page import DashboardPage
from ui.role_selection_page import RoleSelectionPage
from ui.analytics_page import AnalyticsPage
from ui.reports_page import ReportsPage
from ui.settings_page import SettingsPage

from ui.admin.login_page import AdminLoginPage
from ui.admin.dashboard import AdminDashboard
from ui.teacher.login_page import TeacherLoginPage
from ui.student.preview_page import StudentPreviewPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("EduVision AI")

        self.after(100, lambda: self.state("zoomed"))
        self.minsize(1300, 800)

        self.configure(fg_color="#0B1120")

        self.build_ui()

    def build_ui(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================
        # SIDEBAR
        # ==========================
        self.sidebar = ctk.CTkFrame(
            self,
            width=280,
            fg_color="#111827",
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.sidebar.grid_propagate(False)

        # Logo
        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="EduVision AI",
            font=("Segoe UI", 34, "bold")
        )
        self.logo.pack(pady=(45, 8))

        self.logo_sub = ctk.CTkLabel(
            self.sidebar,
            text="AI Student Management",
            font=("Segoe UI", 14),
            text_color="#94A3B8"
        )
        self.logo_sub.pack()

        divider = ctk.CTkFrame(
            self.sidebar,
            height=2,
            fg_color="#1E293B"
        )
        divider.pack(
            fill="x",
            padx=28,
            pady=35
        )

        sidebar_buttons = [
            ("Dashboard", self.show_dashboard),
            ("Role Selection", self.show_role_selection),
            ("Analytics", self.show_analytics),
            ("Reports", self.show_reports),
            ("Settings", self.show_settings)
        ]

        for text, command in sidebar_buttons:

            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
                height=54,
                corner_radius=18,
                fg_color="#1E293B",
                hover_color="#2563EB",
                font=("Segoe UI", 18),
                anchor="w"
            )

            btn.pack(
                fill="x",
                padx=24,
                pady=8
            )

        self.theme_switch = ctk.CTkSwitch(
            self.sidebar,
            text="Light Mode",
            command=self.toggle_theme
        )

        self.theme_switch.pack(
            side="bottom",
            pady=30
        )

        # ==========================
        # CONTENT
        # ==========================
        self.content = ctk.CTkFrame(
            self,
            fg_color="#0F172A"
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.show_dashboard()

    # ==========================
    # ROUTER
    # ==========================
    def clear_page(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_page()
        DashboardPage(self.content).pack(fill="both", expand=True)

    def show_role_selection(self):
        self.clear_page()
        RoleSelectionPage(
            self.content,
            self
        ).pack(fill="both", expand=True)

    def show_analytics(self):
        self.clear_page()
        AnalyticsPage(self.content).pack(fill="both", expand=True)

    def show_reports(self):
        self.clear_page()
        ReportsPage(self.content).pack(fill="both", expand=True)

    def show_settings(self):
        self.clear_page()
        SettingsPage(self.content).pack(fill="both", expand=True)

    # ==========================
    # ROLE ROUTING
    # ==========================
    def show_admin_dashboard(self):
        self.clear_page()

        AdminLoginPage(self.content).pack(
            fill="both",
            expand=True
        )

    def show_teacher_login(self):
        self.clear_page()
        TeacherLoginPage(self.content).pack(
            fill="both",
            expand=True
        )


    def show_student_preview(self):
        self.clear_page()
        StudentPreviewPage(self.content).pack(
            fill="both",
            expand=True
        )

    # ==========================
    # THEME TOGGLE
    # ==========================
    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")