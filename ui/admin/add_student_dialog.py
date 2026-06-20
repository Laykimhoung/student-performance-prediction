import customtkinter as ctk

from database.crud import (
    add_student,
    update_student,
    generate_student_code
)


class AddStudentDialog(ctk.CTkToplevel):

    def __init__(
            self,
            parent,
            class_id,
            refresh_callback,
            student=None
        ):

        super().__init__(parent)

        self.refresh_callback = refresh_callback
        self.student = student
        self.class_id = class_id

        self.title(
            "Edit Student"
            if self.student
            else "Add Student"
        )

        self.geometry("500x520")

        self.resizable(False, False)

        self.update_idletasks()

        width = 500
        height = 520

        x = (
            self.winfo_screenwidth() // 2
        ) - (
            width // 2
        )

        y = (
            self.winfo_screenheight() // 2
        ) - (
            height // 2
        )

        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        # Bring window to front
        self.after(100, self.show_dialog)

        self.build_ui()

    def show_dialog(self):

            self.lift()
            self.focus_force()

            self.grab_set()

            self.attributes("-topmost", True)
            self.after(
                200,
                lambda: self.attributes("-topmost", False)
            )


    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Edit Student" if self.student else "Add Student",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(20, 15)
        )

        # ==========================
        # STUDENT CODE
        # ==========================
        if self.student:
            self.student_code = self.student[1]
        else:
            self.student_code = generate_student_code()

        ctk.CTkLabel(
            self,
            text=f"Student Code: {self.student_code}",
            font=("Segoe UI", 14)
        ).pack(
            pady=10
        )

        # ==========================
        # STUDENT NAME
        # ==========================
        self.name_entry = ctk.CTkEntry(
            self,
            width=350,
            height=40,
            placeholder_text="Student Name"
        )

        self.name_entry.pack(
            pady=10
        )

        # ==========================
        # GENDER
        # ==========================
        self.gender_dropdown = ctk.CTkOptionMenu(
            self,
            width=350,
            values=[
                "Male",
                "Female"
            ]
        )

        self.gender_dropdown.pack(
            pady=10
        )

        # ==========================
        # EDIT MODE
        # ==========================
        if self.student:

            self.name_entry.insert(
                0,
                self.student[2]
            )

            self.gender_dropdown.set(
                self.student[3]
            )

        # ==========================
        # SAVE BUTTON
        # ==========================
        ctk.CTkButton(
            self,
            text="Save Student",
            width=200,
            height=40,
            command=self.save_student
        ).pack(
            pady=25
        )

    def save_student(self):

        student_code = self.student_code

        student_name = self.name_entry.get().strip()

        gender = self.gender_dropdown.get()

        class_id = self.class_id

        if self.student:

            update_student(
                self.student[0],
                student_code,
                student_name,
                gender,
                class_id
            )

        else:

            add_student(
                student_code,
                student_name,
                gender,
                class_id
            )

        self.refresh_callback()

        self.destroy()