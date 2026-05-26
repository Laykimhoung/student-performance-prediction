import customtkinter as ctk
from datetime import datetime


class AttendancePage(ctk.CTkFrame):

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

        self.classes = [
            "Grade 12A",
            "Grade 12B",
            "Grade 11A",
            "Grade 11B"
        ]

        self.students = self.load_students()

        self.build_ui()

    # ==================================
    # MOCK STUDENTS
    # ==================================
    def load_students(self):

        return [
            "Dara (001)",
            "Sokha (002)",
            "Lina (003)",
            "Nita (004)",
            "Ratha (005)",
            "Vannak (006)"
        ]

    # ==================================
    # SAVE
    # ==================================
    def save_attendance(self):

        attendance = {}

        for student, control in self.attendance_controls.items():
            attendance[student] = control.get()

        print("Attendance Saved")
        print(attendance)

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

        # ==================================
        # HEADER
        # ==================================
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
            text="Attendance",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Track classroom attendance and monitor engagement",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(anchor="w")

        if self.back_command:

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

        # ==================================
        # MAIN CARD
        # ==================================
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

        # ==================================
        # TOP FORM
        # ==================================
        top_form = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        top_form.pack(
            fill="x",
            padx=35,
            pady=(35, 10)
        )

        # ==================================
        # CLASS SECTION
        # ==================================
        class_frame = ctk.CTkFrame(
            top_form,
            fg_color="transparent"
        )

        class_frame.pack(side="left")

        ctk.CTkLabel(
            class_frame,
            text="Class",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")

        selected_class = (
            self.class_data["name"]
            if self.class_data
            else self.classes[0]
        )

        # OPENED FROM CLASS DETAIL
        if self.class_data:

            class_box = ctk.CTkFrame(
                class_frame,
                fg_color="#111827",
                corner_radius=14,
                height=48,
                width=260
            )

            class_box.pack()

            class_box.pack_propagate(False)

            ctk.CTkLabel(
                class_box,
                text=selected_class,
                font=("Segoe UI", 15, "bold")
            ).pack(
                pady=12
            )

        # OPENED FROM SIDEBAR
        else:

            self.class_dropdown = ctk.CTkComboBox(
                class_frame,
                values=self.classes,
                width=260,
                height=48
            )

            self.class_dropdown.set(selected_class)

            self.class_dropdown.pack()

        # ==================================
        # DATE
        # ==================================
        date_frame = ctk.CTkFrame(
            top_form,
            fg_color="transparent"
        )

        date_frame.pack(
            side="left",
            padx=30
        )

        ctk.CTkLabel(
            date_frame,
            text="Date",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")

        self.date_entry = ctk.CTkEntry(
            date_frame,
            width=220,
            height=48
        )

        self.date_entry.insert(
            0,
            datetime.now().strftime("%d/%m/%Y")
        )

        self.date_entry.pack()

        # ==================================
        # STUDENT LIST
        # ==================================
        title = ctk.CTkLabel(
            container,
            text="Student Attendance",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(15, 15)
        )

        list_frame = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        list_frame.pack(
            fill="both",
            expand=True,
            padx=35
        )

        self.attendance_controls = {}

        for student in self.students:

            row = ctk.CTkFrame(
                list_frame,
                fg_color="#111827",
                corner_radius=20,
                height=72
            )

            row.pack(
                fill="x",
                pady=8
            )

            row.pack_propagate(False)

            ctk.CTkLabel(
                row,
                text=student,
                font=("Segoe UI", 18, "bold")
            ).pack(
                side="left",
                padx=25
            )

            dropdown = ctk.CTkComboBox(
                row,
                values=[
                    "Present",
                    "Absent",
                    "Late",
                    "Excused"
                ],
                width=180,
                height=42
            )

            dropdown.set("Present")

            dropdown.pack(
                side="right",
                padx=25
            )

            self.attendance_controls[student] = dropdown

        # ==================================
        # SAVE BUTTON
        # ==================================
        save_btn = ctk.CTkButton(
            container,
            text="Save Attendance",
            height=56,
            corner_radius=18,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 18, "bold"),
            command=self.save_attendance
        )

        save_btn.pack(
            fill="x",
            padx=35,
            pady=(25, 35)
        )