# KT DevOps & MLOps Practical

## 📌 Project Overview
This project demonstrates an end-to-end ML DevOps pipeline for predicting house prices.

The system includes:
- DVC for data versioning
- MLflow for experiment tracking
- FastAPI for model serving
- Docker & Docker Compose for containerization
- GitHub Actions for CI/CD
- Email alert system on failure

---

## 🔄 Project Workflow

1. Dataset tracked using DVC
2. Model trained using Scikit-learn
3. Metrics logged using MLflow (MAE, RMSE)
4. Model saved as model.pkl
5. FastAPI serves prediction endpoint
6. Email alert triggered on failure
7. Docker containerizes application
8. GitHub Actions builds & tests automatically

---

## ▶️ Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python ml/train.py
uvicorn api.app:app --reload
