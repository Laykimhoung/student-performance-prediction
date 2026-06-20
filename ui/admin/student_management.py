import customtkinter as ctk

from database.crud import get_student_class_cards
from ui.admin.student_class_detail import StudentClassDetailPage


class StudentManagementPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.classes = get_student_class_cards()

        self.build_ui()

    def open_class(self, class_data):

        parent = self.master

        self.destroy()

        StudentClassDetailPage(
            parent,
            class_data
        ).pack(
            fill="both",
            expand=True
        )

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Student Management",
            font=("Segoe UI", 38, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage students by classroom",
            font=("Segoe UI", 16),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=35
        )

        body = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)

        for index, row in enumerate(self.classes):

            class_id = row[0]
            class_name = row[1]
            total_students = row[2]

            card_data = {
                "id": class_id,
                "name": class_name
            }

            r = index // 2
            c = index % 2

            card = ctk.CTkFrame(
                body,
                fg_color="#0F172A",
                corner_radius=25,
                height=220
            )

            card.grid(
                row=r,
                column=c,
                sticky="nsew",
                padx=10,
                pady=10
            )

            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=class_name,
                font=("Segoe UI", 26, "bold")
            ).pack(
                anchor="w",
                padx=25,
                pady=(25, 15)
            )

            ctk.CTkLabel(
                card,
                text=f"{total_students} Students",
                font=("Segoe UI", 18),
                text_color="#3B82F6"
            ).pack(
                anchor="w",
                padx=25
            )

            ctk.CTkButton(
                card,
                text="Manage Students",
                height=45,
                corner_radius=14,
                command=lambda d=card_data:
                self.open_class(d)
            ).pack(
                fill="x",
                padx=25,
                pady=(40, 25)
            )