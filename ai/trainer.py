import os
import joblib
import pandas as pd

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from database.db import get_connection


MODEL_DIR = "ai/model"

RISK_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "risk_model.pkl"
)

SCORE_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "score_model.pkl"
)


def load_training_data():

    conn = get_connection()

    query = """
    SELECT

        a.attendance,
        a.quiz,
        a.homework,
        a.assignment,
        a.midterm,
        a.final,
        a.participation,
        a.project,
        a.behavior,

        p.risk_level,

        a.average

    FROM assessments a

    JOIN predictions p
        ON a.student_id = p.student_id
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df


def train_models():

    print("Loading training data...")

    df = load_training_data()

    features = [
        "attendance",
        "quiz",
        "homework",
        "assignment",
        "midterm",
        "final",
        "participation",
        "project",
        "behavior"
    ]

    X = df[features]

    # ==========================
    # RISK MODEL
    # ==========================

    y_risk = df["risk_level"]

    risk_model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    risk_model.fit(
        X,
        y_risk
    )

    # ==========================
    # SCORE MODEL
    # ==========================

    y_score = df["average"]

    score_model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    score_model.fit(
        X,
        y_score
    )

    # ==========================
    # SAVE MODELS
    # ==========================

    os.makedirs(
        MODEL_DIR,
        exist_ok=True
    )

    joblib.dump(
        risk_model,
        RISK_MODEL_PATH
    )

    joblib.dump(
        score_model,
        SCORE_MODEL_PATH
    )

    print(
        "Models trained and saved successfully."
    )


if __name__ == "__main__":

    train_models()