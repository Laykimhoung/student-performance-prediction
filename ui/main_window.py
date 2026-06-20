import customtkinter as ctk

from ui.dashboard_page import DashboardPage
from ui.role_selection_page import RoleSelectionPage
from ui.about_ai_page import AboutAIPage
from ui.about_project_page import AboutProjectPage

from ui.admin.login_page import AdminLoginPage
from ui.admin.dashboard import AdminDashboard

from ui.teacher.login_page import TeacherLoginPage
from ui.teacher.dashboard import TeacherDashboard

from ui.student.preview_page import StudentPreviewPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("EduVision AI")

        self.sidebar_buttons = {}
        self.active_button = None

        self.after(100, lambda: self.state("zoomed"))
        self.minsize(1300, 800)

        self.configure(fg_color="#0B1120")

        self.dashboard_container = None

        self.build_ui()

    # ==========================================
    # BUILD UI
    # ==========================================
    def build_ui(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # SIDEBAR
        # ==========================================
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
            ("About AI", self.show_about_ai),
            ("About Project", self.show_about_project),
        ]

        for text, command in sidebar_buttons:

            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=54,
                corner_radius=18,
                fg_color="#1E293B",
                hover_color="#2563EB",
                font=("Segoe UI", 18),
                anchor="w",
                command=lambda c=command, t=text: self.select_sidebar(t, c)
            )

            btn.pack(
                fill="x",
                padx=24,
                pady=8
            )

            self.sidebar_buttons[text] = btn

        
        # ==========================================
        # CONTENT AREA
        # ==========================================
        self.content = ctk.CTkFrame(
            self,
            fg_color="#0F172A"
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.after(
            100,
            lambda: self.select_sidebar(
                "Dashboard",
                self.show_dashboard
            )
        )

    # ==========================================
    # ROUTER
    # ==========================================
    def clear_page(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def show_page(self, page_class):

        self.clear_page()

        page = page_class(self.content)
        page.pack(
            fill="both",
            expand=True
        )

    # ==========================================
    # SELECT SIDEBAR
    # ==========================================
    def select_sidebar(
        self,
        button_name,
        callback
    ):

        for btn in self.sidebar_buttons.values():

            btn.configure(
                fg_color="#1E293B"
            )

        self.sidebar_buttons[
            button_name
        ].configure(
            fg_color="#2563EB"
        )

        self.active_button = button_name

        callback()
    # ==========================================
    # RESTORE GLOBAL LAYOUT
    # ==========================================
    def restore_main_layout(self):

        # Remove dashboard shell
        if self.dashboard_container:
            self.dashboard_container.destroy()
            self.dashboard_container = None

        # Restore sidebar
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # Restore content
        self.content.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # ==========================================
    # DEFAULT PAGES
    # ==========================================
    def show_dashboard(self):

        self.restore_main_layout()
        self.show_page(DashboardPage)

    def show_role_selection(self):

        self.restore_main_layout()

        self.clear_page()

        RoleSelectionPage(
            self.content,
            self
        ).pack(fill="both", expand=True)

    def show_about_ai(self):

        self.restore_main_layout()
        self.show_page(AboutAIPage)


    def show_about_project(self):

        self.restore_main_layout()
        self.show_page(AboutProjectPage)


    # ==========================================
    # LOGIN ROUTES
    # ==========================================
    def show_admin_login(self):

        self.restore_main_layout()
        self.show_page(AdminLoginPage)

    def show_teacher_login(self):

        self.restore_main_layout()
        self.show_page(TeacherLoginPage)

    def show_student_preview(self):

        self.restore_main_layout()
        self.show_page(StudentPreviewPage)

    # ==========================================
    # DASHBOARD ROUTES
    # ==========================================
    def show_admin_dashboard(self):

        # Hide old layout
        self.sidebar.grid_forget()
        self.content.grid_forget()

        # Remove old dashboard
        if self.dashboard_container:
            self.dashboard_container.destroy()

        # Show admin dashboard
        self.dashboard_container = AdminDashboard(self)

        self.dashboard_container.pack(
            fill="both",
            expand=True
        )

    def show_teacher_dashboard(self):

        self.sidebar.grid_forget()
        self.content.grid_forget()

        if self.dashboard_container:
            self.dashboard_container.destroy()

        self.dashboard_container = TeacherDashboard(self)

        self.dashboard_container.pack(
            fill="both",
            expand=True
        )
