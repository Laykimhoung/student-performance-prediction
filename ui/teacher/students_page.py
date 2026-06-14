import customtkinter as ctk

from ui.teacher.student_detail_page import StudentDetailPage
from database.crud import (
    get_student_list,
    get_all_class_names,
    get_student_detail
)


class StudentsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        class_id=None,
        class_name=None,
        back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.back_command = back_command

        self.class_id = class_id
        self.class_name = class_name

        self.all_students = self.load_students()
        self.students = self.all_students.copy()

        self.build_ui()

    # ==================================
    # LOAD STUDENTS
    # ==================================
    def load_students(self):

        students = []

        for row in get_student_list():

            if self.class_name:

                if row[3] != self.class_name:
                    continue

            students.append(
                {
                    "id": row[0],
                    "code": row[1],
                    "name": row[2],
                    "class": row[3],
                    "average": row[4] or 0,
                    "risk": row[5] or "Low"
                }
            )

        return students

    # ==================================
    # OPEN DETAIL
    # ==================================
    def open_student_detail(self, student_id):

        parent = self.master

        self.destroy()

        def back_to_students():

            detail_page.destroy()

            page = StudentsPage(
                parent,
                class_name=self.class_name,
                back_command=self.back_command
            )

            page.pack(
                fill="both",
                expand=True
            )

        detail_page = StudentDetailPage(
            parent,
            student_id=student_id,
            back_command=back_to_students
        )

        detail_page.pack(
            fill="both",
            expand=True
        )

    # ==================================
    # BACK
    # ==================================
    def go_back(self):

        if self.back_command:
            self.back_command()

    # ==================================
    # PREVIEW
    # ==================================
    def show_preview(self, student):

        detail = get_student_detail(student["id"])

        if not detail:
            return

        risk_color = (
            "#EF4444"
            if detail[15] == "High"
            else "#F59E0B"
            if detail[15] == "Medium"
            else "#10B981"
        )

        self.preview_name.configure(
            text=detail[2]
        )

        self.preview_code.configure(
            text=f"Code: {detail[1]}"
        )

        self.preview_class.configure(
            text=f"Class: {detail[4]}"
        )

        self.preview_average.configure(
            text=f"Average: {detail[14]}"
        )

        self.preview_risk.configure(
            text=f"Risk: {detail[15]}",
            text_color=risk_color
        )

        self.preview_scores.configure(
            text=
            f"Attendance: {detail[7]}\n"
            f"Quiz: {detail[5]}\n"
            f"Homework: {detail[6]}\n"
            f"Assignment: {detail[8]}\n"
            f"Midterm: {detail[9]}\n"
            f"Final: {detail[10]}\n"
            f"Participation: {detail[11]}\n"
            f"Project: {detail[12]}\n"
            f"Behavior: {detail[13]}"
        )

    # ==================================
    # FILTER CLASS
    # ==================================
    def filter_by_class(self, selected_class):

        self.class_name = selected_class

        self.students = []

        for student in self.all_students:

            if student["class"] == selected_class:
                self.students.append(student)

        self.search_entry.delete(0, "end")
        self.refresh_student_list()

    # ==================================
    # SEARCH
    # ==================================
    def search_students(self, event=None):

        keyword = self.search_entry.get().lower()

        self.students = []

        for student in self.all_students:

            if self.class_name:

                if student["class"] != self.class_name:
                    continue

            if (
                keyword in student["name"].lower()
                or
                keyword in student["code"].lower()
            ):

                self.students.append(student)

        self.refresh_student_list()

    # ==================================
    # REFRESH LIST
    # ==================================
    def refresh_student_list(self):

        for widget in self.scroll_table.winfo_children():
            widget.destroy()

        for student in self.students:

            avg = student["average"]

            row = ctk.CTkFrame(
                self.scroll_table,
                fg_color="#111827",
                corner_radius=20,
                height=90
            )

            row.pack(
                fill="x",
                pady=10
            )

            row.pack_propagate(False)

            info_frame = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            info_frame.pack(
                side="left",
                padx=25
            )

            ctk.CTkLabel(
                info_frame,
                text=f'{student["name"]} ({student["code"]})',
                font=("Segoe UI", 18, "bold")
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=f"Average: {avg}",
                font=("Segoe UI", 15),
                text_color="#94A3B8"
            ).pack(anchor="w")

            risk_color = (
                "#EF4444"
                if student["risk"] == "High"
                else "#F59E0B"
                if student["risk"] == "Medium"
                else "#10B981"
            )

            risk_label = ctk.CTkLabel(
                row,
                text=student["risk"],
                font=("Segoe UI", 17, "bold"),
                text_color=risk_color
            )

            risk_label.pack(
                side="left",
                padx=40
            )

            ctk.CTkButton(
                row,
                text="View",
                width=110,
                height=42,
                corner_radius=14,
                fg_color="#EF4444",
                hover_color="#DC2626",
                command=lambda sid=student["id"]:
                self.open_student_detail(sid)
            ).pack(
                side="right",
                padx=25
            )

            row.bind(
                "<Button-1>",
                lambda e, s=student:
                self.show_preview(s)
            )

            info_frame.bind(
                "<Button-1>",
                lambda e, s=student:
                self.show_preview(s)
            )

            risk_label.bind(
                "<Button-1>",
                lambda e, s=student:
                self.show_preview(s)
            )

    # ==================================
    # UI
    # ==================================
    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Students",
            font=("Segoe UI", 40, "bold")
        )

        title.pack(
            anchor="w",
            padx=35,
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage student performance and monitor academic risk",
            font=("Segoe UI", 17),
            text_color="#94A3B8"
        )

        subtitle.pack(
            anchor="w",
            padx=35
        )

        # TOP BAR
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=25
        )

        self.search_entry = ctk.CTkEntry(
            top_bar,
            width=430,
            height=48,
            corner_radius=14,
            placeholder_text="Search student..."
        )

        self.search_entry.pack(
            side="left"
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_students
        )

        if self.class_name is None:

            self.class_dropdown = ctk.CTkComboBox(
                top_bar,
                width=180,
                height=48,
                values=get_all_class_names(),
                command=self.filter_by_class
            )

            self.class_dropdown.pack(
                side="right"
            )

            self.class_dropdown.set("AU-CS")
            self.class_name = "AU-CS"

        if self.back_command:

            back_btn = ctk.CTkButton(
                top_bar,
                text="← Back",
                width=120,
                height=48,
                corner_radius=14,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 15, "bold"),
                command=self.go_back
            )

            back_btn.pack(
                side="right",
                padx=(0, 10)
            )

        # BODY
        body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        body.grid_columnconfigure(0, weight=7)
        body.grid_columnconfigure(1, weight=4)
        body.grid_rowconfigure(0, weight=1)

        # LEFT
        table_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        table_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 18)
        )

        ctk.CTkLabel(
            table_frame,
            text="Student List",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(28, 20)
        )

        self.scroll_table = ctk.CTkScrollableFrame(
            table_frame,
            fg_color="transparent"
        )

        self.scroll_table.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 25)
        )

        # RIGHT
        preview = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        preview.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        ctk.CTkLabel(
            preview,
            text="Student Preview",
            font=("Segoe UI", 26, "bold")
        ).pack(
            anchor="w",
            padx=30,
            pady=(28, 25)
        )

        self.preview_name = ctk.CTkLabel(
            preview,
            text="Select a Student",
            font=("Segoe UI", 24, "bold")
        )

        self.preview_name.pack(
            anchor="w",
            padx=30,
            pady=(20, 10)
        )

        self.preview_code = ctk.CTkLabel(
            preview,
            text="Code: -",
            font=("Segoe UI", 16)
        )

        self.preview_code.pack(
            anchor="w",
            padx=30
        )

        self.preview_class = ctk.CTkLabel(
            preview,
            text="Class: -",
            font=("Segoe UI", 16)
        )

        self.preview_class.pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        self.preview_average = ctk.CTkLabel(
            preview,
            text="Average: -",
            font=("Segoe UI", 16)
        )

        self.preview_average.pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        self.preview_risk = ctk.CTkLabel(
            preview,
            text="Risk: -",
            font=("Segoe UI", 18, "bold")
        )

        self.preview_risk.pack(
            anchor="w",
            padx=30,
            pady=(15, 0)
        )

        self.preview_scores = ctk.CTkLabel(
            preview,
            text="",
            justify="left",
            font=("Segoe UI", 15)
        )

        self.preview_scores.pack(
            anchor="w",
            padx=30,
            pady=(20, 0)
        )

        if self.class_name:

            self.filter_by_class(self.class_name)

        else:

            self.refresh_student_list()