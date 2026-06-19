import customtkinter as ctk

from database.crud import (
    add_class,
    get_all_teachers,
    update_class
)


class AddClassDialog(ctk.CTkToplevel):

    def __init__(
            self,
            parent,
            refresh_callback,
            class_data=None
        ):

        super().__init__(parent)

        self.transient(parent)
        self.grab_set()
        self.focus_force()

        self.refresh_callback = refresh_callback

        self.class_data = class_data

        self.title(
            "Edit Class"
            if self.class_data
            else "Add Class"
        )

        # Center Dialog
        self.update_idletasks()

        x = parent.winfo_rootx() + (
            parent.winfo_width() // 2
        ) - 225

        y = parent.winfo_rooty() + (
            parent.winfo_height() // 2
        ) - 175

        self.geometry(f"450x350+{x}+{y}")

        self.lift()
        self.attributes("-topmost", True)

        self.after(
            100,
            lambda: self.attributes("-topmost", False)
        )

        self.resizable(False, False)

        self.teachers = get_all_teachers()

        self.build_ui()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Edit Class" if self.class_data else "Add Class",
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

        if self.class_data:

            self.class_entry.insert(
                0,
                self.class_data[1]
            )

            teacher_id = self.class_data[2]

            for teacher in self.teachers:

                if teacher[0] == teacher_id:

                    self.teacher_dropdown.set(
                        teacher[1]
                    )

                    break
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

        if self.class_data:

            update_class(
                self.class_data[0],
                class_name,
                teacher_id
            )

        else:

            add_class(
                class_name,
                teacher_id
            )

        self.refresh_callback()

        self.destroy()