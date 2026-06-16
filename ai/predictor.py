import joblib
import pandas as pd


RISK_MODEL_PATH = "ai/model/risk_model.pkl"
SCORE_MODEL_PATH = "ai/model/score_model.pkl"


# ==================================
# LOAD MODELS
# ==================================

risk_model = joblib.load(RISK_MODEL_PATH)

score_model = joblib.load(SCORE_MODEL_PATH)


# ==================================
# PREDICT
# ==================================

def predict_student(
    attendance,
    quiz,
    homework,
    assignment,
    midterm,
    final,
    participation,
    project,
    behavior
):

    data = pd.DataFrame([{
        "attendance": attendance,
        "quiz": quiz,
        "homework": homework,
        "assignment": assignment,
        "midterm": midterm,
        "final": final,
        "participation": participation,
        "project": project,
        "behavior": behavior
    }])

    predicted_score = float(
        score_model.predict(data)[0]
    )

    predicted_risk = str(
        risk_model.predict(data)[0]
    )

    return {
        "predicted_score": round(
            predicted_score,
            1
        ),
        "risk_level": predicted_risk
    }