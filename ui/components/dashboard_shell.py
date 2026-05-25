import customtkinter as ctk


class DashboardShell(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        role_name,
        accent_color,
        menu_items
    ):
        super().__init__(parent, fg_color="#071224")

        self.parent = parent
        self.role_name = role_name
        self.accent_color = accent_color
        self.menu_items = menu_items

        self.build_ui()

    def build_ui(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==================================
        # SIDEBAR
        # ==================================
        self.sidebar = ctk.CTkFrame(
            self,
            width=270,
            fg_color="#111827",
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.sidebar.grid_propagate(False)

        # ==================================
        # LOGO
        # ==================================
        logo = ctk.CTkLabel(
            self.sidebar,
            text="EduVision AI",
            font=("Segoe UI", 34, "bold")
        )
        logo.pack(pady=(45, 8))

        role = ctk.CTkLabel(
            self.sidebar,
            text=f"{self.role_name} Panel",
            font=("Segoe UI", 15),
            text_color="#94A3B8"
        )
        role.pack()

        divider = ctk.CTkFrame(
            self.sidebar,
            height=2,
            fg_color="#1E293B"
        )

        divider.pack(
            fill="x",
            padx=28,
            pady=35
        )

        # ==================================
        # MENU
        # ==================================
        for item in self.menu_items:

            btn = ctk.CTkButton(
                self.sidebar,
                text=item,
                height=58,
                corner_radius=18,
                fg_color="#172033",
                hover_color=self.accent_color,
                font=("Segoe UI", 18),
                anchor="w"
            )

            btn.pack(
                fill="x",
                padx=24,
                pady=8
            )

        # ==================================
        # LOGOUT BUTTON
        # ==================================
        logout_btn = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            height=58,
            corner_radius=18,
            fg_color="#991B1B",
            hover_color="#DC2626",
            font=("Segoe UI", 18, "bold"),
            command=self.logout
        )

        logout_btn.pack(
            side="bottom",
            fill="x",
            padx=24,
            pady=30
        )

        # ==================================
        # CONTENT
        # ==================================
        self.content = ctk.CTkFrame(
            self,
            fg_color="#071224"
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(20, 35),
            pady=20
        )

        self.content.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

    # ==================================
    # LOGOUT
    # ==================================
    def logout(self):

        self.destroy()

        self.parent.show_role_selection()