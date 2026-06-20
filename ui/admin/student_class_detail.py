import customtkinter as ctk

from database.crud import (
    get_students_by_class,
    get_class_teacher
)

class StudentClassDetailPage(ctk.CTkFrame):

    def __init__(
            self,
            parent,
            class_data
        ):

        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.class_data = class_data

        self.students = get_students_by_class(
            self.class_data["id"]
        )

        self.all_students = self.students.copy()

        self.build_ui()
    
    def get_gender_stats(self):

        male = sum(
            1 for s in self.students
            if s[3] == "Male"
        )

        female = sum(
            1 for s in self.students
            if s[3] == "Female"
        )

        return male, female

    def open_add_student(self):

        from ui.admin.add_student_dialog import AddStudentDialog

        AddStudentDialog(
            self,
            class_id=self.class_data["id"],
            refresh_callback=self.refresh_students
        )

    def open_edit_student(self, student):

        from ui.admin.add_student_dialog import AddStudentDialog

        AddStudentDialog(
            self,
            class_id=self.class_data["id"],
            refresh_callback=self.refresh_students,
            student=student
        )

    def open_delete_student(
            self,
            student_id,
            student_name
        ):

        from ui.admin.delete_student_dialog import DeleteStudentDialog

        DeleteStudentDialog(
            self,
            student_id,
            student_name,
            self.refresh_students
        )

    def refresh_students(self):

        self.students = get_students_by_class(
            self.class_data["id"]
        )

        self.all_students = self.students.copy()

        for widget in self.winfo_children():
            widget.destroy()

        self.build_ui()
    
    def search_students(self, event=None):

        keyword = self.search_entry.get().strip().lower()

        self.students = self.all_students.copy()

        if keyword:

            self.students = [
                student
                for student in self.students
                if (
                    keyword in student[1].lower()
                    or keyword in student[2].lower()
                )
            ]

        for widget in self.winfo_children():
            widget.destroy()

        self.build_ui()

    def go_back(self):

        from ui.admin.student_management import StudentManagementPage

        parent = self.master

        for widget in parent.winfo_children():
            widget.destroy()

        StudentManagementPage(parent).pack(
            fill="both",
            expand=True
        )

    def build_ui(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(20, 15)
        )

        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(
            fill="x"
        )

        ctk.CTkLabel(
            title_frame,
            text=f"{self.class_data['name']} Students",
            font=("Segoe UI", 34, "bold")
        ).pack(
            side="left"
        )

        ctk.CTkButton(
            title_frame,
            text="← Back",
            width=150,
            height=45,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.go_back
        ).pack(
            side="right"
        )

        content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

        content.grid_columnconfigure(
            0,
            weight=11
        )

        content.grid_columnconfigure(
            1,
            weight=2
        )

        content.grid_rowconfigure(
            0,
            weight=1
        )

        left_frame = ctk.CTkFrame(
            content,
            fg_color="transparent"
        )

        left_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        toolbar = ctk.CTkFrame(
            left_frame,
            fg_color="transparent"
        )

        toolbar.pack(
            fill="x",
            pady=(0, 15)
        )

        self.search_entry = ctk.CTkEntry(
            toolbar,
            placeholder_text="Search Code or Name..."
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        ctk.CTkButton(
            toolbar,
            text="Search",
            width=100,
            height=40,
            command=self.search_students
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.search_entry.bind(
            "<Return>",
            self.search_students
        )

        ctk.CTkButton(
                toolbar,
                text="+ Add Student",
                width=140,
                height=40,
                command=self.open_add_student
            ).pack(
                side="right"
            )

        table = ctk.CTkScrollableFrame(
            left_frame,
            fg_color="#0F172A",
            corner_radius=20,
            height=650
        )

        for col in range(5):
            table.grid_columnconfigure(
                col,
                weight=1
            )
    
        table.pack(
            fill="both",
            expand=True,
        )

        summary = ctk.CTkFrame(
            content,
            fg_color="#0F172A",
            corner_radius=20
        )

        summary.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        ctk.CTkLabel(
            summary,
            text="Class Summary",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 20)
        )

        ctk.CTkLabel(
            summary,
            text=f"Class : {self.class_data['name']}",
            font=("Segoe UI", 16)
        ).pack(
            anchor="w",
            padx=20,
            pady=8
        )
    

        male, female = self.get_gender_stats()

        teacher = get_class_teacher(
            self.class_data["id"]
        )

        teacher_card = ctk.CTkFrame(
            summary,
            fg_color="#111827",
            corner_radius=15
        )

        teacher_card.pack(
            fill="x",
            padx=15,
            pady=(10, 15)
        )

        ctk.CTkLabel(
            teacher_card,
            text="Assigned Teacher",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 0)
        )

        ctk.CTkLabel(
            teacher_card,
            text=teacher[0] if teacher else "Not Assigned",
            font=("Segoe UI", 20, "bold"),
            text_color="#3B82F6"
        ).pack(
            anchor="w",
            padx=15
        )

        ctk.CTkLabel(
            teacher_card,
            text=teacher[1] if teacher else "-",
            font=("Segoe UI", 12),
            text_color="#94A3B8"
        ).pack(
            anchor="w",
            padx=15,
            pady=(0, 10)
        )

        stats = [
            ("Students", len(self.students), "#3B82F6"),
            ("Male", male, "#5FA3DE"),
            ("Female", female, "#ED4AB4"),
            (
                "Female %",
                f"{(female / len(self.students) * 100):.1f}%"
                if len(self.students) > 0
                else "0%",
                "#22C55E"
            )
        ]

        for title, value, color in stats:

            card = ctk.CTkFrame(
                summary,
                fg_color="#111827",
                corner_radius=15
            )

            card.pack(
                fill="x",
                padx=15,
                pady=8
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14)
            ).pack(
                anchor="w",
                padx=15,
                pady=(10, 0)
            )

            ctk.CTkLabel(
                card,
                text=str(value),
                font=("Segoe UI", 24, "bold"),
                text_color=color
            ).pack(
                anchor="w",
                padx=15,
                pady=(0, 10)
            )

        headers = [
            "ID",
            "Code",
            "Name",
            "Gender",
            "Actions"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                table,
                text=header,
                font=("Segoe UI", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=15,
                sticky="ew"
            )

        for row_index, student in enumerate(
            self.students,
            start=1
        ):

            values = [
                student[0],
                student[1],
                student[2],
                student[3]
            ]

            for col_index, value in enumerate(values):

                ctk.CTkLabel(
                    table,
                    text=str(value),
                    font=("Segoe UI", 13)
                ).grid(
                    row=row_index,
                    column=col_index,
                    padx=15,
                    pady=10,
                    sticky="ew"
                )

            action_frame = ctk.CTkFrame(
                table,
                fg_color="transparent"
            )

            action_frame.grid(
                row=row_index,
                column=4,
                padx=10,
                pady=8
            )

            ctk.CTkButton(
                action_frame,
                text="Edit",
                width=60,
                fg_color="#F59E0B",
                command=lambda s=student:
                self.open_edit_student(s)
            ).pack(
                side="left",
                padx=(0, 5)
            )

            ctk.CTkButton(
                action_frame,
                text="Delete",
                width=60,
                fg_color="#EF4444",
                command=lambda s=student:
                self.open_delete_student(
                    s[0],
                    s[2]
                )
            ).pack(
                side="left"
            )
