from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem


def section_title(text, styles):
    return Paragraph(text, styles["Heading2"])


def body(text, styles):
    return Paragraph(text, styles["BodyText"])


def bullet_list(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(item, styles["BodyText"])) for item in items],
        bulletType="bullet",
        leftIndent=14,
    )


def build_pdf(output_path: str) -> None:
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Machine Learning Technology Used",
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCustom", parent=styles["Title"], fontSize=20, leading=24))
    styles["BodyText"].fontSize = 11
    styles["BodyText"].leading = 16

    story = []
    story.append(Paragraph("Machine Learning Technology Used in Heart Disease Prediction System", styles["TitleCustom"]))
    story.append(Spacer(1, 10))
    story.append(body("This document explains the machine learning technologies used in this project, based on the implemented Django prediction flow and the project notebook.", styles))
    story.append(Spacer(1, 14))

    story.append(section_title("1. Core ML Libraries and Tools", styles))
    story.append(bullet_list([
        "scikit-learn: model training, train/test split, and prediction APIs.",
        "pandas: reading dataset (CSV), feature/target extraction, and tabular preprocessing.",
        "numpy: numerical operations and array support.",
        "Python: end-to-end ML and backend integration.",
    ], styles))
    story.append(Spacer(1, 10))

    story.append(section_title("2. Algorithms Used", styles))
    story.append(body("Two ML implementation paths are present in the project:", styles))
    story.append(bullet_list([
        "Production web prediction (Django views): GradientBoostingClassifier from scikit-learn.",
        "Notebook experimentation (Machine_Learning/Heart prediction.ipynb): LogisticRegression with accuracy_score evaluation.",
    ], styles))
    story.append(Spacer(1, 8))
    story.append(body("Additional sklearn model classes (SVC, MLPClassifier) are imported in the web code but not currently used in active prediction flow.", styles))
    story.append(Spacer(1, 10))

    story.append(section_title("3. Active Prediction Pipeline in Django App", styles))
    story.append(body("The function prdict_heart_disease() in health/views.py performs model training and prediction at request time:", styles))
    story.append(bullet_list([
        "Reads dataset from database-linked CSV (Admin_Helath_CSV model).",
        "Selects 13 clinical features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal.",
        "Uses target column for supervised learning.",
        "Splits data using train_test_split(train_size=0.8, random_state=0).",
        "Trains GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).",
        "Predicts on user-entered feature list and calculates test-set score.",
    ], styles))
    story.append(Spacer(1, 10))

    story.append(section_title("4. Notebook-Based ML Flow", styles))
    story.append(body("In Machine_Learning/Heart prediction.ipynb, the implementation uses logistic regression:", styles))
    story.append(bullet_list([
        "train_test_split with test_size=0.2 and stratify=Y.",
        "Model: LogisticRegression().",
        "Evaluation: accuracy_score on both training and test sets.",
    ], styles))
    story.append(Spacer(1, 10))

    story.append(section_title("5. Why These Technologies Fit This Project", styles))
    story.append(bullet_list([
        "Gradient Boosting works well on structured tabular medical data and captures non-linear relationships.",
        "Logistic Regression provides a baseline model that is simple and interpretable.",
        "pandas + sklearn pipeline keeps development straightforward and maintainable for Django integration.",
        "SQLite + CSV approach enables quick prototyping and easy local deployment.",
    ], styles))
    story.append(Spacer(1, 10))

    story.append(section_title("6. Current Limitations in ML Setup", styles))
    story.append(bullet_list([
        "Model is retrained on every prediction request (inefficient for production).",
        "No persisted trained model artifact (e.g., joblib file) is used.",
        "Minimal validation/reporting beyond accuracy score.",
        "No explicit feature scaling in active gradient boosting path (not always necessary, but should be consistent by design).",
        "Limited model comparison and hyperparameter tuning in production path.",
    ], styles))
    story.append(Spacer(1, 10))

    story.append(section_title("7. Suggested Next Improvements", styles))
    story.append(bullet_list([
        "Train once offline and save model with joblib/pickle; load model at app startup.",
        "Add robust evaluation metrics (precision, recall, F1, ROC-AUC, confusion matrix).",
        "Version dataset and model for traceability.",
        "Validate and constrain user inputs with form-level ranges and categorical controls.",
        "Add periodic retraining workflow instead of per-request training.",
    ], styles))
    story.append(Spacer(1, 12))

    story.append(body("Generated for: Heart Disease Prediction System project", styles))

    doc.build(story)


if __name__ == "__main__":
    build_pdf("ML_TECHNOLOGY_DETAILED.pdf")
    print("Created ML_TECHNOLOGY_DETAILED.pdf")
