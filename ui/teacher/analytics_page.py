import customtkinter as ctk

from database.crud import (
    get_all_class_names,
    get_analytics_summary,
    get_assessment_averages,
    get_risk_distribution,
    get_high_risk_students,
    get_score_distribution
)

from ui.teacher.analytics_charts import (
    create_risk_donut_chart,
    create_assessment_chart,
    create_score_histogram
)


class AnalyticsPage(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        class_data=None,
        back_command=None
    ):
        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.class_data = class_data
        self.back_command = back_command

        # ==========================
        # CURRENT CLASS
        # ==========================
        self.selected_class = (
            class_data["name"]
            if class_data
            else None
        )

        # ==========================
        # DATA
        # ==========================
        self.load_data()

        # ==========================
        # BUILD UI
        # ==========================
        self.build_ui()

    # ==================================
    # LOAD DATA
    # ==================================
    def load_data(self):

        summary = get_analytics_summary(
            self.selected_class
        )

        self.total_students = summary[0] or 0
        self.high_risk = summary[1] or 0
        self.medium_risk = summary[2] or 0
        self.low_risk = summary[3] or 0

        self.assessment_data = (
            get_assessment_averages(
                self.selected_class
            )
        )

        self.risk_distribution = (
            get_risk_distribution(
                self.selected_class
            )
        )

        self.high_risk_students = (
            get_high_risk_students(
                self.selected_class
            )
        )

        self.score_distribution = (
            get_score_distribution(
                self.selected_class
            )
        )

    # ==================================
    # REFRESH PAGE
    # ==================================
    def refresh_page(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.load_data()

        self.build_ui()

    # ==================================
    # CLASS CHANGED
    # ==================================
    def on_class_change(
        self,
        selected_class
    ):

        self.selected_class = selected_class

        self.refresh_page()

    # ==================================
    # BUILD UI
    # ==================================
    def build_ui(self):

        # ==================================
        # HEADER
        # ==================================
        top_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_bar.pack(
            fill="x",
            padx=35,
            pady=(25, 5)
        )

        title_frame = ctk.CTkFrame(
            top_bar,
            fg_color="transparent"
        )

        title_frame.pack(
            side="left"
        )

        ctk.CTkLabel(
            title_frame,
            text="Analytics",
            font=("Segoe UI", 40, "bold")
        ).pack(
            anchor="w"
        )

        # ==================================
        # BACK BUTTON
        # ==================================
        if self.back_command:

            back_btn = ctk.CTkButton(
                top_bar,
                text="← Back",
                width=140,
                height=46,
                corner_radius=16,
                fg_color="#EF4444",
                hover_color="#DC2626",
                font=("Segoe UI", 16, "bold"),
                command=self.back_command
            )

            back_btn.pack(
                side="right"
            )

        # ==================================
        # FILTER BAR
        # ==================================
        filter_bar = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        filter_bar.pack(
            fill="x",
            padx=35,
            pady=20
        )

        # ==============================
        # CLASSROOM MODE
        # ==============================
        if self.class_data:

            class_box = ctk.CTkFrame(
                filter_bar,
                fg_color="#111827",
                corner_radius=14,
                width=220,
                height=46
            )

            class_box.pack(
                side="left"
            )

            class_box.pack_propagate(False)

            ctk.CTkLabel(
                class_box,
                text=self.selected_class,
                font=("Segoe UI", 15, "bold")
            ).pack(
                pady=10
            )

        # ==============================
        # SIDEBAR MODE
        # ==============================
        else:

            class_dropdown = ctk.CTkComboBox(
                filter_bar,
                width=220,
                height=46,
                values=get_all_class_names(),
                command=self.on_class_change,
                corner_radius=14,
                button_color="#EF4444",
                button_hover_color="#DC2626"
            )

            class_dropdown.pack(
                side="left"
            )

            if self.selected_class:

                class_dropdown.set(
                    self.selected_class
                )

            else:

                classes = get_all_class_names()

                if classes:

                    if self.selected_class is None:

                        default_class = None

                        for cls in classes:

                            if "CS" in cls.upper():
                                default_class = cls
                                break

                        if default_class is None:
                            default_class = classes[0]

                        self.selected_class = default_class

                        class_dropdown.set(default_class)

                        self.after(
                            100,
                            lambda: self.on_class_change(default_class)
                        )
        
        # ==================================
        # MAIN BODY
        # ==================================
        body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 20)
        )

        body.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        body.grid_rowconfigure(
            0,
            weight=1,
            minsize=430
        )

        body.grid_rowconfigure(
            1,
            weight=1,
            minsize=430
        )
        # ==================================
        # RISK DONUT CHART
        # ==================================
        
        donut_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=460,
        )
        
        donut_frame.grid_propagate(False)

        donut_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=8,
            pady=8
        )

        create_risk_donut_chart(
            donut_frame,
            self.high_risk,
            self.medium_risk,
            self.low_risk
        )

        # ==================================
        # ASSESSMENT BAR CHART
        # ==================================
        assessment_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=460,
        )

        assessment_frame.grid_propagate(False)

        assessment_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8,
            pady=8
        )

        assessment_values = []

        if self.assessment_data:

            assessment_values = [
                value if value is not None else 0
                for value in self.assessment_data
            ]

        create_assessment_chart(
            assessment_frame,
            assessment_values
        )

        # ==================================
        # SCORE HISTOGRAM
        # ==================================
        histogram_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28,
            height=460,
        )

        histogram_frame.grid_propagate(False)

        histogram_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=8,
            pady=8
        )

        create_score_histogram(
            histogram_frame,
            self.score_distribution
        )

        # ==================================
        # HIGH RISK STUDENTS
        # ==================================

        risk_students_frame = ctk.CTkFrame(
            body,
            fg_color="#0F172A",
            corner_radius=28
        )

        risk_students_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=8,
            pady=8
        )

        ctk.CTkLabel(
            risk_students_frame,
            text="High Risk Students",
            font=("Segoe UI", 20, "bold")
        ).pack(
            pady=(15, 10)
        )

        student_list = ctk.CTkScrollableFrame(
            risk_students_frame,
            fg_color="transparent"
        )

        student_list.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        for student in self.high_risk_students:

            name = student[0]
            average = student[1]

            row = ctk.CTkFrame(
                student_list,
                fg_color="#111827",
                corner_radius=12
            )

            row.pack(
                fill="x",
                pady=5
            )

            ctk.CTkLabel(
                row,
                text=name,
                font=("Segoe UI", 14, "bold")
            ).pack(
                side="left",
                padx=15,
                pady=10
            )

            ctk.CTkLabel(
                row,
                text=f"{average:.1f}",
                text_color="#EF4444",
                font=("Segoe UI", 14, "bold")
            ).pack(
                side="right",
                padx=15
            )