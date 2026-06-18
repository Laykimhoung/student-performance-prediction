import customtkinter as ctk

from database.crud import add_teacher


class AddTeacherDialog(ctk.CTkToplevel):

    def __init__(self, parent, refresh_callback):

        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.title("Add Teacher")

        self.geometry("450x350")

        self.resizable(False, False)

        self.build_ui()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Add Teacher",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(20, 15)
        )

        self.username_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Username"
        )

        self.username_entry.pack(
            pady=10
        )

        self.password_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Password"
        )

        self.password_entry.pack(
            pady=10
        )

        self.fullname_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Full Name"
        )

        self.fullname_entry.pack(
            pady=10
        )

        ctk.CTkButton(
            self,
            text="Save Teacher",
            width=180,
            command=self.save_teacher
        ).pack(
            pady=25
        )

    def save_teacher(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get().strip()

        fullname = self.fullname_entry.get().strip()

        if not username or not password or not fullname:
            return

        add_teacher(
            username,
            password,
            fullname
        )

        self.refresh_callback()

        self.destroy()