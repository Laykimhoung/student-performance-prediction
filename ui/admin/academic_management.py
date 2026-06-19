import customtkinter as ctk
from tkinter import messagebox

from database.crud import get_all_classes
from database.crud import get_all_teachers
from database.crud import get_total_teachers
from database.crud import get_teacher_by_id
from database.crud import delete_teacher
from database.crud import get_class_by_id
from database.crud import delete_class

from ui.admin.add_teacher_dialog import AddTeacherDialog
from ui.admin.add_class_dialog import AddClassDialog

class AcademicManagementPage(ctk.CTkFrame):

    def open_add_teacher(self):

        AddTeacherDialog(
            self,
            self.refresh_page
        )

    def refresh_page(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.classes = get_all_classes()

        self.build_ui()

    def edit_teacher(self, teacher_id):

        teacher = get_teacher_by_id(
            teacher_id
        )

        AddTeacherDialog(
            self,
            self.refresh_page,
            teacher
        )

    def remove_teacher(self, teacher_id):

        confirm = messagebox.askyesno(
            "Delete Teacher",
            "Are you sure you want to delete this teacher?"
        )

        if not confirm:
            return

        delete_teacher(teacher_id)

        self.refresh_page()

    def search_teachers(self, event=None):

        keyword = self.teacher_search.get().lower()

        for widget in self.teacher_table.winfo_children():
            widget.destroy()

        headers = [
            "ID",
            "Teacher",
            "Username",
            "Actions"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                self.teacher_table,
                text=header,
                font=("Segoe UI", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=(0, 15),
                sticky="w"
            )
        
        row_num = 1

        for teacher in self.teachers:

            teacher_id = str(teacher[0])

            if (
                keyword in teacher_id.lower()
                or
                keyword in teacher[1].lower()
                or
                keyword in teacher[2].lower()
            ):

                values = [
                    teacher[0],
                    teacher[2],
                    teacher[1]
                ]

                for col_index, value in enumerate(values):

                    ctk.CTkLabel(
                        self.teacher_table,
                        text=str(value),
                        font=("Segoe UI", 13)
                    ).grid(
                        row=row_num,
                        column=col_index,
                        padx=15,
                        pady=8,
                        sticky="w"
                    )

                action_frame = ctk.CTkFrame(
                    self.teacher_table,
                    fg_color="transparent"
                )

                action_frame.grid(
                    row=row_num,
                    column=3,
                    padx=10,
                    sticky="w"
                )

                ctk.CTkButton(
                    action_frame,
                    text="Edit",
                    width=60,
                    height=28,
                    fg_color="#F59E0B",
                    command=lambda t=teacher:
                        self.edit_teacher(t[0])
                ).pack(side="left", padx=3)

                ctk.CTkButton(
                    action_frame,
                    text="Delete",
                    width=60,
                    height=28,
                    fg_color="#DC2626",
                    command=lambda t=teacher:
                        self.remove_teacher(t[0])
                ).pack(side="left", padx=3)

                row_num += 1

    def open_add_class(self):

        AddClassDialog(
            self,
            self.refresh_page
        )

    def edit_class(self, class_id):

        class_data = get_class_by_id(
            class_id
        )

        AddClassDialog(
            self,
            self.refresh_page,
            class_data
        )

    def remove_class(self, class_id):

        confirm = messagebox.askyesno(
            "Delete Class",
            "Are you sure you want to delete this class?"
        )

        if not confirm:
            return

        delete_class(class_id)

        self.refresh_page()

    def search_classes(self, event=None):

        keyword = self.class_search.get().lower()

        for widget in self.class_table.winfo_children():
            widget.destroy()

        headers = [
            "ID",
            "Class",
            "Teacher",
            "Actions"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                self.class_table,
                text=header,
                font=("Segoe UI", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=(0, 15),
                sticky="w"
            )

        row_num = 1

        for row in self.classes:

            class_name = str(row[1]).lower()

            teacher_name = (
                str(row[2]).lower()
                if row[2]
                else ""
            )

            class_id = str(row[0])

            if (
                keyword in class_id.lower()
                or
                keyword in class_name
                or
                keyword in teacher_name
            ):

                values = [
                    row[0],
                    row[1],
                    row[2] if row[2] else "Not Assigned"
                ]

                for col_index, value in enumerate(values):

                    ctk.CTkLabel(
                        self.class_table,
                        text=str(value),
                        font=("Segoe UI", 13)
                    ).grid(
                        row=row_num,
                        column=col_index,
                        padx=15,
                        pady=8,
                        sticky="w"
                    )

                action_frame = ctk.CTkFrame(
                    self.class_table,
                    fg_color="transparent"
                )

                action_frame.grid(
                    row=row_num,
                    column=3,
                    padx=10,
                    sticky="w"
                )

                ctk.CTkButton(
                    action_frame,
                    text="Edit",
                    width=60,
                    height=28,
                    fg_color="#F59E0B",
                    command=lambda c=row:
                        self.edit_class(c[0])
                ).pack(side="left", padx=3)

                ctk.CTkButton(
                    action_frame,
                    text="Delete",
                    width=60,
                    height=28,
                    fg_color="#DC2626",
                    command=lambda c=row:
                        self.remove_class(c[0])
                ).pack(side="left", padx=3)

                row_num += 1
        
    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.teachers = get_all_teachers()
        self.classes = get_all_classes()

        self.build_ui()

    def build_ui(self):

        # ==========================
        # TITLE
        # ==========================
        title = ctk.CTkLabel(
            self,
            text="Academic Management",
            font=("Segoe UI", 32, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        # ==========================
        # STATISTICS
        # ==========================
        stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        total_classes = len(self.classes)

        assigned = len([
            row for row in self.classes
            if row[2] is not None
        ])

        unassigned = total_classes - assigned

        stats = [
            ("Teachers", get_total_teachers()),
            ("Classes", total_classes),
            ("Assigned", assigned),
            ("Available", unassigned)
        ]

        for i, (title, value) in enumerate(stats):

            stats_frame.grid_columnconfigure(
                i,
                weight=1
            )

            card = ctk.CTkFrame(
                stats_frame,
                fg_color="#0F172A",
                corner_radius=20,
                height=100
            )

            card.grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=8
            )

            ctk.CTkLabel(
                card,
                text=str(value),
                font=("Segoe UI", 28, "bold"),
                text_color="#3B82F6"
            ).pack(
                pady=(18, 2)
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14),
                text_color="#94A3B8"
            ).pack()
    
        # ==========================
        # TABLE FRAME
        # ==========================
        content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        content_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)

        # ==========================
        # TEACHERS PANEL
        # ==========================
        teacher_frame = ctk.CTkFrame(
            content_frame,
            fg_color="#0F172A",
            corner_radius=20
        )

        teacher_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        ctk.CTkLabel(
            teacher_frame,
            text="Teachers",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        teacher_toolbar = ctk.CTkFrame(
            teacher_frame,
            fg_color="transparent"
        )

        teacher_toolbar.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.teacher_search = ctk.CTkEntry(
            teacher_toolbar,
            placeholder_text="Search teacher..."
        )

        self.teacher_search.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.teacher_search.bind(
            "<KeyRelease>",
            self.search_teachers
        )

        teacher_add_btn = ctk.CTkButton(
            teacher_toolbar,
            text="+ Add Teacher",
            width=130,
            command=self.open_add_teacher
        )

        teacher_add_btn.pack(
            side="right"
        )

        self.teacher_table = ctk.CTkScrollableFrame(
            teacher_frame,
            fg_color="transparent"
        )

        self.teacher_table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        self.teacher_table.grid_columnconfigure(0, minsize=50)
        self.teacher_table.grid_columnconfigure(1, minsize=180)
        self.teacher_table.grid_columnconfigure(2, minsize=140)
        self.teacher_table.grid_columnconfigure(3, minsize=180)

        headers = [
            "ID",
            "Teacher",
            "Username",
            "Actions"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                self.teacher_table,
                text=header,
                font=("Segoe UI", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=(0, 15),
                sticky="w"
            )

        teachers = get_all_teachers()

        for row_index, teacher in enumerate(teachers, start=1):

            row_color = "#111827" if row_index % 2 == 0 else "#0B1324"

            row_frame = ctk.CTkFrame(
                self.teacher_table,
                fg_color=row_color,
                corner_radius=10,
                height=45
            )

            row_frame.grid(
                row=row_index,
                column=0,
                columnspan=4,
                sticky="nsew",
                pady=4,
                padx=5
            )

            row_frame.grid_columnconfigure(0, minsize=50)
            row_frame.grid_columnconfigure(1, minsize=180)
            row_frame.grid_columnconfigure(2, minsize=140)
            row_frame.grid_columnconfigure(3, minsize=180)

            values = [
                teacher[0],
                teacher[2],
                teacher[1]
            ]

            for col_index, value in enumerate(values):

                ctk.CTkLabel(
                    row_frame,
                    text=str(value),
                    font=("Segoe UI", 13)
                ).grid(
                    row=0,
                    column=col_index,
                    padx=15,
                    pady=10,
                    sticky="w"
                )

            action_frame = ctk.CTkFrame(
                row_frame,
                fg_color="transparent"
            )

            action_frame.grid(
                row=0,
                column=3,
                padx=10,
                sticky="e"
            )

            ctk.CTkButton(
                action_frame,
                text="Edit",
                width=60,
                height=28,
                fg_color="#F59E0B",
                command=lambda t=teacher:
                    self.edit_teacher(t[0])
            ).pack(side="left", padx=3)

            ctk.CTkButton(
                action_frame,
                text="Delete",
                width=60,
                height=28,
                fg_color="#DC2626",
                command=lambda t=teacher:
                    self.remove_teacher(t[0])
            ).pack(side="left", padx=3)

        # ==========================
        # CLASSES PANEL
        # ==========================
        class_frame = ctk.CTkFrame(
            content_frame,
            fg_color="#0F172A",
            corner_radius=20
        )

        class_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        ctk.CTkLabel(
            class_frame,
            text="Classes",
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        class_toolbar = ctk.CTkFrame(
            class_frame,
            fg_color="transparent"
        )

        class_toolbar.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.class_search = ctk.CTkEntry(
            class_toolbar,
            placeholder_text="Search class..."
        )

        self.class_search.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.class_search.bind(
            "<KeyRelease>",
            self.search_classes
        )
        
        class_add_btn = ctk.CTkButton(
            class_toolbar,
            text="+ Add Class",
            width=130,
            command=self.open_add_class
        )

        class_add_btn.pack(
            side="right"
        )

        self.class_table = ctk.CTkScrollableFrame(
            class_frame,
            fg_color="transparent"
        )

        self.class_table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 20)
        )

        self.class_table.grid_columnconfigure(0, minsize=50)
        self.class_table.grid_columnconfigure(1, minsize=140)
        self.class_table.grid_columnconfigure(2, minsize=180)
        self.class_table.grid_columnconfigure(3, minsize=180)

        headers = [
            "ID",
            "Class",
            "Teacher",
            "Actions"
        ]

        for col, header in enumerate(headers):

            ctk.CTkLabel(
                self.class_table,
                text=header,
                font=("Segoe UI", 14, "bold")
            ).grid(
                row=0,
                column=col,
                padx=15,
                pady=(0, 15),
                sticky="w"
            )
        
        for row_index, row in enumerate(self.classes, start=1):

            row_color = "#111827" if row_index % 2 == 0 else "#0B1324"

            teacher_name = row[2] if row[2] else "Not Assigned"

            row_frame = ctk.CTkFrame(
                self.class_table,
                fg_color=row_color,
                corner_radius=10,
                height=45
            )

            row_frame.grid(
                row=row_index,
                column=0,
                columnspan=4,
                sticky="nsew",
                pady=4,
                padx=5
            )

            row_frame.grid_columnconfigure(0, minsize=50)
            row_frame.grid_columnconfigure(1, minsize=140)
            row_frame.grid_columnconfigure(2, minsize=180)
            row_frame.grid_columnconfigure(3, minsize=180)

            values = [
                row[0],
                row[1],
                teacher_name
            ]

            for col_index, value in enumerate(values):

                ctk.CTkLabel(
                    row_frame,
                    text=str(value),
                    font=("Segoe UI", 13)
                ).grid(
                    row=0,
                    column=col_index,
                    padx=15,
                    pady=10,
                    sticky="w"
                )

            action_frame = ctk.CTkFrame(
                row_frame,
                fg_color="transparent"
            )

            action_frame.grid(
                row=0,
                column=3,
                padx=10,
                sticky="e"
            )

            ctk.CTkButton(
                action_frame,
                text="Edit",
                width=60,
                height=28,
                fg_color="#F59E0B",
                command=lambda c=row:
                    self.edit_class(c[0])
            ).pack(side="left", padx=3)

            ctk.CTkButton(
                action_frame,
                text="Delete",
                width=60,
                height=28,
                fg_color="#DC2626",
                command=lambda c=row:
                    self.remove_class(c[0])
            ).pack(side="left", padx=3)