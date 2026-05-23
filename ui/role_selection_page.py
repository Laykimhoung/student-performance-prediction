import customtkinter as ctk
from PIL import Image


class RoleSelectionPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="#071224")

        self.role_cards = []
        self.build_ui()

    # ==================================
    # CARD HOVER EFFECT
    # ==================================
    def on_card_hover(self, card, color):

        card.configure(
            border_color=color,
            border_width=3,
            fg_color="#111C34"
        )

    def on_card_leave(self, card):

        card.configure(
            border_color="#1E293B",
            border_width=2,
            fg_color="#0F172A"
        )

    # ==================================
    # BUTTON HOVER
    # ==================================
    def on_button_hover(self, btn, hover_color):

        btn.configure(
            fg_color=hover_color,
            width=235,
            height=54
        )

    def on_button_leave(self, btn, color):

        btn.configure(
            fg_color=color,
            width=220,
            height=50
        )

    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        title = ctk.CTkLabel(
            self,
            text="Choose Your Role",
            font=("Segoe UI", 48, "bold"),
            text_color="#F8FAFC"
        )
        title.pack(pady=(50, 8))

        subtitle = ctk.CTkLabel(
            self,
            text="Select how you want to access EduVision AI",
            font=("Segoe UI", 18),
            text_color="#94A3B8"
        )
        subtitle.pack()

        # ==================================
        # CONTAINER
        # ==================================
        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=40
        )

        container.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        # ==================================
        # ROLE DATA
        # ==================================
        roles = [
            (
                "Admin",
                "Full system control,\nteacher and class management",
                "#3B82F6",
                "#1E3A8A",
                "assets/icons/admin2.png",
                "#60A5FA"
            ),
            (
                "Teacher",
                "Manage classes,\nacademic records and students",
                "#EF4444",
                "#7F1D1D",
                "assets/icons/teacher2.png",
                "#F87171"
            ),
            (
                "Student",
                "Preview academic\nprediction instantly",
                "#10B981",
                "#065F46",
                "assets/icons/student2.png",
                "#34D399"
            )
        ]

        for i, (
            role,
            desc,
            color,
            bg_color,
            icon_path,
            hover_color
        ) in enumerate(roles):

            # ==================================
            # CARD
            # ==================================
            card = ctk.CTkFrame(
                container,
                fg_color="#0F172A",
                corner_radius=30,
                border_width=2,
                border_color="#1E293B"
            )

            card.grid(
                row=0,
                column=i,
                padx=20,
                pady=10,
                sticky="nsew"
            )

            # Hover effect
            card.bind(
                "<Enter>",
                lambda e, c=card, clr=color:
                self.on_card_hover(c, clr)
            )

            card.bind(
                "<Leave>",
                lambda e, c=card:
                self.on_card_leave(c)
            )

            # ==================================
            # ACCENT LINE
            # ==================================
            accent = ctk.CTkFrame(
                card,
                fg_color=color,
                height=5,
                corner_radius=100
            )

            accent.pack(
                fill="x",
                padx=30,
                pady=(28, 28)
            )

            # ==================================
            # ICON BG
            # ==================================
            icon_bg = ctk.CTkFrame(
                card,
                width=110,
                height=110,
                corner_radius=55,
                fg_color=bg_color
            )

            icon_bg.pack(
                pady=(0, 18)
            )

            icon = ctk.CTkImage(
                light_image=Image.open(icon_path),
                dark_image=Image.open(icon_path),
                size=(62, 62)
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

            # ==================================
            # TITLE
            # ==================================
            role_label = ctk.CTkLabel(
                card,
                text=role,
                font=("Segoe UI", 30, "bold"),
                text_color="#F8FAFC"
            )
            role_label.pack()

            # ==================================
            # DESCRIPTION
            # ==================================
            desc_label = ctk.CTkLabel(
                card,
                text=desc,
                wraplength=280,
                justify="center",
                font=("Segoe UI", 16),
                text_color="#94A3B8"
            )

            desc_label.pack(
                padx=30,
                pady=(12, 28)
            )

            # ==================================
            # BUTTON
            # ==================================
            enter_btn = ctk.CTkButton(
                card,
                text="Continue",
                width=220,
                height=50,
                corner_radius=18,
                fg_color=color,
                hover_color=color,
                font=("Segoe UI", 16, "bold")
            )

            enter_btn.pack(
                pady=(0, 28)
            )

            # Button hover animation
            enter_btn.bind(
                "<Enter>",
                lambda e, b=enter_btn, hc=hover_color:
                self.on_button_hover(b, hc)
            )

            enter_btn.bind(
                "<Leave>",
                lambda e, b=enter_btn, c=color:
                self.on_button_leave(b, c)
            )