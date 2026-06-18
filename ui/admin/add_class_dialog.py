import customtkinter as ctk

from database.crud import (
    add_class,
    get_all_teachers
)


class AddClassDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add Class")

        self.geometry("450x350")

        self.resizable(False, False)

        self.teachers = get_all_teachers()

        self.build_ui()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Add Class",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(20, 15)
        )

        self.class_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Class Name"
        )

        self.class_entry.pack(
            pady=10
        )

        teacher_names = [
            teacher[1]
            for teacher in self.teachers
        ]

        self.teacher_dropdown = ctk.CTkOptionMenu(
            self,
            width=300,
            values=teacher_names
        )

        self.teacher_dropdown.pack(
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Save Class",
            width=180,
            command=self.save_class
        ).pack(
            pady=25
        )

    def save_class(self):

        class_name = self.class_entry.get().strip()

        selected_teacher = self.teacher_dropdown.get()

        if not class_name:
            return

        teacher_id = None

        for teacher in self.teachers:

            if teacher[1] == selected_teacher:
                teacher_id = teacher[0]
                break

        add_class(
            class_name,
            teacher_id
        )

        self.refresh_callback()

        self.destroy()