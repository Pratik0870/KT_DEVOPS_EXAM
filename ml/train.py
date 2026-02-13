import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import mlflow
import os

def train():
    print("Training model...")

    # Load data
    df = pd.read_csv("data/data.csv")

    X = df[["sqft", "bedrooms", "bathrooms"]]
    y = df["price"]

    # MLflow tracking
    mlflow.set_experiment("KT_House_Price")

    with mlflow.start_run():

        model = LinearRegression()
        model.fit(X, y)

        predictions = model.predict(X)

        mae = mean_absolute_error(y, predictions)
        rmse = mean_squared_error(y, predictions) ** 0.5


        # Log parameters
        mlflow.log_param("model_type", "LinearRegression")

        # Log metrics
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("RMSE", rmse)

        # Save model
        os.makedirs("api", exist_ok=True)
        joblib.dump(model, "api/model.pkl")

        print("Model saved successfully!")

if __name__ == "__main__":
    train()
