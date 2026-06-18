from ui.teacher.student_detail_page import StudentDetailPage
from ui.teacher.students_page import StudentsPage
from ui.teacher.grade_entry_page import GradeEntryPage
from ui.teacher.analytics_page import AnalyticsPage
from reports.pdf_generator import export_class_pdf
from reports.excel_generator import export_class_excel
import customtkinter as ctk

from database.crud import (
    get_students_by_class,
    get_student_detail
)


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

        students = []

        class_id = self.class_data["id"]

        rows = get_students_by_class(class_id)

        for row in rows:

            student_id = row[0]

            detail = get_student_detail(student_id)

            students.append(
                {
                    "id": detail[0],
                    "code": detail[1],
                    "name": detail[2],
                    "gender": detail[3],

                    "quiz": detail[5] or 0,
                    "homework": detail[6] or 0,
                    "attendance": detail[7] or 0,
                    "assignment": detail[8] or 0,
                    "midterm": detail[9] or 0,
                    "final": detail[10] or 0,
                    "participation": detail[11] or 0,
                    "project": detail[12] or 0,
                    "behavior": detail[13] or 0,

                    "average": detail[14] or 0,
                    "predicted_score": detail[15] or 0,
                    "risk": detail[16] or "Low",
                    "recommendation": detail[17] or ""
                }
            )
        return students
    
    # ==================================
    # OPEN STUDENT DETAIL
    # ==================================
    def open_student_detail(self, student):

        parent = self.master

        self.destroy()

        StudentDetailPage(
            parent,
            student_id=student["id"],
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
    # OPEN STUDENTS
    # ==================================
    def open_students(self):

        parent = self.master

        self.destroy()

        StudentsPage(
            parent,
            class_id=self.class_data["id"],
            class_name=self.class_data["name"],
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # EXPORT EXCEL
    # ==================================
    def export_excel(self):

        class_export_data = {
            "name": self.class_data["name"],
            "students": self.class_data["students"],
            "average": self.class_data["average"],
            "attendance": 0
        }

        export_class_excel(
            class_export_data,
            self.students
        )
    
    # ==================================
    # EXPORT PDF
    # ==================================
    def export_pdf(self):

        export_class_pdf(
            self.class_data,
            self.students
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
            command=self.back_command if self.back_command else lambda: None
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
            (f'{class_info["average"]}%', "Average", "#10B981"),
            (str(class_info["risk"]), "High Risk", "#EF4444")
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

        body.grid_columnconfigure(0, weight=4)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

                # STUDENT PERFORMANCE TABLE
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
            text="Student Performance",
            font=("Segoe UI", 28, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 20)
        )

        # TABLE HEADER
        header = ctk.CTkFrame(
            table_frame,
            fg_color="#111827",
            corner_radius=18
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        columns = [
            ("Student", 120),
            ("Attend", 70),
            ("Quiz", 60),
            ("HW", 60),
            ("Assign", 70),
            ("Mid", 60),
            ("Final", 60),
            ("Part", 60),
            ("Project", 70),
            ("Behavior", 80),
            ("Avg", 60),
            ("Risk", 80),
            ("Act", 70)
        ]

        for col, width in columns:

            ctk.CTkLabel(
                header,
                text=col,
                width=width,
                font=("Segoe UI", 13, "bold")
            ).pack(
                side="left",
                padx=2,
                pady=16
            )

        scroll_table = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )

        scroll_table.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 20)
        )

        for student in self.students:

            average = student["average"]

            row = ctk.CTkFrame(
                scroll_table,
                fg_color="#111827",
                corner_radius=18
            )

            row.pack(
                fill="x",
                pady=8,
                padx=5
            )

            values = [
                (student["name"], 120),
                (f'{student["attendance"]}%', 70),
                (student["quiz"], 60),
                (student["homework"], 60),
                (student["assignment"], 70),
                (student["midterm"], 60),
                (student["final"], 60),
                (student["participation"], 60),
                (student["project"], 70),
                (student["behavior"], 80),
                (average, 60)
            ]

            for value, width in values:

                ctk.CTkLabel(
                    row,
                    text=str(value),
                    width=width,
                    font=("Segoe UI", 12)
                ).pack(
                    side="left",
                    padx=2,
                    pady=16
                )

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
                width=80,
                font=("Segoe UI", 12, "bold"),
                text_color=risk_color
            ).pack(
                side="left",
                padx=2,
                pady=16
            )

            ctk.CTkButton(
                row,
                text="View",
                width=80,
                height=34,
                corner_radius=12,
                fg_color="#EF4444",
                hover_color="#DC2626",
                command=lambda s=student:
                self.open_student_detail(s)
            ).pack(
                side="left",
                padx=5,
                pady=8
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
            text="Quick Act",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(28, 20)
        )

        actions = [
            ("Students", self.open_students),
            ("Assessment", self.open_grade_entry),
            ("Analytics", self.open_analytics),
            ("Export Excel", self.export_excel),
            ("Export PDF", self.export_pdf)
        ]

        for text, command in actions:

            btn = ctk.CTkButton(
                actions_frame,
                text=text,
                height=52,
                corner_radius=18,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold"),
                command=command
            )

            btn.pack(
                fill="x",
                padx=25,
                pady=8
            )