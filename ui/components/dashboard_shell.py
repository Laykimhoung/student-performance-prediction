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

        self.menu_buttons = {}
        self.active_button = None

        self.parent = parent
        self.role_name = role_name
        self.accent_color = accent_color
        self.menu_items = menu_items

        self.content = None

        self.build_ui()

    # ==================================
    # NAVIGATION
    # ==================================
    def navigate(self, page_name):
        pass

    # ==================================
    # LOGOUT
    # ==================================
    def logout(self):

        self.destroy()

        self.parent.show_role_selection()

    # ==================================
    # MENU SELECTION
    # ==================================
    def select_menu(self, page_name):

        # Reset all buttons
        for btn in self.menu_buttons.values():
            btn.configure(
                fg_color="#172033"
            )

        # Highlight selected button
        self.menu_buttons[page_name].configure(
            fg_color=self.accent_color
        )

        self.active_button = page_name

        self.navigate(page_name)

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==================================
        # SIDEBAR
        # ==================================
        sidebar = ctk.CTkFrame(
            self,
            width=280,
            fg_color="#111827",
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        sidebar.grid_propagate(False)

        # Logo
        logo = ctk.CTkLabel(
            sidebar,
            text="EduVision AI",
            font=("Segoe UI", 32, "bold")
        )
        logo.pack(pady=(40, 5))

        subtitle = ctk.CTkLabel(
            sidebar,
            text=f"{self.role_name} Panel",
            text_color="#94A3B8",
            font=("Segoe UI", 14)
        )
        subtitle.pack()

        divider = ctk.CTkFrame(
            sidebar,
            height=2,
            fg_color="#1E293B"
        )

        divider.pack(
            fill="x",
            padx=25,
            pady=30
        )

        # ==================================
        # MENU BUTTONS
        # ==================================
        for item in self.menu_items:

            btn = ctk.CTkButton(
                sidebar,
                text=item,
                height=54,
                corner_radius=18,
                fg_color="#172033",
                hover_color=self.accent_color,
                font=("Segoe UI", 17),
                anchor="w",
                command=lambda x=item: self.select_menu(x)
            )

            btn.pack(
                fill="x",
                padx=22,
                pady=7
            )

            self.menu_buttons[item] = btn

        # Logout
        logout_btn = ctk.CTkButton(
            sidebar,
            text="Logout",
            height=54,
            corner_radius=18,
            fg_color="#991B1B",
            hover_color="#DC2626",
            font=("Segoe UI", 17),
            command=self.logout
        )

        logout_btn.pack(
            side="bottom",
            fill="x",
            padx=22,
            pady=25
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

        if self.menu_items:
            self.after(
                100,
                lambda: self.select_menu(self.menu_items[0])
            )