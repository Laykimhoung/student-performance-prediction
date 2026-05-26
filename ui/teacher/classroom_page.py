import customtkinter as ctk

from ui.teacher.class_detail_page import ClassDetailPage


class ClassroomPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.classes = self.load_classes()

        self.build_ui()

    # ==================================
    # CLASS DATA
    # ==================================
    def load_classes(self):

        return [
            {
                "name": "Grade 12A",
                "students": 36,
                "attendance": 92,
                "average": 84,
                "risk": 4
            },
            {
                "name": "Grade 12B",
                "students": 34,
                "attendance": 89,
                "average": 80,
                "risk": 6
            },
            {
                "name": "Grade 11A",
                "students": 31,
                "attendance": 94,
                "average": 87,
                "risk": 2
            },
            {
                "name": "Grade 11B",
                "students": 29,
                "attendance": 85,
                "average": 77,
                "risk": 7
            }
        ]

    # ==================================
    # OPEN CLASS
    # ==================================
    def open_class(self, class_data):

        parent = self.master

        self.destroy()

        ClassDetailPage(
            parent,
            class_data=class_data,
            back_command=self.go_back
        ).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # BACK
    # ==================================
    def go_back(self):

        parent = self.master

        for widget in parent.winfo_children():
            widget.destroy()

        ClassroomPage(parent).pack(
            fill="both",
            expand=True
        )

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Classroom",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage classes and monitor student performance",
            font=("Segoe UI", 17),
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
            pady=25
        )

        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)

        for index, class_info in enumerate(self.classes):

            row = index // 2
            col = index % 2

            card = ctk.CTkFrame(
                body,
                fg_color="#0F172A",
                corner_radius=28,
                height=260
            )

            card.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=12,
                pady=12
            )

            card.grid_propagate(False)

            # ======================
            # TITLE
            # ======================
            title = ctk.CTkLabel(
                card,
                text=class_info["name"],
                font=("Segoe UI", 28, "bold")
            )

            title.pack(
                anchor="w",
                padx=25,
                pady=(25, 8)
            )

            # ======================
            # STATS
            # ======================
            stats_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            stats_frame.pack(
                fill="x",
                padx=25,
                pady=10
            )

            stats = [
                ("Students", class_info["students"]),
                ("Average", f'{class_info["average"]}%'),
                ("Attendance", f'{class_info["attendance"]}%'),
                ("At Risk", class_info["risk"])
            ]

            for label, value in stats:

                row_frame = ctk.CTkFrame(
                    stats_frame,
                    fg_color="#111827",
                    corner_radius=16,
                    height=44
                )

                row_frame.pack(
                    fill="x",
                    pady=5
                )

                row_frame.pack_propagate(False)

                ctk.CTkLabel(
                    row_frame,
                    text=label,
                    font=("Segoe UI", 15)
                ).pack(
                    side="left",
                    padx=18
                )

                ctk.CTkLabel(
                    row_frame,
                    text=str(value),
                    font=("Segoe UI", 15, "bold"),
                    text_color="#3B82F6"
                ).pack(
                    side="right",
                    padx=18
                )

            # ======================
            # BUTTON
            # ======================
            open_btn = ctk.CTkButton(
                card,
                text="Open Class",
                height=46,
                corner_radius=16,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold"),
                command=lambda c=class_info:
                self.open_class(c)
            )

            open_btn.pack(
                fill="x",
                padx=25,
                pady=(12, 22)
            )