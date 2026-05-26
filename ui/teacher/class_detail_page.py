from ui.teacher.student_detail_page import StudentDetailPage
from ui.teacher.grade_entry_page import GradeEntryPage
from ui.teacher.attendance_page import AttendancePage
from ui.teacher.analytics_page import AnalyticsPage
import customtkinter as ctk


class ClassDetailPage(ctk.CTkFrame):

    def __init__(
            self,
            parent,
            class_data,
            back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.class_data = class_data
        self.back_command = back_command

        self.students = self.load_students()

        self.build_ui()

    # ==================================
    # STUDENT DATA
    # ==================================
    def load_students(self):

        return [
            {
                "id": "001",
                "name": "Dara",
                "class": self.class_data["name"],
                "semester": 1,
                "attendance": 92,
                "quiz": 84,
                "homework": 81,
                "assignment": 78,
                "midterm": 75,
                "final": 89,
                "participation": 85,
                "project": 90,
                "behavior": 88,
                "risk": "Low",
                "risk_factors": [
                    "✓ Strong attendance consistency",
                    "✓ High final performance",
                    "✓ Homework submission stable"
                ],
                "recommendation":
                    "Continue monitoring progress.\n"
                    "Maintain attendance and\n"
                    "encourage participation."
            },

            {
                "id": "002",
                "name": "Sokha",
                "class": self.class_data["name"],
                "semester": 1,
                "attendance": 58,
                "quiz": 54,
                "homework": 62,
                "assignment": 58,
                "midterm": 60,
                "final": 57,
                "participation": 45,
                "project": 59,
                "behavior": 68,
                "risk": "High",
                "risk_factors": [
                    "⚠ Low attendance",
                    "⚠ Weak quiz performance",
                    "⚠ Poor participation",
                    "⚠ Final score declining"
                ],
                "recommendation":
                    "Schedule intervention.\n"
                    "Increase monitoring and\n"
                    "provide academic support."
            },

            {
                "id": "003",
                "name": "Lina",
                "class": self.class_data["name"],
                "semester": 1,
                "attendance": 81,
                "quiz": 72,
                "homework": 74,
                "assignment": 71,
                "midterm": 79,
                "final": 80,
                "participation": 83,
                "project": 82,
                "behavior": 84,
                "risk": "Medium",
                "risk_factors": [
                    "⚠ Quiz slightly declining",
                    "✓ Stable attendance",
                    "✓ Good participation"
                ],
                "recommendation":
                    "Monitor quiz trend.\n"
                    "Provide light academic support."
            }
        ]

    # ==================================
    # OPEN STUDENT DETAIL
    # ==================================
    def open_student_detail(self, student):

        parent = self.master

        self.destroy()

        StudentDetailPage(
            parent,
            student_data=student,
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # OPEN GRADE ENTRY
    # ==================================
    def open_grade_entry(self):

        parent = self.master

        self.destroy()

        GradeEntryPage(
            parent,
            class_data=self.class_data,
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # OPEN ATTENDANCE
    # ==================================
    def open_attendance(self):

        parent = self.master

        self.destroy()

        AttendancePage(
            parent,
            class_data=self.class_data,
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # OPEN ANALYTICS
    # ==================================
    def open_analytics(self):

        parent = self.master

        self.destroy()

        AnalyticsPage(
            parent,
            class_data=self.class_data,
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # BACK TO CLASS DETAIL
    # ==================================
    def go_back(self):

        parent = self.master

        for widget in parent.winfo_children():
            widget.destroy()

        ClassDetailPage(
            parent,
            class_data=self.class_data,
            back_command=self.back_command
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        class_info = self.class_data

        # HEADER
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=(25, 10)
        )

        title_frame = ctk.CTkFrame(
            top_bar,
            fg_color="transparent"
        )

        title_frame.pack(side="left")

        title = ctk.CTkLabel(
            title_frame,
            text=class_info["name"],
            font=("Segoe UI", 40, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Class management and performance monitoring",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(anchor="w")

        back_btn = ctk.CTkButton(
            top_bar,
            text="← Back",
            width=140,
            height=46,
            corner_radius=16,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 16, "bold"),
            command=self.back_command
        )

        back_btn.pack(side="right")

        # STATS
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=30,
            pady=(10, 25)
        )

        stats = [
            (str(class_info["students"]), "Students", "#3B82F6"),
            (f'{class_info["attendance"]}%', "Attendance", "#10B981"),
            (f'{class_info["average"]}%', "Average", "#F59E0B"),
            (str(class_info["risk"]), "At Risk", "#EF4444")
        ]

        for value, label, color in stats:

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                height=145,
                corner_radius=28
            )

            card.pack(
                side="left",
                fill="both",
                expand=True,
                padx=10
            )

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 34, "bold"),
                text_color=color
            ).pack(pady=(28, 5))

            ctk.CTkLabel(
                card,
                text=label,
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            ).pack()

        # BODY
        body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        body.grid_columnconfigure(0, weight=2)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        # STUDENTS
        table_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        table_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        ctk.CTkLabel(
            table_frame,
            text="Students",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(28, 20)
        )

        scroll = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        for student in self.students:

            row = ctk.CTkFrame(
                scroll,
                fg_color="#111827",
                corner_radius=18,
                height=80
            )

            row.pack(
                fill="x",
                pady=8
            )

            row.pack_propagate(False)

            info = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            info.pack(side="left", padx=20)

            ctk.CTkLabel(
                info,
                text=f'{student["name"]} ({student["id"]})',
                font=("Segoe UI", 17, "bold")
            ).pack(anchor="w")

            ctk.CTkLabel(
                info,
                text=f'Average: {student["final"]}',
                font=("Segoe UI", 14),
                text_color="#94A3B8"
            ).pack(anchor="w")

            risk_color = (
                "#EF4444"
                if student["risk"] == "High"
                else "#F59E0B"
                if student["risk"] == "Medium"
                else "#10B981"
            )

            ctk.CTkLabel(
                row,
                text=student["risk"],
                font=("Segoe UI", 16, "bold"),
                text_color=risk_color
            ).pack(
                side="left",
                padx=30
            )

            ctk.CTkButton(
                row,
                text="View",
                width=100,
                height=40,
                corner_radius=14,
                fg_color="#EF4444",
                hover_color="#DC2626",
                command=lambda s=student:
                self.open_student_detail(s)
            ).pack(
                side="right",
                padx=20
            )

        # QUICK ACTIONS
        actions_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        actions_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        ctk.CTkLabel(
            actions_frame,
            text="Quick Actions",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(28, 20)
        )

        actions = [
            ("Take Attendance", self.open_attendance),
            ("Grade Entry", self.open_grade_entry),
            ("Risk Analytics", self.open_analytics),
            ("Export Report", None)
        ]

        for text, command in actions:

            ctk.CTkButton(
                actions_frame,
                text=text,
                height=52,
                corner_radius=18,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold"),
                command=command
            ).pack(
                fill="x",
                padx=25,
                pady=8
            )