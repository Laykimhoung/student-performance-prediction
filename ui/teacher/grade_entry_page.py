import customtkinter as ctk
from database.crud import (
    get_student_dropdown_by_class,
    get_student_id_by_dropdown,
    update_assessment,
    update_prediction
)

class GradeEntryPage(ctk.CTkFrame):

    def __init__(
            self,
            parent,
            class_data=None,
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
    # DATA
    # ==================================
    def load_students(self):

        students = []

        class_id = self.class_data["id"]

        rows = get_student_dropdown_by_class(class_id)

        for student in rows:

            students.append(
                f"{student[2]} ({student[1]})"
            )

        return students

    # ==================================
    # CALCULATE RESULT
    # ==================================
    def calculate_result(self):

        try:

            scores = [
                float(self.quiz.get() or 0),
                float(self.homework.get() or 0),
                float(self.assignment.get() or 0),
                float(self.midterm.get() or 0),
                float(self.final_exam.get() or 0),
                float(self.participation.get() or 0),
                float(self.project.get() or 0),
                float(self.behavior.get() or 0)
            ]

            average = round(
                sum(scores) / len(scores),
                1
            )

            if average >= 80:
                risk = "Low"
                color = "#10B981"

            elif average >= 65:
                risk = "Medium"
                color = "#F59E0B"

            else:
                risk = "High"
                color = "#EF4444"

            self.average_label.configure(
                text=f"Average: {average}"
            )

            self.risk_label.configure(
                text=f"Risk: {risk}",
                text_color=color
            )

        except ValueError:
            pass

    # ==================================
    # SAVE
    # ==================================
    def save_grade(self):

        try:

            student_text = self.student_dropdown.get()

            student_id = get_student_id_by_dropdown(
                student_text
            )

            if not student_id:
                return

            quiz = float(self.quiz.get() or 0)
            homework = float(self.homework.get() or 0)
            attendance = float(self.attendance.get() or 0)
            assignment = float(self.assignment.get() or 0)
            midterm = float(self.midterm.get() or 0)
            final = float(self.final_exam.get() or 0)
            participation = float(self.participation.get() or 0)
            project = float(self.project.get() or 0)
            behavior = float(self.behavior.get() or 0)

            average = round(
                (
                    quiz +
                    homework +
                    attendance +
                    assignment +
                    midterm +
                    final +
                    participation +
                    project +
                    behavior
                ) / 9,
                1
            )

            if average >= 80:

                risk = "Low"

                recommendation = (
                    "Maintain current performance."
                )

            elif average >= 65:

                risk = "Medium"

                recommendation = (
                    "Needs additional monitoring."
                )

            else:

                risk = "High"

                recommendation = (
                    "Immediate intervention recommended."
                )

            update_assessment(
                student_id,
                quiz,
                homework,
                attendance,
                assignment,
                midterm,
                final,
                participation,
                project,
                behavior,
                average
            )

            update_prediction(
                student_id,
                risk,
                recommendation
            )

            self.calculate_result()

            print("Assessment saved successfully")

        except ValueError:

            print("Invalid score input")

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        page = ctk.CTkScrollableFrame(
            self,
            fg_color="#071224"
        )

        page.pack(
            fill="both",
            expand=True
        )

        # HEADER
        top_bar = ctk.CTkFrame(
            page,
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
            text="Assessment",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Manage student assessment and performance",
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

        # MAIN CARD
        container = ctk.CTkFrame(
            page,
            fg_color="#0F172A",
            corner_radius=30
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(10, 35)
        )

        # STUDENT
        title = ctk.CTkLabel(
            container,
            text="Select Student",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(35, 15)
        )

        self.student_dropdown = ctk.CTkComboBox(
            container,
            values=self.students,
            width=350,
            height=48
        )

        self.student_dropdown.pack(
            anchor="w",
            padx=35
        )

        # FORM
        form_frame = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        form_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(30, 30)
        )

        form_frame.grid_columnconfigure(0, weight=1)
        form_frame.grid_columnconfigure(1, weight=1)

        self.quiz = self.create_input(
            form_frame,
            "Quiz",
            0,
            0
        )

        self.homework = self.create_input(
            form_frame,
            "Homework",
            0,
            1
        )

        self.attendance = self.create_input(
            form_frame,
            "Attendance",
            1,
            0
        )

        self.assignment = self.create_input(
            form_frame,
            "Assignment",
            1,
            1
        )

        self.midterm = self.create_input(
            form_frame,
            "Midterm",
            2,
            0
        )

        self.final_exam = self.create_input(
            form_frame,
            "Final",
            2,
            1
        )

        self.participation = self.create_input(
            form_frame,
            "Participation",
            3,
            0
        )

        self.project = self.create_input(
            form_frame,
            "Project",
            3,
            1
        )

        self.behavior = self.create_input(
            form_frame,
            "Behavior",
            4,
            0
        )

        # RESULT PREVIEW
        preview_frame = ctk.CTkFrame(
            container,
            fg_color="#111827",
            corner_radius=18
        )

        preview_frame.pack(
            fill="x",
            padx=35,
            pady=(0, 20)
        )

        self.average_label = ctk.CTkLabel(
            preview_frame,
            text="Average: --",
            font=("Segoe UI", 18, "bold")
        )

        self.average_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        self.risk_label = ctk.CTkLabel(
            preview_frame,
            text="Risk: --",
            font=("Segoe UI", 18, "bold")
        )

        self.risk_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # SAVE BUTTON
        save_btn = ctk.CTkButton(
            container,
            text="Save Assessment",
            height=56,
            corner_radius=18,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 18, "bold"),
            command=self.save_grade
        )

        save_btn.pack(
            fill="x",
            padx=35,
            pady=(10, 35)
        )

    # ==================================
    # INPUT HELPER
    # ==================================
    def create_input(
            self,
            parent,
            label_text,
            row,
            column
    ):

        frame = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        frame.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=12,
            pady=12
        )

        label = ctk.CTkLabel(
            frame,
            text=label_text,
            font=("Segoe UI", 16, "bold")
        )

        label.pack(
            anchor="w",
            pady=(0, 8)
        )

        entry = ctk.CTkEntry(
            frame,
            height=50,
            corner_radius=14,
            placeholder_text=f"Enter {label_text}"
        )

        entry.pack(fill="x")

        return entry