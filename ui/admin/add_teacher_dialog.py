import customtkinter as ctk

from database.crud import add_teacher
from database.crud import update_teacher


class AddTeacherDialog(ctk.CTkToplevel):

    def __init__(
            self,
            parent,
            refresh_callback,
            teacher=None
        ):

        super().__init__(parent)

        # Keep dialog in front
        self.transient(parent)
        self.grab_set()
        self.focus_force()

        self.refresh_callback = refresh_callback
        self.teacher = teacher

        if self.teacher:
            self.title("Edit Teacher")
        else:
            self.title("Add Teacher")

        # Center dialog
        self.update_idletasks()

        x = parent.winfo_rootx() + (
            parent.winfo_width() // 2
        ) - 225

        y = parent.winfo_rooty() + (
            parent.winfo_height() // 2
        ) - 175

        self.geometry(f"450x350+{x}+{y}")

        # Bring to front
        self.lift()
        self.attributes("-topmost", True)

        self.after(
            100,
            lambda: self.attributes("-topmost", False)
        )

        self.resizable(False, False)

        self.build_ui()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Edit Teacher" if self.teacher else "Add Teacher",
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

        if self.teacher:
            self.password_entry.pack_forget()

        self.fullname_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Full Name"
        )

        self.fullname_entry.pack(
            pady=10
        )

        if self.teacher:

            self.username_entry.insert(
                0,
                self.teacher[1]
            )

            self.fullname_entry.insert(
                0,
                self.teacher[2]
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

        if not username or not fullname:
            return

        if self.teacher:

            update_teacher(
                self.teacher[0],
                username,
                fullname
            )

        else:

            if not password:
                return

            add_teacher(
                username,
                password,
                fullname
            )

        self.refresh_callback()

        self.destroy()