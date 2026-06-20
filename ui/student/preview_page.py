import customtkinter as ctk

from ai.predictor import predict_student
from ai.recommender import generate_recommendation
from reports.student_pdf_generator import export_student_pdf


class StudentPreviewPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#071224"
        )

        self.student_data = None

        self.build_ui()

    def build_ui(self):

        # ==================================
        # TITLE
        # ==================================
        ctk.CTkLabel(
            self,
            text="Student Performance Predictor",
            font=("Segoe UI", 40, "bold")
        ).pack(
            pady=(20, 10)
        )

        # ==================================
        # MAIN CONTAINER
        # ==================================
        main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(10, 20)
        )

        main_frame.grid_columnconfigure(
            0,
            weight=5
        )

        main_frame.grid_columnconfigure(
            1,
            weight=5
        )

        main_frame.grid_rowconfigure(
            0,
            weight=1
        )

        # ==================================
        # LEFT CARD
        # ==================================
        input_card = ctk.CTkFrame(
            main_frame,
            fg_color="#0F172A",
            corner_radius=25
        )

        input_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 15)
        )

        ctk.CTkLabel(
            input_card,
            text="Student Information",
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=(20, 15)
        )

        self.name_entry = ctk.CTkEntry(
            input_card,
            width=300,
            height=40,
            placeholder_text="Student Name"
        )

        self.name_entry.pack(
            pady=(0, 20)
        )

        ctk.CTkLabel(
            input_card,
            text="Assessment Scores",
            font=("Segoe UI", 24, "bold")
        ).pack(
            pady=(0, 15)
        )

        self.entries = {}

        subjects = [
            "Attendance",
            "Quiz",
            "Homework",
            "Assignment",
            "Midterm",
            "Final",
            "Participation",
            "Project",
            "Behavior"
        ]

        scores_frame = ctk.CTkFrame(
            input_card,
            fg_color="transparent"
        )

        scores_frame.pack(
            padx=20,
            pady=(10, 20)
        )

        for col in range(3):
            scores_frame.grid_columnconfigure(
                col,
                weight=1
            )

        subjects = [
            "Attendance",
            "Quiz",
            "Homework",
            "Assignment",
            "Midterm",
            "Final",
            "Participation",
            "Project",
            "Behavior"
        ]

        self.entries = {}

        for i, field in enumerate(subjects):

            row = i // 3
            col = i % 3

            item = ctk.CTkFrame(
                scores_frame,
                fg_color="transparent"
            )

            item.grid(
                row=row,
                column=col,
                padx=12,
                pady=12
            )

            ctk.CTkLabel(
                item,
                text=field,
                font=("Segoe UI", 18, "bold")
            ).pack(
                pady=(0, 5)
            )

            entry = ctk.CTkEntry(
                item,
                width=160,
                height=40,
                font=("Segoe UI", 16)
            )

            entry.pack()

            self.entries[field] = entry

        ctk.CTkButton(
            input_card,
            text="Predict Result",
            height=45,
            font=("Segoe UI", 16, "bold"),
            command=self.predict
        ).pack(
            pady=25
        )

        # ==================================
        # RIGHT CARD
        # ==================================
        output_card = ctk.CTkFrame(
            main_frame,
            fg_color="#0F172A",
            corner_radius=25
        )

        output_card.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        ctk.CTkLabel(
            output_card,
            text="Prediction Result",
            font=("Segoe UI", 28, "bold")
        ).pack(
            pady=(20, 20)
        )

        # ==================================
        # RESULT CARDS
        # ==================================
        stats_frame = ctk.CTkFrame(
            output_card,
            fg_color="transparent"
        )

        stats_frame.pack(
            fill="x",
            padx=20
        )

        stats_frame.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        avg_card = ctk.CTkFrame(
            stats_frame,
            fg_color="#111827",
            corner_radius=20
        )

        avg_card.grid(
            row=0,
            column=0,
            padx=8,
            sticky="ew"
        )

        self.avg_label = ctk.CTkLabel(
            avg_card,
            text="Average\n-",
            font=("Segoe UI", 24, "bold"),
            text_color="#3B82F6"
        )

        self.avg_label.pack(
            pady=20
        )

        pred_card = ctk.CTkFrame(
            stats_frame,
            fg_color="#111827",
            corner_radius=20
        )

        pred_card.grid(
            row=0,
            column=1,
            padx=8,
            sticky="ew"
        )

        self.predicted_label = ctk.CTkLabel(
            pred_card,
            text="Predicted\n-",
            font=("Segoe UI", 24, "bold"),
            text_color="#10B981"
        )

        self.predicted_label.pack(
            pady=20
        )

        risk_card = ctk.CTkFrame(
            stats_frame,
            fg_color="#111827",
            corner_radius=20
        )

        risk_card.grid(
            row=0,
            column=2,
            padx=8,
            sticky="ew"
        )

        self.risk_label = ctk.CTkLabel(
            risk_card,
            text="Risk\n-",
            font=("Segoe UI", 24, "bold"),
            text_color="#EF4444"
        )

        self.risk_label.pack(
            pady=20
        )

        # ==================================
        # RECOMMENDATION HEADER
        # ==================================
        header = ctk.CTkFrame(
            output_card,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(25, 10)
        )

        ctk.CTkLabel(
            header,
            text="AI Recommendation",
            font=("Segoe UI", 22, "bold")
        ).pack(
            side="left"
        )

        ctk.CTkFrame(
            output_card,
            height=3,
            fg_color="#10B981"
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.export_btn = ctk.CTkButton(
            header,
            width=180,
            height=42,
            text="Export PDF",
            fg_color="#10B981",
            hover_color="#059669",
            text_color="white",
            command=self.export_pdf
        )

        self.export_btn.pack(
            side="right"
        )

        # ==================================
        # RECOMMENDATION BOX
        # ==================================
        self.recommendation_box = ctk.CTkTextbox(
            output_card,
            font=("Segoe UI", 17),
            corner_radius=15,
            border_width=1,
            border_color="#1E293B"
        )

        self.recommendation_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # ==================================
    # PREDICT
    # ==================================
    def predict(self):

        try:

            attendance = float(
                self.entries["Attendance"].get()
            )

            quiz = float(
                self.entries["Quiz"].get()
            )

            homework = float(
                self.entries["Homework"].get()
            )

            assignment = float(
                self.entries["Assignment"].get()
            )

            midterm = float(
                self.entries["Midterm"].get()
            )

            final = float(
                self.entries["Final"].get()
            )

            participation = float(
                self.entries["Participation"].get()
            )

            project = float(
                self.entries["Project"].get()
            )

            behavior = float(
                self.entries["Behavior"].get()
            )

        except ValueError:

            self.recommendation_box.delete(
                "1.0",
                "end"
            )

            self.recommendation_box.insert(
                "1.0",
                "Please enter valid scores."
            )

            return

        result = predict_student(
            attendance,
            quiz,
            homework,
            assignment,
            midterm,
            final,
            participation,
            project,
            behavior
        )

        average = round(
            (
                attendance +
                quiz +
                homework +
                assignment +
                midterm +
                final +
                participation +
                project +
                behavior
            ) / 9,
            1
        )

        recommendation = generate_recommendation(
            attendance,
            quiz,
            homework,
            assignment,
            midterm,
            final,
            participation,
            project,
            behavior,
            result["predicted_score"],
            result["risk_level"]
        )

        self.avg_label.configure(
            text=f"Average\n{average}%"
        )

        self.predicted_label.configure(
            text=f"Predicted\n{result['predicted_score']}%"
        )

        risk = result["risk_level"]

        color = "#10B981"

        if risk == "Medium":
            color = "#F59E0B"

        elif risk == "High":
            color = "#EF4444"

        self.risk_label.configure(
            text=f"Risk\n{risk}",
            text_color=color
        )

        self.recommendation_box.delete(
            "1.0",
            "end"
        )

        self.recommendation_box.insert(
            "1.0",
            recommendation
        )

        self.student_data = {
            "name": self.name_entry.get() or "Student",
            "id": "N/A",
            "class": "Preview Mode",
            "attendance": attendance,
            "quiz": quiz,
            "homework": homework,
            "assignment": assignment,
            "midterm": midterm,
            "final": final,
            "participation": participation,
            "project": project,
            "behavior": behavior,
            "average": average,
            "predicted_score": result["predicted_score"],
            "risk": result["risk_level"],
            "recommendation": recommendation
        }

        self.export_btn.configure(
            state="normal"
        )

    # ==================================
    # EXPORT PDF
    # ==================================
    def export_pdf(self):

        if self.student_data:
            export_student_pdf(
                self.student_data
            )
        
        if not self.student_data:

            self.recommendation_box.delete("1.0", "end")

            self.recommendation_box.insert(
                "1.0",
                "Please predict a result before exporting."
            )

            return