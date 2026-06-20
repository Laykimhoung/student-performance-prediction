from ui.components.dashboard_shell import DashboardShell
from ui.admin.academic_management import AcademicManagementPage
from ui.admin.student_management import StudentManagementPage
import customtkinter as ctk
from database.crud import (
    get_total_students,
    get_total_teachers,
    get_total_classes,
    get_high_risk_count,
    get_top_class,
    get_lowest_class
)


class AdminDashboard(DashboardShell):

    def __init__(self, parent):

        super().__init__(
            parent,
            role_name="Admin",
            accent_color="#3B82F6",
            menu_items=[
                "Dashboard",
                "Academic Management",
                "Student Management",
            ]
        )

        self.build_dashboard()

    
    # ==================================
    # NAVIGATION
    # ==================================
    def navigate(self, page_name):

        # Clear current content
        for widget in self.content.winfo_children():
            widget.destroy()

        if page_name == "Dashboard":

            self.build_dashboard()

        elif page_name == "Academic Management":

            page = AcademicManagementPage(self.content)

            page.pack(
                fill="both",
                expand=True
            )
        elif page_name == "Student Management":

            page = StudentManagementPage(self.content)

            page.pack(
                fill="both",
                expand=True
            )

    # ==================================
    # DASHBOARD UI
    # ==================================
    def build_dashboard(self):

        # ==========================
        # CONTENT GRID FIX
        # ==========================
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_columnconfigure(2, weight=1)
        self.content.grid_columnconfigure(3, weight=1)

        self.content.grid_rowconfigure(3, weight=1)
        self.content.grid_rowconfigure(4, weight=1)

        # ==========================
        # HEADER
        # ==========================
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
            pady=(10, 5)
        )

        subtitle = ctk.CTkLabel(
            self.content,
            text="Manage teachers, students, classes and academic records",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="w",
            pady=(0, 30)
        )

        # ==========================
        # STAT CARDS
        # ==========================
        stats = [
            (str(get_total_students()), "Students"),
            (str(get_total_teachers()), "Teachers"),
            (str(get_total_classes()), "Classes"),
            (str(get_high_risk_count()), "High Risk")
        ]

        for i, (value, label) in enumerate(stats):

            card = ctk.CTkFrame(
                self.content,
                fg_color="#0F172A",
                corner_radius=28,
                height=160
            )

            card.grid(
                row=2,
                column=i,
                sticky="nsew",
                padx=10,
                pady=(0, 22)
            )

            card.grid_propagate(False)

            num = ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 38, "bold"),
                text_color="#3B82F6"
            )

            num.pack(
                expand=True,
                pady=(30, 0)
            )

            txt = ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 18),
                text_color="#94A3B8"
            )

            txt.pack(
                pady=(0, 28)
            )
    
        # ===============================
        # MAIN BODY
        # ===============================
        body = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        body.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="nsew",
            pady=(0, 15)
        )

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # ===============================
        # WELCOME PANEL
        # ===============================
        welcome_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        welcome_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        ctk.CTkLabel(
            welcome_frame,
            text="Welcome to EduVision AI",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        description = (
            "This Admin Panel provides complete control over\n"
            "the EduVision AI platform. Administrators can\n"
            "manage teachers, students, classes and\n"
            "support academic management."
        )

        ctk.CTkLabel(
            welcome_frame,
            text=description,
            justify="left",
            font=("Segoe UI", 16),
            text_color="#CBD5E1"
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        ctk.CTkLabel(
            welcome_frame,
            text="Administrative Capabilities:",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        features = [
            "Manage teachers and user accounts",
            "Manage students and classes",
            "Assign teachers to classrooms",
            "Monitor academic risk levels",
            "Support academic management"
        ]

        for item in features:

            ctk.CTkLabel(
                welcome_frame,
                text=f"• {item}",
                font=("Segoe UI", 16),
                text_color="#CBD5E1"
            ).pack(
                anchor="w",
                padx=40,
                pady=4
            )
        
        # ===============================
        # SYSTEM INSIGHTS
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
            text="Administrative Insights",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        top_class = get_top_class()
        lowest_class = get_lowest_class()

        insights = [
            (
                "Top Class",
                f"{top_class[0]} ({top_class[1]})" if top_class else "N/A",
                "#10B981"
            ),
            (
                "Lowest Class",
                f"{lowest_class[0]} ({lowest_class[1]})" if lowest_class else "N/A",
                "#EF4444"
            ),
            (
                "High Risk Students",
                str(get_high_risk_count()),
                "#F59E0B"
            )
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
                pady=8
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14),
                text_color="#94A3B8"
            ).pack(
                anchor="w",
                padx=15,
                pady=(12, 2)
            )

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 22, "bold"),
                text_color=color
            ).pack(
                anchor="w",
                padx=15,
                pady=(0, 12)
            )

        