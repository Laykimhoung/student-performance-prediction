# 🎓 EduVision AI

> **AI-Enhanced Student Performance Prediction and Management System**

An intelligent desktop application designed to monitor academic performance, predict at-risk students, and provide academic intervention recommendations using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Desktop-CustomTkinter-green)
![Database](https://img.shields.io/badge/Database-SQLite-blue)
![AI](https://img.shields.io/badge/AI-Scikit--Learn-orange)

---

## 📑 Table of Contents

* [📌 Project Overview](#-project-overview)
* [🚀 Installation & Setup](#-installation--setup)
* [🔄 Rebuild Database & AI Model](#-rebuild-database--ai-model)
* [✨ Core Features](#-core-features)
* [🤖 AI Features](#-ai-features)
* [🛠️ Technologies Used](#️-technologies-used)
* [⚙️ How the System Works](#️-how-the-system-works)
* [👨‍💻 Developer](#-developer)

---

## 📌 Project Overview

**EduVision AI** is a desktop-based student management system that combines traditional academic management with Artificial Intelligence to support academic performance monitoring and early intervention.

The system enables teachers and administrators to manage students, classes, assessments, and reports while utilizing Machine Learning models to identify at-risk students and generate personalized recommendations.

### Objectives

* Monitor academic performance
* Predict student risk levels
* Provide AI-powered recommendations
* Support early academic intervention
* Analyze classroom performance
* Improve educational decision-making

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Laykimhoung/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Create Virtual Environment

```bash
py -3.11 -m venv .venv
```

### 3. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
python app.py
```

> The repository already includes the database and trained AI models. Most users only need to install the requirements and run the application.

---

## 🔄 Rebuild Database & AI Model

If you want to generate a fresh demo database and retrain the AI model from scratch, follow these steps:

### Step 1 — Delete Database

Delete:

```text
database/eduvision.db
```

### Step 2 — Recreate Database Tables

```bash
python -m database.schema
```

### Step 3 — Generate Demo Data

```bash
python -m database.seed
```

### Step 4 — Retrain AI Models

```bash
python -m ai.trainer
```

This will automatically overwrite the existing AI model files:

```text
ai/model/risk_model.pkl
ai/model/score_model.pkl
```

After training is completed, simply run:

```bash
python app.py
```

to start EduVision AI with the newly generated database and AI models.

---

## ✨ Core Features

### 👑 Admin Module
Full system access:

* Secure login system
* Manage teachers
* Manage classes
* Assign teachers to classes
* Monitor student records
* Add, edit, and delete students
* System overview dashboard

### 👨‍🏫 Teacher Module
Class-level access:

* Secure login system
* Manage assigned classes
* Record assessment scores
* Generate AI predictions
* Export Class Inforamtion to PDF and Excel
* Export reports to PDF
* View classroom analytics

### 🎓 Student Prediction Sandbox
Prediction-only access:

* No login required
* Enter assessment scores manually
* Receive instant AI predictions
* View personalized recommendations
* Export prediction report as PDF

> Student Sandbox Mode is used for demonstration and self-analysis purposes. Data entered here is not stored in the database.

---

## 🤖 AI Features

EduVision AI uses Machine Learning techniques to evaluate student performance based on multiple academic indicators.

### Prediction Factors

* Attendance
* Quiz
* Homework
* Assignment
* Midterm Exam
* Final Exam
* Participation
* Project
* Behavior

### AI Outputs

* Predicted Academic Score
* Risk Classification
* Performance Analysis
* Personalized Recommendations

### Risk Levels

| Risk Level     | Description                   |
| -------------- | ----------------------------- |
| 🟢 Low Risk    | Student is performing well    |
| 🟡 Medium Risk | Student requires monitoring   |
| 🔴 High Risk   | Student requires intervention |

---

## 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python 3.11   | Core Programming Language |
| CustomTkinter | Modern Desktop GUI        |
| SQLite        | Local Database            |
| Pandas        | Data Processing           |
| NumPy         | Numerical Computation     |
| Scikit-Learn  | Machine Learning          |
| Matplotlib    | Data Visualization        |
| ReportLab     | PDF Report Generation     |
| OpenPyXL      | Excel Export              |


---

## ⚙️ How the System Works

### Step 1 — Data Collection

Teachers enter student assessment scores into the system.

### Step 2 — Academic Evaluation

The system calculates student performance metrics and academic indicators.

### Step 3 — AI Prediction

The trained Machine Learning model analyzes student performance patterns and predicts:

* Academic Score
* Risk Level
* Intervention Priority

### Step 4 — Recommendation Generation

The recommendation engine generates personalized improvement suggestions based on student weaknesses.

### Step 5 — Reporting

Users can export performance reports and prediction results in PDF format.

---

## 👨‍💻 Developer

### Lay Kimhoung (Xakuraii)

Computer Science Student

**Project:** EduVision AI
**Version:** 1.0
**Year:** 2026

---

### Academic Research Topic

**Artificial Intelligence in Student Management Systems to Enhance Academic Performance Monitoring and Intervention**
