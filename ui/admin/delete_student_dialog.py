import customtkinter as ctk

from database.crud import delete_student


class DeleteStudentDialog(ctk.CTkToplevel):

    def __init__(
            self,
            parent,
            student_id,
            student_name,
            refresh_callback
        ):

        super().__init__(parent)

        self.student_id = student_id
        self.refresh_callback = refresh_callback

        self.title("Delete Student")

        self.geometry("400x220")

        self.resizable(False, False)

        self.update_idletasks()

        width = 400
        height = 220

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

        self.after(
            100,
            self.show_dialog
        )
    
        self.build_ui(student_name)

    def show_dialog(self):

        self.lift()

        self.focus_force()

        self.grab_set()

        self.attributes("-topmost", True)

        self.after(
            200,
            lambda: self.attributes(
                "-topmost",
                False
            )
        )

    def build_ui(self, student_name):

        ctk.CTkLabel(
            self,
            text="Delete Student",
            font=("Segoe UI", 22, "bold")
        ).pack(
            pady=(25, 10)
        )

        ctk.CTkLabel(
            self,
            text=f"Are you sure you want to delete\n{student_name}?",
            font=("Segoe UI", 15)
        ).pack(
            pady=(0, 20)
        )

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack()

        ctk.CTkButton(
            button_frame,
            text="Cancel",
            width=120,
            command=self.destroy
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            button_frame,
            text="Delete",
            width=120,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.confirm_delete
        ).pack(
            side="left",
            padx=10
        )

    def confirm_delete(self):

        delete_student(
            self.student_id
        )

        self.refresh_callback()

        self.destroy()