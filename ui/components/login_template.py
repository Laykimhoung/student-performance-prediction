import customtkinter as ctk
from PIL import Image


class LoginTemplate(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        role_name="Teacher",
        accent_color="#EF4444",
        accent_hover="#DC2626",
        accent_bg="#7F1D1D",
        icon_path="assets/icons/teacher2.png",
        hero_title="Welcome.",
        hero_subtitle="Access your dashboard securely",
        login_command=None
    ):
        super().__init__(parent, fg_color="#071224")

        self.role_name = role_name
        self.accent_color = accent_color
        self.accent_hover = accent_hover
        self.accent_bg = accent_bg
        self.icon_path = icon_path
        self.hero_title = hero_title
        self.hero_subtitle = hero_subtitle
        self.login_command = login_command

        self.password_visible = False

        self.build_ui()

    # ==================================
    # PASSWORD TOGGLE
    # ==================================
    def toggle_password(self):

        if self.password_visible:
            self.password_entry.configure(show="●")
            self.eye_btn.configure(text="👁")
            self.password_visible = False
        else:
            self.password_entry.configure(show="")
            self.eye_btn.configure(text="🙈")
            self.password_visible = True

    # ==================================
    # BUTTON HOVER EFFECT
    # ==================================
    def button_hover(self):

        self.login_btn.configure(
            width=320,
            height=58
        )

    def button_leave(self):

        self.login_btn.configure(
            width=300,
            height=54
        )

    def build_ui(self):

        # ==================================
        # MAIN WRAPPER
        # ==================================
        wrapper = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        wrapper.pack(
            fill="both",
            expand=True,
            padx=80,
            pady=60
        )

        # ==================================
        # MAIN CARD
        # ==================================
        card = ctk.CTkFrame(
            wrapper,
            fg_color="#121212",
            corner_radius=35
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.88,
            relheight=0.78
        )

        # ==================================
        # LEFT PANEL (LOGIN)
        # ==================================
        left_panel = ctk.CTkFrame(
            card,
            width=430,
            fg_color="#F7F7F7",
            corner_radius=35
        )

        left_panel.pack(
            side="left",
            fill="y"
        )

        # Logo
        logo = ctk.CTkLabel(
            left_panel,
            text="EduVision AI",
            font=("Segoe UI", 28, "bold"),
            text_color="#111827"
        )
        logo.pack(pady=(40, 25))

        # Icon Circle
        icon_bg = ctk.CTkFrame(
            left_panel,
            width=100,
            height=100,
            corner_radius=50,
            fg_color=self.accent_bg
        )
        icon_bg.pack(pady=(15, 20))

        icon = ctk.CTkImage(
            light_image=Image.open(self.icon_path),
            dark_image=Image.open(self.icon_path),
            size=(52, 52)
        )

        icon_label = ctk.CTkLabel(
            icon_bg,
            image=icon,
            text=""
        )
        icon_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Title
        title = ctk.CTkLabel(
            left_panel,
            text=f"{self.role_name} Login",
            font=("Segoe UI", 30, "bold"),
            text_color="#111827"
        )
        title.pack()

        subtitle = ctk.CTkLabel(
            left_panel,
            text="Secure access to dashboard",
            font=("Segoe UI", 15),
            text_color="#6B7280"
        )
        subtitle.pack(pady=(0, 25))

        # Username
        self.username_entry = ctk.CTkEntry(
            left_panel,
            width=300,
            height=50,
            corner_radius=20,
            placeholder_text="Username",
            fg_color="#FFFFFF",
            border_color="#D1D5DB",
            text_color="#111827"
        )
        self.username_entry.pack(pady=10)

        # Password
        password_frame = ctk.CTkFrame(
            left_panel,
            fg_color="transparent"
        )
        password_frame.pack(pady=10)

        self.password_entry = ctk.CTkEntry(
            password_frame,
            width=235,
            height=50,
            corner_radius=20,
            placeholder_text="Password",
            show="●",
            fg_color="#FFFFFF",
            border_color="#D1D5DB",
            text_color="#111827"
        )
        self.password_entry.pack(side="left")

        self.eye_btn = ctk.CTkButton(
            password_frame,
            text="👁",
            width=55,
            height=50,
            corner_radius=18,
            fg_color="#E5E7EB",
            hover_color="#D1D5DB",
            text_color="#111827",
            command=self.toggle_password
        )
        self.eye_btn.pack(side="left", padx=(10, 0))

        # Login button
        self.login_btn = ctk.CTkButton(
            left_panel,
            text="LOGIN",
            width=300,
            height=54,
            corner_radius=22,
            fg_color=self.accent_color,
            hover_color=self.accent_hover,
            font=("Segoe UI", 16, "bold"),
            command=self.login_command
        )
        self.login_btn.pack(pady=(30, 20))

        self.login_btn.bind(
            "<Enter>",
            lambda e: self.button_hover()
        )

        self.login_btn.bind(
            "<Leave>",
            lambda e: self.button_leave()
        )

        footer = ctk.CTkLabel(
            left_panel,
            text="EduVision AI Secure Access",
            text_color="#6B7280",
            font=("Segoe UI", 12)
        )
        footer.pack(side="bottom", pady=25)

        # ==================================
        # RIGHT PANEL
        # ==================================
        right_panel = ctk.CTkFrame(
            card,
            fg_color="#161616"
        )
        right_panel.pack(
            side="left",
            fill="both",
            expand=True
        )

        glow = ctk.CTkFrame(
            right_panel,
            width=520,
            height=520,
            corner_radius=260,
            fg_color="#2A2A2A"
        )
        glow.place(
            relx=0.55,
            rely=0.45,
            anchor="center"
        )

        hero = ctk.CTkLabel(
            right_panel,
            text=self.hero_title,
            font=("Segoe UI", 52, "bold")
        )
        hero.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        hero_sub = ctk.CTkLabel(
            right_panel,
            text=self.hero_subtitle,
            font=("Segoe UI", 18),
            text_color="#A1A1AA"
        )
        hero_sub.place(
            relx=0.5,
            rely=0.58,
            anchor="center"
        )