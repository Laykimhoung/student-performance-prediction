# 🎓 EduVision AI (Student Performance Prediction)

> Student Performance Prediction System

An AI-powered system for academic performance monitoring, risk prediction, and early intervention.

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Python](https://img.shields.io/badge/Python-3.11.x-blue)
![Desktop App](https://img.shields.io/badge/Platform-Desktop-green)

---

## 📌 Project Overview

**EduVision AI** is a modern desktop-based student management system designed to monitor academic performance, predict at-risk students, and recommend intervention strategies using Artificial Intelligence.

The project is inspired by modern educational analytics systems and research on AI-enhanced student performance monitoring.

The goal of this system is to help schools, teachers, and administrators:

- Monitor student academic performance
- Detect students at academic risk
- Generate AI-powered recommendations
- Analyze class performance through dashboards
- Manage multiple classes and teachers
- Provide student self-analysis tools

This project is currently **under development** and continuously improving.

---

## 🚧 Project Status

> **Work In Progress (WIP)**

**EduVision AI** is actively being developed.

Current development focus includes:

- [ ] Modern Desktop UI Design
- [ ] Role-based Authentication
- [ ] Student Management System
- [ ] Multi-Class Management
- [ ] Teacher Dashboard
- [ ] Student Prediction Sandbox
- [ ] AI Risk Prediction Model
- [ ] Analytics Dashboard
- [ ] Charts & Data Visualization
- [ ] PDF Report Generation
- [ ] Database Architecture

---
## 🛠️ Technologies Used

This project is powered by the following technologies:

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| CustomTkinter | Modern Desktop GUI |
| SQLite | Local Database |
| Pandas | Data Processing |
| NumPy | AI calculations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data Visualization |
| Plotly | Interactive Charts |
| ReportLab | PDF Report Generation |
| openpyxl | Excel Report Generation |
| Pillow | Image Processing |

---
## 🚀 Installation & Setup

Follow these steps to run **EduVision AI** locally. But make sure you already have Python version **3.11.X**.

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Laykimhoung/student-performance-prediction.git
cd student-performance-prediction
```

---

### Step 2 — Create a Virtual Environment​​

Create a local Python virtual environment with Python 3.11:

```bash
py -3.11 -m venv .venv
```


---

### Step 3 — Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

After activation, your terminal should look similar to:

```txt
(.venv) C:\EduVision-AI>
```

---

### Step 4 — Install Required Libraries

Install all project dependencies:

```bash
pip install -r requirements.txt
```

This automatically installs:

- CustomTkinter
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Plotly
- ReportLab
- openpyxl
- Pillow

---

### Step 5 — Run the Application

Start **EduVision AI**:

```bash
python app.py
```

---
## 💼 Setup Database

Follow these steps to run **eduvision.db** locally.

---
### Step 1 — Delete the file eduvision.db fist
just delete that file, then we will create new for your local computer in next step.

---

### Step 2 — Run schema.py​

Create a local database table:

```bash
python -m database.schema
```

---
### Step 3 — Run seed.py
Create a fake data in database to view:

```bash
python -m database.seed
```
---

## ✨ Core Features

### 👑 Admin System

- Manage teachers
- Create and manage classes
- Assign teachers to multiple classes
- Monitor all students
- View analytics and reports
- Manage system-wide settings

### 👨‍🏫 Teacher System

- Secure login
- Access assigned classes
- Add, edit, delete students
- Track student performance
- Generate AI predictions
- Export reports
- View analytics dashboard

### 🎓 Student System

- No login required
- Select available class
- Enter academic information
- Instantly receive AI predictions
- View intervention recommendations

> Student prediction mode acts as a **sandbox** and does **not save data** to the database.

---

## 🤖 AI Features

**EduVision AI** uses machine learning techniques to:

- Predict academic risk levels
- Detect weak academic performance
- Suggest intervention strategies
- Generate academic insights

Prediction outputs include:

- Low Risk
- Medium Risk
- High Risk
- Risk Probability Score
- Personalized Recommendations

Example:

```text
Risk Level: Medium

Risk Score: 63%

Recommendation:
• Improve attendance
• Increase study time
• Join tutoring sessions
```

---

## 📊 Analytics & Visualization

The system includes interactive dashboards and data visualization:

- Student Risk Distribution
- Attendance Trends
- Performance Analysis
- Class Comparison
- High-Risk Student Detection
- AI Insights Dashboard

Charts supported:

- Pie Charts
- Line Graphs
- Bar Charts
- Performance Comparisons

---

## 🔐 System Roles

### Admin

Full system access:

- Manage teachers
- Manage classes
- View analytics
- Monitor system performance

### Teacher

Class-based access:

- Manage assigned classes
- Add and update student data
- Generate reports
- View AI predictions

### Student

Quick self-analysis mode:

- Select class
- Enter academic metrics
- View instant AI feedback

---

## 👨‍💻 Developer

**Lay Kimhoung (Xakuraii)**

Computer Science Student

---
