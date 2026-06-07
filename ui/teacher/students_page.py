import customtkinter as ctk

from ui.teacher.student_detail_page import StudentDetailPage


class StudentsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

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
                "class": "Grade 12A",
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
                "class": "Grade 12A",
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
                "class": "Grade 12A",
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
            },

            {
                "id": "004",
                "name": "Nita",
                "class": "Grade 12A",
                "semester": 1,
                "attendance": 94,
                "quiz": 91,
                "homework": 90,
                "assignment": 92,
                "midterm": 89,
                "final": 94,
                "participation": 95,
                "project": 93,
                "behavior": 90,
                "risk": "Low",
                "risk_factors": [
                    "✓ Excellent attendance",
                    "✓ Strong academic trend",
                    "✓ High engagement"
                ],
                "recommendation":
                    "Maintain current performance."
            }
        ]

    # ==================================
    # OPEN DETAIL PAGE
    # ==================================
    def open_student_detail(self, student_data):

        parent = self.master

        self.destroy()

        detail_page = StudentDetailPage(
            parent,
            student_data=student_data,
            back_command=self.go_back
        )

        detail_page.pack(
            fill="both",
            expand=True
        )

    # ==================================
    # BACK
    # ==================================
    def go_back(self):
        if self.back_command:
            self.back_command()

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Students",
            font=("Segoe UI", 40, "bold")
        )
        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage student performance and monitor academic risk",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )
        subtitle.pack(
            anchor="w",
            padx=35
        )

        # ======================
        # TOP BAR
        # ======================
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=25
        )

        search_entry = ctk.CTkEntry(
            top_bar,
            width=430,
            height=48,
            corner_radius=14,
            placeholder_text="Search student..."
        )
        search_entry.pack(side="left")

        # CLASS DROPDOWN
        class_dropdown = ctk.CTkComboBox(
            top_bar,
            width=180,
            height=48,
            values=[
                "Grade 12A",
                "Grade 12B",
                "Grade 11A",
                "Grade 11B"
            ]
        )

        class_dropdown.set("Grade 12A")
        class_dropdown.pack(
            side="right"
        )

        # BACK BUTTON
        if self.back_command:

            back_btn = ctk.CTkButton(
                top_bar,
                text="← Back",
                width=120,
                height=48,
                corner_radius=14,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 15, "bold"),
                command=self.go_back
            )

            back_btn.pack(
                side="right",
                padx=(0, 10)
            )

        # ======================
        # BODY
        # ======================
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

        body.grid_columnconfigure(0, weight=7)
        body.grid_columnconfigure(1, weight=4)
        body.grid_rowconfigure(0, weight=1)

        # ======================
        # LEFT PANEL
        # ======================
        table_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        table_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 18)
        )

        table_title = ctk.CTkLabel(
            table_frame,
            text="Student List",
            font=("Segoe UI", 26, "bold")
        )

        table_title.pack(
            anchor="w",
            padx=30,
            pady=(28, 20)
        )

        scroll_table = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )

        scroll_table.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 25)
        )

        for student in self.students:

            avg = round(
                (
                    student["quiz"]
                    + student["homework"]
                    + student["assignment"]
                    + student["midterm"]
                    + student["final"]
                    + student["participation"]
                    + student["project"]
                    + student["behavior"]
                ) / 8
            )

            row = ctk.CTkFrame(
                scroll_table,
                fg_color="#111827",
                corner_radius=20,
                height=90
            )

            row.pack(
                fill="x",
                pady=10
            )

            row.pack_propagate(False)

            info_frame = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            info_frame.pack(
                side="left",
                padx=25
            )

            ctk.CTkLabel(
                info_frame,
                text=f'{student["name"]} ({student["id"]})',
                font=("Segoe UI", 18, "bold")
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=f"Average: {avg}",
                font=("Segoe UI", 15),
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
                font=("Segoe UI", 17, "bold"),
                text_color=risk_color
            ).pack(
                side="left",
                padx=40
            )

            ctk.CTkButton(
                row,
                text="View",
                width=110,
                height=42,
                corner_radius=14,
                fg_color="#EF4444",
                hover_color="#DC2626",
                command=lambda s=student:
                self.open_student_detail(s)
            ).pack(
                side="right",
                padx=25
            )

        # ======================
        # RIGHT PANEL
        # ======================
        preview = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        preview.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        preview_title = ctk.CTkLabel(
            preview,
            text="Student Preview",
            font=("Segoe UI", 26, "bold")
        )

        preview_title.pack(
            anchor="w",
            padx=30,
            pady=(28, 25)
        )

        preview_text = ctk.CTkLabel(
            preview,
            text="Click View to open\nstudent profile",
            justify="center",
            font=("Segoe UI", 20),
            text_color="#94A3B8"
        )

        preview_text.pack(expand=True)