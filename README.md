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
* [✨ Core Features](#-core-features)
* [🤖 AI Features](#-ai-features)
* [🛠️ Technologies Used](#️-technologies-used)
* [🖼 User Interface](#️-user-interface)
* [🚀 Installation & Setup](#-installation--setup)
* [🔄 Rebuild Database & AI Model](#-rebuild-database--ai-model)
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
## 🖼User Interface

<img width="1920" height="1080" alt="14" src="https://github.com/user-attachments/assets/e21e40eb-2196-45e2-876d-1391aad5045f" />
<img width="1920" height="1080" alt="15" src="https://github.com/user-attachments/assets/0d596674-ff2e-4628-9395-0a5da9abfe3f" />
<img width="1920" height="1080" alt="16" src="https://github.com/user-attachments/assets/b8e68f93-a43e-48ff-b062-40eabf213c50" />
<img width="1920" height="1080" alt="17" src="https://github.com/user-attachments/assets/bfd6094a-753c-4613-95b8-cfbc9260f837" />
<img width="1920" height="1080" alt="18" src="https://github.com/user-attachments/assets/73df297b-ae41-4772-aa01-af738596ea86" />
<img width="1920" height="1080" alt="19" src="https://github.com/user-attachments/assets/8fc98ecf-c8e5-431b-8d1e-a2fd4ecfc7aa" />

---

# 🚀 Installation & Setup
⚠️ **Before starting, make sure you have Python 3.11.X installed. Most of the libraries and dependencies used in this project were developed and tested with Python 3.11, and using other versions may cause installation or compatibility issues.**

## 1. Clone Repository

Open **VS Code Terminal** or **Command Prompt**:

```bash
git clone https://github.com/Laykimhoung/student-performance-prediction.git
cd student-performance-prediction
```

---

## 2. Create Virtual Environment

Open **VS Code Terminal** and run:

```bash
py -3.11 -m venv .venv
```

This creates an isolated Python environment for the project.

---

## 3. Activate Virtual Environment
In **VS Code Terminal** and run:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate

```
If successful, you should see:
```text
(.venv) PS C:\YourProject\student-performance-prediction>
```

✅ This means the virtual environment is active.

---

### ⚠️ First-Time PowerShell Users

If you receive an error similar to:

```text
running scripts is disabled on this system
```

You must allow PowerShell scripts to run.

### Step A — Open PowerShell as Administrator

1. Search for **PowerShell**
2. Right-click **Windows PowerShell**
3. Select **Run as Administrator**

Run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

When prompted:

```text
Do you want to change the execution policy?
[Y] Yes
```

Type:

```text
Y
```

and press **Enter**.

---

### Step B — Activate Environment

Return to the **VS Code Terminal** and run:

```powershell
.venv\Scripts\Activate.ps1
```

If successful, you should see:

```text
(.venv) PS C:\YourProject\student-performance-prediction>
```

✅ This means the virtual environment is active.

---

## 4. Install Dependencies

With the virtual environment activated, run in the **VS Code Terminal**:

```bash
pip install -r requirements.txt
```

### ⏳ Please Be Patient

The installation may appear stuck while installing large packages. Depending on your internet speed and computer performance, installation may take:

```text
5–10 minutes
```

Do NOT close the terminal.

Wait until you see:

```text
Successfully installed ...
```

before proceeding.

---

## 🔧 Troubleshooting Installation Issues

### Problem 1: Installation Failed

If package installation fails or the application reports missing modules such as:

```text
No module named 'customtkinter'
```

or

```text
No module named 'PIL'
```

recreate the virtual environment.

### Step 1 — Deactivate Environment

Run in **VS Code Terminal**:

```powershell
deactivate
```

### Step 2 — Delete Old Virtual Environment

```powershell
Remove-Item -Recurse -Force .venv
```

### Step 3 — Create New Virtual Environment

```powershell
py -3.11 -m venv .venv
```

### Step 4 — Activate Environment

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5 — Reinstall Dependencies

```powershell
pip install -r requirements.txt
```

Wait until installation finishes completely.

---

## 5. Run Application

Run this to start EduVision AI:

```bash
python app.py
```

If everything is installed correctly, EduVision AI will launch successfully.
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
