import customtkinter as ctk


class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#0F172A")

        label = ctk.CTkLabel(
            self,
            text="Settings",
            font=("Segoe UI", 40, "bold")
        )
        label.pack(pady=70)